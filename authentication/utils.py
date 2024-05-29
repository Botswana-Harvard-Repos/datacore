from allauth.account.models import EmailAddress
from allauth.account import app_settings
from allauth.utils import get_user_model


def email_address_exists(email, exclude_user=None):
    emailaddresses = EmailAddress.objects
    if exclude_user:
        emailaddresses = emailaddresses.exclude(user=exclude_user)
    ret = emailaddresses.filter(email__iexact=email).count() > 0
    if not ret:
        email_field = app_settings.USER_MODEL_EMAIL_FIELD
        if email_field:
            users = get_user_model().objects
            if exclude_user:
                users = users.exclude(pk=exclude_user.pk)
            ret = users.filter(
                **{email_field + "__iexact": email}).count() > 0
    return ret


def has_verified_email(user, email=None):
    emailaddress = None
    if email:
        ret = False
        try:
            emailaddress = EmailAddress.objects.get_for_user(user, email)
            ret = emailaddress.verified
        except EmailAddress.DoesNotExist:
            pass
    else:
        ret = EmailAddress.objects.filter(user=user, verified__in=[True]).count() > 0
    return ret
