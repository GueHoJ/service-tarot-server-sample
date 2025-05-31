# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConaiTarotServiceLogMst(models.Model):
    conai_tarot_service_log_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each log entry')
    user_id = models.CharField(max_length=255, blank=True, null=True, db_comment='User identifier (nullable if no user is logged in)')
    event_type = models.TextField(blank=True, null=True, db_comment='Type of the event (e.g., "login", "button_click", "session_start")')
    event_details = models.JSONField(blank=True, null=True, db_comment='Additional details about the event in JSONB format')
    event_timestamp = models.DateTimeField(blank=True, null=True, db_comment='Timestamp when the event occurred')
    duration_seconds = models.IntegerField(blank=True, null=True, db_comment='Duration of the event in seconds (optional)')
    ip_address = models.CharField(max_length=50, blank=True, null=True, db_comment='IP address of the user (optional)')
    device_info = models.JSONField(blank=True, null=True, db_comment='Device-related information (e.g., OS, browser, app version)')
    metadata = models.JSONField(blank=True, null=True, db_comment='Additional metadata for the log entry')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of log creation')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of last update')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_log_mst'
        db_table_comment = 'Table to log user activities and events for Conai Tarot Service'


class ConaiTarotServiceLogMstMod(models.Model):
    conai_tarot_service_log_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each log entry')
    user_id = models.CharField(max_length=255, blank=True, null=True, db_comment='User identifier (nullable if no user is logged in)')
    event_type = models.TextField(blank=True, null=True, db_comment='Type of the event (e.g., "login", "button_click", "session_start")')
    event_details = models.JSONField(blank=True, null=True, db_comment='Additional details about the event in JSONB format')
    event_timestamp = models.DateTimeField(blank=True, null=True, db_comment='Timestamp when the event occurred')
    duration_seconds = models.IntegerField(blank=True, null=True, db_comment='Duration of the event in seconds (optional)')
    ip_address = models.CharField(max_length=50, blank=True, null=True, db_comment='IP address of the user (optional)')
    device_info = models.JSONField(blank=True, null=True, db_comment='Device-related information (e.g., OS, browser, app version)')
    metadata = models.JSONField(blank=True, null=True, db_comment='Additional metadata for the log entry')
    # created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of log creation')
    # updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of last update')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_log_mst'
        db_table_comment = 'Table to log user activities and events for Conai Tarot Service'