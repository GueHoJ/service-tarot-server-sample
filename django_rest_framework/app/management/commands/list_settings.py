from django.conf import settings
from django.core.management.base import BaseCommand


# List all settings from settings.py
class Command(BaseCommand):
    help = 'List all settings from settings.py'

    def handle(self, *args, **options):
        self.stdout.write("Django settings:")
        for setting in dir(settings):
            if setting.isupper():
                self.stdout.write(f"{setting}: {getattr(settings, setting)}")
