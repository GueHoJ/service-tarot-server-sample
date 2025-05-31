# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConaiChatbotConversationHistoryMst(models.Model):
    conai_chatbot_conversation_history_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key for the conversation history table')
    conversation_id = models.UUIDField(db_comment='Related conversation')
    user_id = models.CharField(max_length=255, db_comment='Identifier for the user participating in the conversation')
    history_data = models.JSONField(db_comment='JSONB field storing the conversation history')
    created_at = models.DateTimeField(db_comment='Timestamp when the history was created')
    updated_at = models.DateTimeField(db_comment='Timestamp when the history was last updated')

    class Meta:
        managed = False
        db_table = 'conai_chatbot_conversation_history_mst'
        db_table_comment = 'Table storing detailed history of chatbot conversations'


class ConaiChatbotConversationHistoryMstMod(models.Model):
    conai_chatbot_conversation_history_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key for the conversation history table')
    conversation_id = models.UUIDField(db_comment='Related conversation')
    user_id = models.CharField(max_length=255, db_comment='Identifier for the user participating in the conversation')
    history_data = models.JSONField(db_comment='JSONB field storing the conversation history')
    # created_at = models.DateTimeField(db_comment='Timestamp when the history was created')
    # updated_at = models.DateTimeField(db_comment='Timestamp when the history was last updated')

    class Meta:
        managed = False
        db_table = 'conai_chatbot_conversation_history_mst'
        db_table_comment = 'Table storing detailed history of chatbot conversations'