from django.core import signing
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from allauth.account import app_settings, signals
from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress

from .managers import CustomUserManager
from allauth.account.utils import user_email


class User(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username} {self.email}'

    @property
    def user_initials(self):
        initials = ''
        if self.first_name and self.last_name:
            if (len(self.first_name.split(' ')) > 1):
                first = self.first_name.split(' ')[0]
                middle = self.first_name.split(' ')[1]
                initials = f'{first[:1]}{middle[:1]}{self.last_name[:1]}'
            else:
                initials = f'{self.first_name[:1]}{self.last_name[:1]}'
        return initials


class EmailConfirmationHMAC:
    """ Override confirmation HMAC for djongo consideration of booolean querying.
    """
    def __init__(self, email_address):
        self.email_address = email_address

    @property
    def key(self):
        return signing.dumps(obj=self.email_address.pk, salt=app_settings.SALT)

    @classmethod
    def from_key(cls, key):
        try:
            max_age = 60 * 60 * 24 * app_settings.EMAIL_CONFIRMATION_EXPIRE_DAYS
            pk = signing.loads(key, max_age=max_age, salt=app_settings.SALT)
            ret = EmailConfirmationHMAC(
                EmailAddress.objects.get(pk=pk, verified__in=[False]))
        except (
            signing.SignatureExpired,
            signing.BadSignature,
            EmailAddress.DoesNotExist,
        ):
            ret = None
        return ret

    def confirm(self, request):
        if not self.email_address.verified:
            email_address = self.email_address
            get_adapter(request).confirm_email(request, email_address)
            signals.email_confirmed.send(
                sender=self.__class__,
                request=request,
                email_address=email_address,
            )
            return email_address

    def send(self, request=None, signup=False):
        get_adapter(request).send_confirmation_mail(request, self, signup)
        signals.email_confirmation_sent.send(
            sender=self.__class__,
            request=request,
            confirmation=self,
            signup=signup,
        )


def set_email_as_primary(email_address_obj, conditional=False):
    email_model_cls = email_address_obj.__class__
    user = email_address_obj.user
    email = email_address_obj.email
    old_primary = None
    try:
        old_primary = email_model_cls.objects.get(
            user=user, primary__in=[True])
    except email_model_cls.DoesNotExist:
        pass
    else:
        if conditional:
            return False
        old_primary.primary = False
        old_primary.save()
    email_address_obj.primary = True
    email_address_obj.save()
    user_email(user, email)
    user.save()
    return True
