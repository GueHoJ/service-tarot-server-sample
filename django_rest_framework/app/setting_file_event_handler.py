import os
import time
import sys
import importlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.conf import settings


class SettingsFileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Construct the full path to settings_vault.py
        settings_vault_path = os.path.abspath(os.path.join(BASE_DIR, 'project', 'config', 'settings_vault.py'))

        # Check if the modified file is settings_vault.py
        if event.src_path == settings_vault_path:
            print(f"{event.src_path} has been modified. Reloading settings...")
            self.reload_settings()

    def reload_settings(self):
        try:
            # Unload the settings module if it's already loaded
            if 'project.config.settings_vault' in sys.modules:
                del sys.modules['project.config.settings_vault']

            # Reload the settings_vault module
            settings_vault = importlib.import_module('project.config.settings_vault')

            # Re-configure Django settings with the reloaded settings
            settings.configure(default_settings=settings_vault)
            print("Settings reloaded successfully!")
        except Exception as e:
            print(f"Error reloading settings: {e}")


if __name__ == "__main__":
    # Get the base directory of the project
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Set the path to settings_vault.py
    settings_vault_path = os.path.join(BASE_DIR, 'project', 'config', 'settings_vault.py')

    # Set up file event handling
    event_handler = SettingsFileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(settings_vault_path), recursive=False)
    observer.start()

    print(f"Watching {settings_vault_path} for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
