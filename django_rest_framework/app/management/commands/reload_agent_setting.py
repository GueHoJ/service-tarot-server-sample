# management/commands/reload_settings.py
from django.core.management.base import BaseCommand
import importlib
import sys


class Command(BaseCommand):
    help = "Reload Django settings"

    def handle(self, *args, **kwargs):
        try:
            # Unload the settings module
            del sys.modules['project.config.settings_vault']

            # Reload the module using importlib
            importlib.import_module('project.config.settings_vault')

            # Reassign the reloaded settings to Django's settings
            from django.conf import settings
            settings.configure(default_settings=importlib.import_module('project.config.settings_vault'))
            self.stdout.write(self.style.SUCCESS('Vault settings reloaded successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error Vault reloading settings: {e}"))
