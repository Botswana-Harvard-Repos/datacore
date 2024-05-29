from allauth.account import app_settings as allauth_account_settings
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.utils.translation import gettext_lazy as _

from .models import User
from .utils import email_address_exists


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CustomRegisterSerializer(RegisterSerializer):
    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _('A user is already registered with this e-mail address.'),
                )
        return email


class CustomLoginSerializer(LoginSerializer):
    @staticmethod
    def validate_email_verification_status(user):
        if (
            allauth_account_settings.EMAIL_VERIFICATION == allauth_account_settings.EmailVerificationMethod.MANDATORY
            and not user.emailaddress_set.filter(email=user.email, verified__in=[True]).count() > 0
        ):
            raise serializers.ValidationError(_('E-mail is not verified.'))
