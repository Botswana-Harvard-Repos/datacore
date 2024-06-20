from allauth import ratelimit
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.app_settings import EmailVerificationMethod
from allauth.account import app_settings
from allauth.utils import get_user_model, build_absolute_uri
from allauth.account.utils import send_email_confirmation
from datetime import timedelta

from django import forms
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .utils import email_address_exists, has_verified_email
from .models import set_email_as_primary


class CustomAccountAdapter(DefaultAccountAdapter):

    def confirm_email(self, request, email_address):
        """
        Marks the email address as confirmed on the db
        """
        email_address.verified = True
        set_email_as_primary(email_address, conditional=True)
        email_address.save()

    def clean_username(self, username, shallow=False):
        """
        Validates the username. You can hook into this if you want to
        (dynamically) restrict what usernames can be chosen.
        """
        for validator in app_settings.USERNAME_VALIDATORS:
            validator(username)

        # TODO: Add regexp support to USERNAME_BLACKLIST
        username_blacklist_lower = [
            ub.lower() for ub in app_settings.USERNAME_BLACKLIST
        ]
        if username.lower() in username_blacklist_lower:
            raise forms.ValidationError(self.error_messages["username_blacklisted"])
        # Skipping database lookups when shallow is True, needed for unique
        # username generation.
        if not shallow:
            from allauth.account.utils import filter_users_by_username

            if filter_users_by_username(username).count() > 0:
                user_model = get_user_model()
                username_field = app_settings.USER_MODEL_USERNAME_FIELD
                error_message = user_model._meta.get_field(
                    username_field
                ).error_messages.get("unique")
                if not error_message:
                    error_message = self.error_messages["username_taken"]
                raise forms.ValidationError(
                    error_message,
                    params={
                        "model_name": user_model.__name__,
                        "field_label": username_field,
                    },
                )
        return username

    def validate_unique_email(self, email):
        if email_address_exists(email):
            raise forms.ValidationError(self.error_messages["email_taken"])
        return email

    def should_send_confirmation_mail(self, request, email_address):
        from allauth.account.models import EmailConfirmation

        cooldown_period = timedelta(seconds=app_settings.EMAIL_CONFIRMATION_COOLDOWN)
        if app_settings.EMAIL_CONFIRMATION_HMAC:
            send_email = ratelimit.consume(
                request,
                action="confirm_email",
                key=email_address.email.lower(),
                amount=1,
                duration=cooldown_period.total_seconds(),
            )
        else:
            send_email = not EmailConfirmation.objects.filter(
                sent__gt=timezone.now() - cooldown_period,
                email_address=email_address,
            ).count() > 0
        return send_email

    def pre_login(
        self,
        request,
        user,
        *,
        email_verification,
        signal_kwargs,
        email,
        signup,
        redirect_url
    ):

        if not user.is_active:
            return self.respond_user_inactive(request, user)

        if email_verification == EmailVerificationMethod.NONE:
            pass
        elif email_verification == EmailVerificationMethod.OPTIONAL:
            # In case of OPTIONAL verification: send on signup.
            if not has_verified_email(user, email) and signup:
                send_email_confirmation(request, user, signup=signup, email=email)
        elif email_verification == EmailVerificationMethod.MANDATORY:
            if not has_verified_email(user, email):
                send_email_confirmation(request, user, signup=signup, email=email)
                return self.respond_email_verification_sent(request, user)

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = reverse('authentication:account_confirm_email', args=[emailconfirmation.key])
        ret = build_absolute_uri(request, url)
        return ret

    def respond_email_verification_sent(self, request, user):
        return HttpResponseRedirect(
            reverse('authentication:account_email_verification_sent'))
