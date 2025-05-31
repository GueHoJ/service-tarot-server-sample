# management/commands/reload_settings.py
from django.core.management.base import BaseCommand
import importlib
import sys


class Command(BaseCommand):
    help = "Reload Django settings"

    def handle(self, *args, **kwargs):
        try:
            # Unload the settings module
            del sys.modules['project.settings']

            # Reload the module using importlib
            importlib.import_module('project.settings')

            # Reassign the reloaded settings to Django's settings
            from django.conf import settings
            settings.configure(default_settings=importlib.import_module('project.settings'))
            self.stdout.write(self.style.SUCCESS('Settings reloaded successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error settings reloading settings: {e}"))
