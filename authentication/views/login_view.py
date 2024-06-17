from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.urls.base import reverse


class UserLoginView(ObtainAuthToken):
    """ User login API view to validate credentials for user and
        assign token if successful.
    """
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
            return Response(
                {'token': token.key,
                 'username': user.username,
                 'role': user.role})
        else:
            return Response(
                {'message':
                 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED)


def login_page(request):
    """ Function-based view to render login page.
    """
    if request.user.is_authenticated:
        return redirect(reverse('tsepamo:tsepamo-dashboard'))
    else:
        return render(request, 'authentication/login.html')
