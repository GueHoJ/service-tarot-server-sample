# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConaiChatbotGptParametersMst(models.Model):
    conai_chatbot_gpt_parameters_mst_id = models.UUIDField(primary_key=True, db_comment='Unique identifier for each parameter set.')
    user_id = models.CharField(db_comment='Unique identifier for each user.')
    session_id = models.CharField(blank=True, null=True, db_comment='Identifier for the chatbot session.')
    config_name = models.CharField(max_length=255, db_comment='Name of the configuration preset.')
    model = models.CharField(db_comment='AI model used for chatbot interactions.')
    temperature = models.FloatField(db_comment='Controls randomness in model output.')
    max_tokens = models.IntegerField(db_comment='Maximum number of tokens to generate in a response.')
    stop_sequences = models.JSONField(blank=True, null=True, default=list, db_comment='Stop sequences as a JSON array.')
    top_p = models.FloatField(db_comment='Top-p sampling for nucleus sampling.')
    frequency_penalty = models.FloatField(db_comment='Penalty for token frequency repetition.')
    presence_penalty = models.FloatField(db_comment='Penalty for encouraging new topics.')
    description = models.TextField(blank=True, null=True, db_comment='Explanation or description of the preset.')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp when the row was created.')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp when the row was last updated.')

    class Meta:
        managed = False
        db_table = 'conai_chatbot_gpt_parameters_mst'
        db_table_comment = 'Stores GPT chatbot configuration parameters for each user and session.'


class ConaiChatbotGptParametersMstMod(models.Model):
    conai_chatbot_gpt_parameters_mst_id = models.UUIDField(primary_key=True, db_comment='Unique identifier for each parameter set.')
    user_id = models.CharField(db_comment='Unique identifier for each user.')
    session_id = models.CharField(blank=True, null=True, db_comment='Identifier for the chatbot session.')
    config_name = models.CharField(max_length=255, db_comment='Name of the configuration preset.')
    model = models.CharField(db_comment='AI model used for chatbot interactions.')
    temperature = models.FloatField(db_comment='Controls randomness in model output.')
    max_tokens = models.IntegerField(db_comment='Maximum number of tokens to generate in a response.')
    stop_sequences = models.JSONField(blank=True, null=True, db_comment='Stop sequences as a JSON array.')
    top_p = models.FloatField(db_comment='Top-p sampling for nucleus sampling.')
    frequency_penalty = models.FloatField(db_comment='Penalty for token frequency repetition.')
    presence_penalty = models.FloatField(db_comment='Penalty for encouraging new topics.')
    description = models.TextField(blank=True, null=True, db_comment='Explanation or description of the preset.')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp when the row was created.')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp when the row was last updated.')

    class Meta:
        managed = False
        db_table = 'conai_chatbot_gpt_parameters_mst'
        db_table_comment = 'Stores GPT chatbot configuration parameters for each user and session.'