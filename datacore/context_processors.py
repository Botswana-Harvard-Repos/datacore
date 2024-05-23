from importlib import import_module
from django.conf import settings


def navbar_links(request):
    navbar_links = []

    # Iterate through installed apps
    for app_config in settings.INSTALLED_APPS:
        try:
            # Import the app's urls.py module
            app_config = app_config.split('.apps', 1)[0]
            urls_module = import_module(app_config + '.urls')
            # app_name = getattr(urls_module, 'app_name', '')

            # Extract navbar links from the app's URL patterns
            # for url_pattern in urls_module.urlpatterns:
            if hasattr(urls_module, 'navbar_links'):
                navbar_links.extend(urls_module.navbar_links)
        except ImportError:
            pass

    return {'navbar_links': navbar_links}
