from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = getattr(settings, "DJANGO_SUPERUSER_USERNAME", None)
        email = getattr(settings, "DJANGO_SUPERUSER_EMAIL", None)
        password = getattr(settings, "DJANGO_SUPERUSER_PASSWORD", None)
        try:
            u = None
            if not User.objects.filter(username=username).exists() and not User.objects.filter(is_superuser=True).exists():
                print("admin user not found, creating one")

                # new_password = get_random_string(10)

                u = User.objects.create_superuser(username, email, password)
                print(f"===================================")
                print(f"A superuser '{username}' was created with email '{email}' and password '{password}'")
                print(f"===================================")
            else:
                print("admin user found. Skipping super user creation")
                print(u)
        except Exception as e:
            print(f"There was an error: {e}")
