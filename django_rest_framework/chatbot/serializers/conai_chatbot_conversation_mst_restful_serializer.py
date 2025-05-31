# serializers/conai_chatbot_conversation_mst_restful_serializer.py

import uuid
from rest_framework import serializers
from ..domain.CONAI_CHATBOT_CONVERSATION_MST import ConaiChatbotConversationMst, ConaiChatbotConversationMstMod


class ConaiChatbotConversationMstGetSerializer(serializers.Serializer):
    conaiChatbotConversationMstId = serializers.UUIDField(
        source='conai_chatbot_conversation_mst_id',
        required=False,
        help_text='Primary key for the conversation table',
    )
    sessionId = serializers.UUIDField(
        source='session_id',
        required=False,
        help_text='Identifier for the conversation session',
    )
    title = serializers.CharField(
        required=False,
        help_text='Title of the conversation',
    )
    userId = serializers.CharField(
        source='user_id',
        required=False,
        help_text='Identifier for the user participating in the conversation',
    )
    createdAt = serializers.DateTimeField(
        source='created_at',
        required=False,
        help_text='Timestamp when the conversation was created',
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at',
        required=False,
        help_text='Timestamp when the conversation was last updated',
    )

class ConaiChatbotConversationMstPostSerializer(serializers.ModelSerializer):
    conaiChatbotConversationMstId = serializers.UUIDField(
        source='conai_chatbot_conversation_mst_id',
        default=uuid.uuid4,
        required=False,
        help_text='Primary key for the conversation table',
    )
    sessionId = serializers.UUIDField(
        source='session_id',
        default=uuid.uuid4,
        required=False,
        help_text='Identifier for the conversation session',
    )
    title = serializers.CharField(
        required=False,
        help_text='Title of the conversation',
    )
    userId = serializers.CharField(
        source='user_id',
        required=True,
        help_text='Identifier for the user participating in the conversation',
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at',
    #     required=False,
    #     help_text='Timestamp when the conversation was created',
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at',
    #     required=False,
    #     help_text='Timestamp when the conversation was last updated',
    # )

    class Meta:
        model = ConaiChatbotConversationMstMod
        fields = [
            'conaiChatbotConversationMstId',
            'sessionId',
            'title',
            'userId',
            # 'createdAt',
            # 'updatedAt',
        ]

class ConaiChatbotConversationMstPutSerializer(serializers.ModelSerializer):
    conaiChatbotConversationMstId = serializers.UUIDField(
        source='conai_chatbot_conversation_mst_id',
        required=False,
        help_text='Primary key for the conversation table',
    )
    sessionId = serializers.UUIDField(
        source='session_id',
        required=True,
        help_text='Identifier for the conversation session',
    )
    title = serializers.CharField(
        required=False,
        help_text='Title of the conversation',
    )
    userId = serializers.CharField(
        source='user_id',
        required=True,
        help_text='Identifier for the user participating in the conversation',
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at',
    #     required=False,
    #     help_text='Timestamp when the conversation was created',
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at',
    #     required=False,
    #     help_text='Timestamp when the conversation was last updated',
    # )

    class Meta:
        model = ConaiChatbotConversationMstMod
        fields = [
            'conaiChatbotConversationMstId',
            'sessionId',
            'title',
            'userId',
            # 'createdAt',
            # 'updatedAt',
        ]

class ConaiChatbotConversationMstDeleteSerializer(serializers.ModelSerializer):
    conaiChatbotConversationMstId = serializers.UUIDField(
        source='conai_chatbot_conversation_mst_id',
        required=True,
        help_text='Primary key for the conversation table',
    )

    class Meta:
        model = ConaiChatbotConversationMst
        fields = ['conaiChatbotConversationMstId']
