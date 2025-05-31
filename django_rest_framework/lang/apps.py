from django.apps import AppConfig
from lang.utils.load_lama_model import get_model


class LangConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lang'

    # def ready(self):
    #     # Initialize the model on startup
    #     print("Initializing Llama model...")
    #     get_model()
