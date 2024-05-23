"""
URL configuration for datacore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from authentication.views import login_page, user_logout_handle
from authentication.views import UserLoginView, UserLogoutView, UserRegistrationView

from .views import main_page

urlpatterns = [
    path('', login_page, name='login'),
    path('logout/', user_logout_handle, name='logout'),

    # Authentication API urls
    path('api/auth/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/auth/login/', UserLoginView.as_view(), name='user-login'),
    path('api/auth/logout/', UserLogoutView.as_view(), name='user-logout'),

    path('dashboard/', main_page, name='dashboard'),
    path('admin/', admin.site.urls),
    # Tsepamo
    path('tsepamo/', include('tsepamo.urls')),
]
