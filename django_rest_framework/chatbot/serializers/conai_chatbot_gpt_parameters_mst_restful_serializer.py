import uuid
from django.utils import timezone

from rest_framework import serializers
from ..domain.CONAI_CHATBOT_GPT_PARAMETERS_MST import ConaiChatbotGptParametersMst


class ConaiChatbotGptParametersMstGetSerializer(serializers.Serializer):
    conaiChatbotGptParametersMstId = serializers.UUIDField(
        source='conai_chatbot_gpt_parameters_mst_id', required=False,
        help_text='Unique identifier for each parameter set.'
    )
    userId = serializers.CharField(
        source='user_id', required=False, help_text='Unique identifier for each user.'
    )
    sessionId = serializers.CharField(
        source='session_id', allow_null=True, required=False, help_text='Identifier for the chatbot session.'
    )
    configName = serializers.CharField(
        source='config_name', required=False, help_text='Name of the configuration preset.'
    )
    model = serializers.CharField(
        required=False, help_text='AI model used for chatbot interactions.'
    )
    temperature = serializers.FloatField(
        required=False, help_text='Controls randomness in model output.'
    )
    maxTokens = serializers.IntegerField(
        source='max_tokens', required=False, help_text='Maximum number of tokens to generate in a response.'
    )
    stopSequences = serializers.JSONField(
        source='stop_sequences', allow_null=True, required=False, help_text='Stop sequences as a JSON array.'
    )
    topP = serializers.FloatField(
        source='top_p', required=False, help_text='Top-p sampling for nucleus sampling.'
    )
    frequencyPenalty = serializers.FloatField(
        source='frequency_penalty', required=False, help_text='Penalty for token frequency repetition.'
    )
    presencePenalty = serializers.FloatField(
        source='presence_penalty', required=False, help_text='Penalty for encouraging new topics.'
    )
    description = serializers.CharField(
        required=False, allow_null=True, help_text='Explanation or description of the preset.'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', allow_null=True, required=False, help_text='Timestamp when the row was created.'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False, help_text='Timestamp when the row was last updated.'
    )


class ConaiChatbotGptParametersMstPostSerializer(serializers.ModelSerializer):
    conaiChatbotGptParametersMstId = serializers.UUIDField(
        source='conai_chatbot_gpt_parameters_mst_id', required=False, default=uuid.uuid4,
        help_text='Unique identifier for each parameter set.'
    )
    userId = serializers.CharField(
        source='user_id', required=False, help_text='Unique identifier for each user.'
    )
    sessionId = serializers.CharField(
        source='session_id', allow_null=True, required=False, default=uuid.uuid4, help_text='Identifier for the chatbot session.'
    )
    configName = serializers.CharField(
        source='config_name', required=False, help_text='Name of the configuration preset.'
    )
    model = serializers.CharField(
        required=False, help_text='AI model used for chatbot interactions.'
    )
    temperature = serializers.FloatField(
        required=False, help_text='Controls randomness in model output.'
    )
    maxTokens = serializers.IntegerField(
        source='max_tokens', required=False, help_text='Maximum number of tokens to generate in a response.'
    )
    stopSequences = serializers.JSONField(
        source='stop_sequences', allow_null=True, required=False, default=list, help_text='Stop sequences as a JSON array.'
    )
    topP = serializers.FloatField(
        source='top_p', required=False, help_text='Top-p sampling for nucleus sampling.'
    )
    frequencyPenalty = serializers.FloatField(
        source='frequency_penalty', required=False, help_text='Penalty for token frequency repetition.'
    )
    presencePenalty = serializers.FloatField(
        source='presence_penalty', required=False, help_text='Penalty for encouraging new topics.'
    )
    description = serializers.CharField(
        required=False, allow_null=True, help_text='Explanation or description of the preset.'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', allow_null=True, required=False, default=timezone.now, help_text='Timestamp when the row was created.'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False, default=timezone.now, help_text='Timestamp when the row was last updated.'
    )

    class Meta:
        model = ConaiChatbotGptParametersMst
        fields = [
            'conaiChatbotGptParametersMstId', 'userId', 'sessionId', 'configName', 'model',
            'temperature', 'maxTokens', 'stopSequences', 'topP', 'frequencyPenalty',
            'presencePenalty', 'description', 'createdAt', 'updatedAt'
        ]


class ConaiChatbotGptParametersMstPutSerializer(serializers.ModelSerializer):
    conaiChatbotGptParametersMstId = serializers.UUIDField(
        source='conai_chatbot_gpt_parameters_mst_id', required=False,
        help_text='Unique identifier for each parameter set.'
    )
    userId = serializers.CharField(
        source='user_id', required=False, help_text='Unique identifier for each user.'
    )
    sessionId = serializers.CharField(
        source='session_id', allow_null=True, required=False, help_text='Identifier for the chatbot session.'
    )
    configName = serializers.CharField(
        source='config_name', required=False, help_text='Name of the configuration preset.'
    )
    model = serializers.CharField(
        required=False, help_text='AI model used for chatbot interactions.'
    )
    temperature = serializers.FloatField(
        required=False, help_text='Controls randomness in model output.'
    )
    maxTokens = serializers.IntegerField(
        source='max_tokens', required=False, help_text='Maximum number of tokens to generate in a response.'
    )
    stopSequences = serializers.JSONField(
        source='stop_sequences', allow_null=True, required=False, default=list, help_text='Stop sequences as a JSON array.'
    )
    topP = serializers.FloatField(
        source='top_p', required=False, help_text='Top-p sampling for nucleus sampling.'
    )
    frequencyPenalty = serializers.FloatField(
        source='frequency_penalty', required=False, help_text='Penalty for token frequency repetition.'
    )
    presencePenalty = serializers.FloatField(
        source='presence_penalty', required=False, help_text='Penalty for encouraging new topics.'
    )
    description = serializers.CharField(
        required=False, allow_null=True, help_text='Explanation or description of the preset.'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', allow_null=True, required=False, help_text='Timestamp when the row was created.'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False, help_text='Timestamp when the row was last updated.'
    )

    class Meta:
        model = ConaiChatbotGptParametersMst
        fields = [
            'conaiChatbotGptParametersMstId', 'userId', 'sessionId', 'configName', 'model',
            'temperature', 'maxTokens', 'stopSequences', 'topP', 'frequencyPenalty',
            'presencePenalty', 'description', 'createdAt', 'updatedAt'
        ]


class ConaiChatbotGptParametersMstDeleteSerializer(serializers.ModelSerializer):
    conaiChatbotGptParametersMstId = serializers.UUIDField(
        source='conai_chatbot_gpt_parameters_mst_id', required=True,
        help_text='Unique identifier for each parameter set.'
    )

    class Meta:
        model = ConaiChatbotGptParametersMst
        fields = ['conaiChatbotGptParametersMstId']
