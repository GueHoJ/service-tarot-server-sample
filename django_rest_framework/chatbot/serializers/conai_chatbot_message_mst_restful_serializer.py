# serializers/conai_chatbot_message_mst_restful_serializer.py

import uuid
from rest_framework import serializers
from ..domain.CONAI_CHATBOT_MESSAGE_MST import ConaiChatbotMessageMst, ConaiChatbotMessageMstMod


class ConaiChatbotMessageMstGetSerializer(serializers.Serializer):
    conaiChatbotMessageMstId = serializers.UUIDField(
        source='conai_chatbot_message_mst_id',
        required=False,
        help_text='Primary key for the message table',
    )
    conversationId = serializers.UUIDField(
        source='conversation_id',
        required=False,
        help_text='Links to conai_chatbot_conversation_mst_id',
    )
    userId = serializers.CharField(
        source='user_id',
        allow_null=True,
        required=False,
        help_text='User who sent the message',
    )
    role = serializers.CharField(
        required=False,
        help_text='Role of the entity sending the message (system/user/assistant)',
    )
    message = serializers.CharField(
        allow_null=True,
        required=False,
        help_text='Content of the message',
    )
    mediaType = serializers.CharField(
        source='media_type',
        allow_null=True,
        required=False,
        help_text="Type of media: 'image', 'video', etc.",
    )
    mediaUrl = serializers.CharField(
        source='media_url',
        allow_null=True,
        required=False,
        help_text='URL or path to the media content',
    )
    createdAt = serializers.DateTimeField(
        source='created_at',
        required=False,
        help_text='Timestamp when the message was created',
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at',
        required=False,
        help_text='Timestamp when the message was last updated',
    )

class ConaiChatbotMessageMstPostSerializer(serializers.ModelSerializer):
    conaiChatbotMessageMstId = serializers.UUIDField(
        source='conai_chatbot_message_mst_id',
        default=uuid.uuid4,
        required=False,
        help_text='Primary key for the message table',
    )
    conversationId = serializers.UUIDField(
        source='conversation_id',
        required=True,
        help_text='Links to conai_chatbot_conversation_mst_id',
    )
    userId = serializers.CharField(
        source='user_id',
        allow_null=True,
        required=False,
        help_text='User who sent the message',
    )
    role = serializers.CharField(
        required=True,
        help_text='Role of the entity sending the message (system/user/assistant)',
    )
    message = serializers.CharField(
        allow_null=True,
        required=False,
        help_text='Content of the message',
    )
    mediaType = serializers.CharField(
        source='media_type',
        allow_null=True,
        required=False,
        help_text="Type of media: 'image', 'video', etc.",
    )
    mediaUrl = serializers.CharField(
        source='media_url',
        allow_null=True,
        required=False,
        help_text='URL or path to the media content',
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at',
    #     required=False,
    #     help_text='Timestamp when the message was created',
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at',
    #     required=False,
    #     help_text='Timestamp when the message was last updated',
    # )

    class Meta:
        model = ConaiChatbotMessageMstMod
        fields = [
            'conaiChatbotMessageMstId',
            'conversationId',
            'userId',
            'role',
            'message',
            'mediaType',
            'mediaUrl',
            # 'createdAt',
            # 'updatedAt',
        ]

class ConaiChatbotMessageMstPutSerializer(serializers.ModelSerializer):
    conaiChatbotMessageMstId = serializers.UUIDField(
        source='conai_chatbot_message_mst_id',
        required=False,
        help_text='Primary key for the message table',
    )
    conversationId = serializers.UUIDField(
        source='conversation_id',
        required=True,
        help_text='Links to conai_chatbot_conversation_mst_id',
    )
    userId = serializers.CharField(
        source='user_id',
        allow_null=True,
        required=False,
        help_text='User who sent the message',
    )
    role = serializers.CharField(
        required=True,
        help_text='Role of the entity sending the message (system/user/assistant)',
    )
    message = serializers.CharField(
        allow_null=True,
        required=False,
        help_text='Content of the message',
    )
    mediaType = serializers.CharField(
        source='media_type',
        allow_null=True,
        required=False,
        help_text="Type of media: 'image', 'video', etc.",
    )
    mediaUrl = serializers.CharField(
        source='media_url',
        allow_null=True,
        required=False,
        help_text='URL or path to the media content',
    )
    createdAt = serializers.DateTimeField(
        source='created_at',
        required=False,
        help_text='Timestamp when the message was created',
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at',
        required=False,
        help_text='Timestamp when the message was last updated',
    )

    class Meta:
        model = ConaiChatbotMessageMst
        fields = [
            'conaiChatbotMessageMstId',
            'conversationId',
            'userId',
            'role',
            'message',
            'mediaType',
            'mediaUrl',
            'createdAt',
            'updatedAt',
        ]

class ConaiChatbotMessageMstDeleteSerializer(serializers.ModelSerializer):
    conaiChatbotMessageMstId = serializers.UUIDField(
        source='conai_chatbot_message_mst_id',
        required=True,
        help_text='Primary key for the message table',
    )

    class Meta:
        model = ConaiChatbotMessageMst
        fields = ['conaiChatbotMessageMstId']
