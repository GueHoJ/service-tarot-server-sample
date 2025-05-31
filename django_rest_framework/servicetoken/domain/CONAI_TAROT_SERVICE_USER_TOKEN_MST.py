# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConaiTarotServiceUserTokenMst(models.Model):
    conai_tarot_service_user_token_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each token record')
    user_id = models.CharField(unique=True, max_length=150, db_comment='Unique identifier for the user associated with this token')
    access_token = models.TextField(db_comment='Current access token for user authentication')
    refresh_token = models.TextField(db_comment='Refresh token associated with the access token')
    is_active = models.BooleanField(blank=True, null=True, db_comment='Indicates whether the token is currently active or has been invalidated')
    expires_at = models.DateTimeField(db_comment='Expiration timestamp of the access token')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp when the token was created')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp when the token was last updated')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_user_token_mst'
        unique_together = (('user_id', 'access_token'),)
        db_table_comment = 'Table to manage JWT tokens for user API interaction in Conai Tarot Service'


class ConaiTarotServiceUserTokenMstMod(models.Model):
    conai_tarot_service_user_token_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each token record')
    user_id = models.CharField(unique=True, max_length=150, db_comment='Unique identifier for the user associated with this token')
    access_token = models.TextField(db_comment='Current access token for user authentication')
    refresh_token = models.TextField(db_comment='Refresh token associated with the access token')
    is_active = models.BooleanField(blank=True, null=True, db_comment='Indicates whether the token is currently active or has been invalidated')
    expires_at = models.DateTimeField(db_comment='Expiration timestamp of the access token')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_user_token_mst'
        unique_together = (('user_id', 'access_token'),)
        db_table_comment = 'Table to manage JWT tokens for user API interaction in Conai Tarot Service'