# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConaiTarotServiceUserMst(models.Model):
    conai_tarot_service_user_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each user')
    user_id = models.CharField(unique=True, max_length=150, db_comment='User`s unique id')
    username = models.CharField(blank=True, null=True,max_length=150, db_comment='User`s unique username')
    nickname = models.CharField(unique=True, max_length=150, db_comment='User`s unique nickname')
    age = models.IntegerField(blank=True, null=True, db_comment='User`s age')
    gender = models.CharField(max_length=10, blank=True, null=True, db_comment='User`s gender')
    job = models.CharField(max_length=50, blank=True, null=True, db_comment='User`s job')
    email = models.CharField(unique=True, max_length=254, db_comment='User`s email address')
    phone_number = models.CharField(unique=True, max_length=15, blank=True, null=True, db_comment='Optional phone number for user contact')
    password = models.CharField(max_length=255, blank=True, null=True, db_comment='User`s password (hashed)')
    profile_picture_url = models.TextField(blank=True, null=True, db_comment='URL to the user`s profile picture')
    status = models.CharField(max_length=50, blank=True, null=True, db_comment='Account status (e.g., active, inactive, banned)')
    is_premium = models.BooleanField(blank=True, null=True, db_comment='Indicates if the user is a premium member')
    is_admin = models.BooleanField(blank=True, null=True, db_comment='Indicates if the user is a admin member')
    language_preference = models.CharField(max_length=10, blank=True, null=True, db_comment='Preferred language for chatbot interactions')
    last_seen = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of the user`s last activity')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of account creation')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of last update')
    chatbot_persona = models.JSONField(blank=True, null=True, db_comment='Configuration for chatbot preferences (e.g., tone, style)')
    metadata = models.JSONField(blank=True, null=True, db_comment='Additional metadata for user (e.g., app-specific settings)')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_user_mst'
        db_table_comment = 'Table to store user information for Conai Tarot Service'


class ConaiTarotServiceUserMstMod(models.Model):
    conai_tarot_service_user_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each user')
    user_id = models.CharField(unique=True, max_length=150, db_comment='User`s unique id')
    username = models.CharField(blank=True, null=True, max_length=150, db_comment='User`s unique username')
    nickname = models.CharField(unique=True, max_length=150, db_comment='User`s unique nickname')
    age = models.IntegerField(blank=True, null=True, db_comment='User`s age')
    gender = models.CharField(max_length=10, blank=True, null=True, db_comment='User`s gender')
    job = models.CharField(max_length=50, blank=True, null=True, db_comment='User`s job')
    email = models.CharField(unique=True, max_length=254, blank=True, null=True, db_comment='User`s email address')
    phone_number = models.CharField(unique=True, max_length=15, blank=True, null=True, db_comment='Optional phone number for user contact')
    password = models.CharField(max_length=255, blank=True, null=True, db_comment='User`s password (hashed)')
    profile_picture_url = models.TextField(blank=True, null=True, db_comment='URL to the user`s profile picture')
    status = models.CharField(max_length=50, blank=True, null=True, db_comment='Account status (e.g., active, inactive, banned)')
    is_premium = models.BooleanField(blank=True, null=True, db_comment='Indicates if the user is a premium member')
    is_admin = models.BooleanField(blank=True, null=True, db_comment='Indicates if the user is a admin member')
    language_preference = models.CharField(max_length=10, blank=True, null=True, db_comment='Preferred language for chatbot interactions')
    last_seen = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of the user`s last activity')
    # created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of account creation')
    # updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of last update')
    chatbot_persona = models.JSONField(blank=True, null=True, db_comment='Configuration for chatbot preferences (e.g., tone, style)')
    metadata = models.JSONField(blank=True, null=True, db_comment='Additional metadata for user (e.g., app-specific settings)')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_user_mst'
        db_table_comment = 'Table to store user information for Conai Tarot Service'