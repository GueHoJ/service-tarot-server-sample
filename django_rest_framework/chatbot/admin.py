from django.contrib import admin
from .domain.CONAI_CHATBOT_GPT_PARAMETERS_MST import ConaiChatbotGptParametersMst


class GPTParameterAdmin(admin.ModelAdmin):
    """
    Admin interface for GPT Parameters
    """
    list_display = ("conai_chatbot_gpt_parameters_mst_id", "user_id", "session_id", "config_name", "model",
                    "temperature", "max_tokens", "stop_sequences", "top_p", "frequency_penalty", "presence_penalty",
                    "description", "created_at", "updated_at")
    list_filter = ("model", "user_id")  # Enable filtering by model or user
    search_fields = ("user_id__username", "session_id", "model")  # Search by username, session ID, or model
    readonly_fields = ("created_at", "updated_at")  # Make read-only fields
    fieldsets = (
        (None, {
            "fields": (
                "user_id",
                "session_id",
                "config_name",
                "model",
                "temperature",
                "max_tokens",
                "stop_sequences",
                "top_p",
                "frequency_penalty",
                "presence_penalty",
                "description",
            ),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
        }),
    )


# Register the model and custom admin interface
admin.site.register(ConaiChatbotGptParametersMst, GPTParameterAdmin)
