from django.shortcuts import render


def user_profile_page(request):
    """ Function-based view to render user profile page.
    """
    if request.user.is_authenticated:
        return render(request, 'authentication/user_profile.html')
    else:
        return render(request, 'authentication/login.html')
