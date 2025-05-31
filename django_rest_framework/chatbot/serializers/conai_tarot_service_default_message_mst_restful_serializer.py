import uuid
from rest_framework import serializers
from ..domain.CONAI_TAROT_SERVICE_DEFAULT_MESSAGE_MST import ConaiTarotServiceDefaultMessageMst, ConaiTarotServiceDefaultMessageMstMod


class ConaiTarotServiceDefaultMessageMstGetSerializer(serializers.Serializer):
    conaiTarotServiceDefaultMessageMstId = serializers.UUIDField(
        source='conai_tarot_service_default_message_mst_id', required=False,
        help_text='Primary key and unique identifier for each message'
    )
    messageType = serializers.CharField(
        source='message_type', required=False,
        help_text='Type of the message (e.g., "system", "trigger")'
    )
    messageContent = serializers.CharField(
        source='message_content', required=False,
        help_text='Content of the system or trigger message'
    )
    version = serializers.CharField(
        required=False,
        help_text='Version identifier for the message'
    )
    isActive = serializers.BooleanField(
        source='is_active', required=False,
        help_text='Indicates whether this message is currently active'
    )
    description = serializers.CharField(
        required=False, allow_null=True,
        help_text='Description of the message or its purpose'
    )
    chatbotGptParametersMstId = serializers.UUIDField(
        source='chatbot_gpt_parameters_mst_id', required=False,
        allow_null=True, help_text='Foreign key to the GPT parameters table'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', required=False, allow_null=True,
        help_text='Timestamp of record creation'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', required=False, allow_null=True,
        help_text='Timestamp of last record update'
    )


class ConaiTarotServiceDefaultMessageMstPostSerializer(serializers.ModelSerializer):
    conaiTarotServiceDefaultMessageMstId = serializers.UUIDField(
        source='conai_tarot_service_default_message_mst_id', default=uuid.uuid4, required=False,
        help_text='Primary key and unique identifier for each message'
    )
    messageType = serializers.CharField(
        source='message_type', required=True,
        help_text='Type of the message (e.g., "system", "trigger")'
    )
    messageContent = serializers.CharField(
        source='message_content', required=True,
        help_text='Content of the system or trigger message'
    )
    version = serializers.CharField(
        required=True,
        help_text='Version identifier for the message'
    )
    isActive = serializers.BooleanField(
        source='is_active', required=False, default=False,
        help_text='Indicates whether this message is currently active'
    )
    description = serializers.CharField(
        required=False, allow_null=True,
        help_text='Description of the message or its purpose'
    )
    chatbotGptParametersMstId = serializers.UUIDField(
        source='chatbot_gpt_parameters_mst_id', required=False,
        allow_null=True, help_text='Foreign key to the GPT parameters table'
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at', required=False, allow_null=True,
    #     help_text='Timestamp of record creation'
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at', required=False, allow_null=True,
    #     help_text='Timestamp of last record update'
    # )

    class Meta:
        model = ConaiTarotServiceDefaultMessageMstMod
        fields = [
            'conaiTarotServiceDefaultMessageMstId', 'messageType', 'messageContent', 'version',
            'isActive', 'description', 'chatbotGptParametersMstId',
            # 'createdAt', 'updatedAt'
        ]


class ConaiTarotServiceDefaultMessageMstPutSerializer(serializers.ModelSerializer):
    conaiTarotServiceDefaultMessageMstId = serializers.UUIDField(
        source='conai_tarot_service_default_message_mst_id', required=False,
        help_text='Primary key and unique identifier for each message'
    )
    messageType = serializers.CharField(
        source='message_type', required=True,
        help_text='Type of the message (e.g., "system", "trigger")'
    )
    messageContent = serializers.CharField(
        source='message_content', required=True,
        help_text='Content of the system or trigger message'
    )
    version = serializers.CharField(
        required=True,
        help_text='Version identifier for the message'
    )
    isActive = serializers.BooleanField(
        source='is_active', required=False, default=False,
        help_text='Indicates whether this message is currently active'
    )
    description = serializers.CharField(
        required=False, allow_null=True,
        help_text='Description of the message or its purpose'
    )
    chatbotGptParametersMstId = serializers.UUIDField(
        source='chatbot_gpt_parameters_mst_id', required=False,
        allow_null=True, help_text='Foreign key to the GPT parameters table'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', required=False, allow_null=True,
        help_text='Timestamp of record creation'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', required=False, allow_null=True,
        help_text='Timestamp of last record update'
    )

    class Meta:
        model = ConaiTarotServiceDefaultMessageMst
        fields = [
            'conaiTarotServiceDefaultMessageMstId', 'messageType', 'messageContent', 'version',
            'isActive', 'description', 'chatbotGptParametersMstId', 'createdAt', 'updatedAt'
        ]


class ConaiTarotServiceDefaultMessageMstDeleteSerializer(serializers.ModelSerializer):
    conaiTarotServiceDefaultMessageMstId = serializers.UUIDField(
        source='conai_tarot_service_default_message_mst_id', required=True,
        help_text='Primary key and unique identifier for each message'
    )

    class Meta:
        model = ConaiTarotServiceDefaultMessageMst
        fields = ['conaiTarotServiceDefaultMessageMstId']
