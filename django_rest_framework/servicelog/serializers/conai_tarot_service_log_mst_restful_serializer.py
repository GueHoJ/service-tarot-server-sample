import uuid

from rest_framework import serializers
from ..domain.CONAI_TAROT_SERVICE_LOG_MST import ConaiTarotServiceLogMst, ConaiTarotServiceLogMstMod


# Get Serializer
class ConaiTarotServiceLogMstGetSerializer(serializers.Serializer):
    conaiTarotServiceLogMstId = serializers.UUIDField(
        source='conai_tarot_service_log_mst_id', required=False,
        help_text='Primary key and unique identifier for each log entry'
    )
    userId = serializers.CharField(
        source='user_id', allow_null=True, required=False,
        help_text='User identifier (nullable if no user is logged in)'
    )
    eventType = serializers.CharField(
        source='event_type', required=False,
        help_text='Type of the event (e.g., "login", "button_click", "session_start")'
    )
    eventDetails = serializers.JSONField(
        source='event_details', allow_null=True, required=False,
        help_text='Additional details about the event in JSONB format'
    )
    eventTimestamp = serializers.DateTimeField(
        source='event_timestamp', allow_null=True, required=False,
        help_text='Timestamp when the event occurred'
    )
    durationSeconds = serializers.IntegerField(
        source='duration_seconds', allow_null=True, required=False,
        help_text='Duration of the event in seconds (optional)'
    )
    ipAddress = serializers.CharField(
        source='ip_address', allow_null=True, required=False,
        help_text='IP address of the user (optional)'
    )
    deviceInfo = serializers.JSONField(
        source='device_info', allow_null=True, required=False,
        help_text='Device-related information (e.g., OS, browser, app version)'
    )
    metadata = serializers.JSONField(
        allow_null=True, required=False,
        help_text='Additional metadata for the log entry'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', allow_null=True, required=False,
        help_text='Timestamp of log creation'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False,
        help_text='Timestamp of last update'
    )


# Post Serializer
class ConaiTarotServiceLogMstPostSerializer(serializers.ModelSerializer):
    conaiTarotServiceLogMstId = serializers.UUIDField(
        source='conai_tarot_service_log_mst_id', required=False, default=uuid.uuid4,
        help_text='Primary key and unique identifier for each log entry'
    )
    userId = serializers.CharField(
        source='user_id', allow_null=True, required=False,
        help_text='User identifier (nullable if no user is logged in)'
    )
    eventType = serializers.CharField(
        source='event_type', required=False,
        help_text='Type of the event (e.g., "login", "button_click", "session_start")'
    )
    eventDetails = serializers.JSONField(
        source='event_details', allow_null=True, required=False,
        help_text='Additional details about the event in JSONB format'
    )
    eventTimestamp = serializers.DateTimeField(
        source='event_timestamp', allow_null=True, required=False,
        help_text='Timestamp when the event occurred'
    )
    durationSeconds = serializers.IntegerField(
        source='duration_seconds', allow_null=True, required=False,
        help_text='Duration of the event in seconds (optional)'
    )
    ipAddress = serializers.CharField(
        source='ip_address', allow_null=True, required=False,
        help_text='IP address of the user (optional)'
    )
    deviceInfo = serializers.JSONField(
        source='device_info', allow_null=True, required=False,
        help_text='Device-related information (e.g., OS, browser, app version)'
    )
    metadata = serializers.JSONField(
        allow_null=True, required=False,
        help_text='Additional metadata for the log entry'
    )
    class Meta:
        model = ConaiTarotServiceLogMstMod
        fields = [
            'conaiTarotServiceLogMstId', 'userId', 'eventType', 'eventDetails',
            'eventTimestamp', 'durationSeconds', 'ipAddress', 'deviceInfo', 'metadata',
            # 'createdAt', 'updatedAt'
        ]


# Put Serializer
class ConaiTarotServiceLogMstPutSerializer(serializers.ModelSerializer):
    conaiTarotServiceLogMstId = serializers.UUIDField(
        source='conai_tarot_service_log_mst_id', required=False,
        help_text='Primary key and unique identifier for each log entry'
    )
    userId = serializers.CharField(
        source='user_id', allow_null=True, required=False,
        help_text='User identifier (nullable if no user is logged in)'
    )
    eventType = serializers.CharField(
        source='event_type', required=False,
        help_text='Type of the event (e.g., "login", "button_click", "session_start")'
    )
    eventDetails = serializers.JSONField(
        source='event_details', allow_null=True, required=False,
        help_text='Additional details about the event in JSONB format'
    )
    eventTimestamp = serializers.DateTimeField(
        source='event_timestamp', allow_null=True, required=False,
        help_text='Timestamp when the event occurred'
    )
    durationSeconds = serializers.IntegerField(
        source='duration_seconds', allow_null=True, required=False,
        help_text='Duration of the event in seconds (optional)'
    )
    ipAddress = serializers.CharField(
        source='ip_address', allow_null=True, required=False,
        help_text='IP address of the user (optional)'
    )
    deviceInfo = serializers.JSONField(
        source='device_info', allow_null=True, required=False,
        help_text='Device-related information (e.g., OS, browser, app version)'
    )
    metadata = serializers.JSONField(
        allow_null=True, required=False,
        help_text='Additional metadata for the log entry'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', allow_null=True, required=False,
        help_text='Timestamp of log creation'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False,
        help_text='Timestamp of last update'
    )
    class Meta:
        model = ConaiTarotServiceLogMst
        fields = [
            'conaiTarotServiceLogMstId', 'userId', 'eventType', 'eventDetails',
            'eventTimestamp', 'durationSeconds', 'ipAddress', 'deviceInfo', 'metadata',
            'createdAt', 'updatedAt'
        ]


# Delete Serializer
class ConaiTarotServiceLogMstDeleteSerializer(serializers.ModelSerializer):
    conaiTarotServiceLogMstId = serializers.UUIDField(
        source='conai_tarot_service_log_mst_id', required=True,
        help_text='Primary key and unique identifier for each log entry'
    )

    class Meta:
        model = ConaiTarotServiceLogMst
        fields = ['conaiTarotServiceLogMstId']
