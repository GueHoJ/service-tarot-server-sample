# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConaiTarotServiceDefaultMessageMst(models.Model):
    conai_tarot_service_default_message_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each message')
    message_type = models.CharField(max_length=50, db_comment='Type of the message (e.g., "system", "trigger")')
    message_content = models.TextField(db_comment='Content of the system or trigger message')
    version = models.CharField(max_length=50, db_comment='Version identifier for the message')
    is_active = models.BooleanField(blank=True, null=True, db_comment='Indicates whether this message is currently active. Default is FALSE')
    description = models.TextField(blank=True, null=True, db_comment='Description of the message or its purpose')
    chatbot_gpt_parameters_mst_id = models.UUIDField(blank=True, null=True, db_comment='Foreign key to the GPT parameters table')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of record creation')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of last record update')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_default_message_mst'
        unique_together = (('message_type', 'version'),)
        db_table_comment = 'Table to manage system and trigger messages for Conai Tarot Service'


class ConaiTarotServiceDefaultMessageMstMod(models.Model):
    conai_tarot_service_default_message_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each message')
    message_type = models.CharField(max_length=50, db_comment='Type of the message (e.g., "system", "trigger")')
    message_content = models.TextField(db_comment='Content of the system or trigger message')
    version = models.CharField(max_length=50, db_comment='Version identifier for the message')
    is_active = models.BooleanField(blank=True, null=True, db_comment='Indicates whether this message is currently active. Default is FALSE')
    description = models.TextField(blank=True, null=True, db_comment='Description of the message or its purpose')
    chatbot_gpt_parameters_mst_id = models.UUIDField(blank=True, null=True, db_comment='Foreign key to the GPT parameters table')
    # created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of record creation')
    # updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of last record update')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_default_message_mst'
        unique_together = (('message_type', 'version'),)
        db_table_comment = 'Table to manage system and trigger messages for Conai Tarot Service'