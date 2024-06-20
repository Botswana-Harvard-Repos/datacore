from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from allauth.account.models import EmailConfirmation
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView as BaseVerifyEmailView

from ..models import EmailConfirmationHMAC

#
# def email_confirm_redirect(request, key):
#     return HttpResponseRedirect(
#         f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}/{key}"
#     )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )


class VerifyEmailView(BaseVerifyEmailView):

    def get_object(self, queryset=None):
        key = self.kwargs["key"]
        emailconfirmation = EmailConfirmationHMAC.from_key(key)
        if not emailconfirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                emailconfirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                raise Http404()
        return emailconfirmation


class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.confirm(self.request)
        return render(request, 'email_confirm.html')
