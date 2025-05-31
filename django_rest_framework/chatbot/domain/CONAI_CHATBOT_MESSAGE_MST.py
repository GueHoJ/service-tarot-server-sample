# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConaiChatbotMessageMst(models.Model):
    conai_chatbot_message_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key for the message table')
    conversation_id = models.UUIDField(db_comment='Links to conai_chatbot_conversation_mst_id')
    user_id = models.CharField(max_length=255, blank=True, null=True, db_comment='User who sent the message (plain VARCHAR field)')
    role = models.CharField(max_length=50, db_comment='Role of the entity sending the message (system/user/assistant)')
    message = models.TextField(blank=True, null=True, db_comment='Content of the message')
    media_type = models.CharField(max_length=50, blank=True, null=True, db_comment="Type of media: 'image', 'video', etc.")
    media_url = models.TextField(blank=True, null=True, db_comment='URL or path to the media content')
    created_at = models.DateTimeField(db_comment='Timestamp when the message was created')
    updated_at = models.DateTimeField(db_comment='Timestamp when the message was last updated')

    class Meta:
        managed = False
        db_table = 'conai_chatbot_message_mst'
        db_table_comment = 'Table storing messages exchanged in a conversation'


class ConaiChatbotMessageMstMod(models.Model):
    conai_chatbot_message_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key for the message table')
    conversation_id = models.UUIDField(db_comment='Links to conai_chatbot_conversation_mst_id')
    user_id = models.CharField(max_length=255, blank=True, null=True, db_comment='User who sent the message (plain VARCHAR field)')
    role = models.CharField(max_length=50, db_comment='Role of the entity sending the message (system/user/assistant)')
    message = models.TextField(blank=True, null=True, db_comment='Content of the message')
    media_type = models.CharField(max_length=50, blank=True, null=True, db_comment="Type of media: 'image', 'video', etc.")
    media_url = models.TextField(blank=True, null=True, db_comment='URL or path to the media content')
    # created_at = models.DateTimeField(db_comment='Timestamp when the message was created')
    # updated_at = models.DateTimeField(db_comment='Timestamp when the message was last updated')

    class Meta:
        managed = False
        db_table = 'conai_chatbot_message_mst'
        db_table_comment = 'Table storing messages exchanged in a conversation'