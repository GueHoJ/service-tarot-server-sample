# serializers/conai_chatbot_conversation_history_mst_restful_serializer.py

import uuid
from rest_framework import serializers
from ..domain.CONAI_CHATBOT_CONVERSATION_HISTORY_MST import ConaiChatbotConversationHistoryMst, \
    ConaiChatbotConversationHistoryMstMod


class ConaiChatbotConversationHistoryMstGetSerializer(serializers.Serializer):
    conaiChatbotConversationHistoryMstId = serializers.UUIDField(
        source='conai_chatbot_conversation_history_mst_id',
        required=False,
        help_text='Primary key for the conversation history table',
    )
    conversationId = serializers.UUIDField(
        source='conversation_id',
        required=False,
        help_text='Related conversation',
    )
    userId = serializers.CharField(
        source='user_id',
        required=False,
        help_text='Identifier for the user participating in the conversation',
    )
    historyData = serializers.JSONField(
        source='history_data',
        required=False,
        help_text='JSONB field storing the conversation history',
    )
    createdAt = serializers.DateTimeField(
        source='created_at',
        required=False,
        help_text='Timestamp when the history was created',
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at',
        required=False,
        help_text='Timestamp when the history was last updated',
    )

class ConaiChatbotConversationHistoryMstPostSerializer(serializers.ModelSerializer):
    conaiChatbotConversationHistoryMstId = serializers.UUIDField(
        source='conai_chatbot_conversation_history_mst_id',
        default=uuid.uuid4,
        required=False,
        help_text='Primary key for the conversation history table',
    )
    conversationId = serializers.UUIDField(
        source='conversation_id',
        required=True,
        help_text='Related conversation',
    )
    userId = serializers.CharField(
        source='user_id',
        required=True,
        help_text='Identifier for the user participating in the conversation',
    )
    historyData = serializers.JSONField(
        source='history_data',
        required=True,
        help_text='JSONB field storing the conversation history',
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at',
    #     required=False,
    #     help_text='Timestamp when the history was created',
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at',
    #     required=False,
    #     help_text='Timestamp when the history was last updated',
    # )

    class Meta:
        model = ConaiChatbotConversationHistoryMstMod
        fields = [
            'conaiChatbotConversationHistoryMstId',
            'conversationId',
            'userId',
            'historyData',
            # 'createdAt',
            # 'updatedAt',
        ]

class ConaiChatbotConversationHistoryMstPutSerializer(serializers.ModelSerializer):
    conaiChatbotConversationHistoryMstId = serializers.UUIDField(
        source='conai_chatbot_conversation_history_mst_id',
        required=False,
        help_text='Primary key for the conversation history table',
    )
    conversationId = serializers.UUIDField(
        source='conversation_id',
        required=True,
        help_text='Related conversation',
    )
    userId = serializers.CharField(
        source='user_id',
        required=True,
        help_text='Identifier for the user participating in the conversation',
    )
    historyData = serializers.JSONField(
        source='history_data',
        required=True,
        help_text='JSONB field storing the conversation history',
    )
    createdAt = serializers.DateTimeField(
        source='created_at',
        required=False,
        help_text='Timestamp when the history was created',
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at',
        required=False,
        help_text='Timestamp when the history was last updated',
    )

    class Meta:
        model = ConaiChatbotConversationHistoryMst
        fields = [
            'conaiChatbotConversationHistoryMstId',
            'conversationId',
            'userId',
            'historyData',
            'createdAt',
            'updatedAt',
        ]

class ConaiChatbotConversationHistoryMstDeleteSerializer(serializers.ModelSerializer):
    conaiChatbotConversationHistoryMstId = serializers.UUIDField(
        source='conai_chatbot_conversation_history_mst_id',
        required=True,
        help_text='Primary key for the conversation history table',
    )

    class Meta:
        model = ConaiChatbotConversationHistoryMst
        fields = ['conaiChatbotConversationHistoryMstId']
