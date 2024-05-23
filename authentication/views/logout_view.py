import requests
from django.urls.base import reverse
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'detail': 'Successfully logged out.'})


def user_logout_handle(request):
    if request.method == 'GET':
        user_token = Token.objects.get(user=request.user)
        response = requests.post(
            'http://127.0.0.1:8001/api/auth/logout/',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Token {user_token.key}'})
        if response.status_code == 200:
            return redirect(reverse('login'))
        else:
            response.raise_for_status()
