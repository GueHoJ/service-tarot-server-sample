import uuid
from rest_framework import serializers

from ..domain.CONAI_TAROT_SERVICE_USER_TOKEN_MST import ConaiTarotServiceUserTokenMst, ConaiTarotServiceUserTokenMstMod


class ConaiTarotServiceUserTokenMstGetSerializer(serializers.Serializer):
    conaiTarotServiceUserTokenMstId = serializers.UUIDField(
        source='conai_tarot_service_user_token_mst_id', required=False,
        help_text='Primary key and unique identifier for each token record'
    )
    userId = serializers.CharField(
        source='user_id', required=False,
        help_text='Unique identifier for the user associated with this token'
    )
    accessToken = serializers.CharField(
        source='access_token', required=False,
        help_text='Current access token for user authentication'
    )
    refreshToken = serializers.CharField(
        source='refresh_token', required=False,
        help_text='Refresh token associated with the access token'
    )
    isActive = serializers.BooleanField(
        source='is_active', allow_null=True, required=False,
        help_text='Indicates whether the token is currently active or has been invalidated'
    )
    expiresAt = serializers.DateTimeField(
        source='expires_at', required=False,
        help_text='Expiration timestamp of the access token'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', allow_null=True, required=False,
        help_text='Timestamp when the token was created'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False,
        help_text='Timestamp when the token was last updated'
    )



class ConaiTarotServiceUserTokenMstPostSerializer(serializers.ModelSerializer):
    conaiTarotServiceUserTokenMstId = serializers.UUIDField(
        source='conai_tarot_service_user_token_mst_id', default=uuid.uuid4, required=False,
        help_text='Primary key and unique identifier for each token record'
    )
    userId = serializers.CharField(
        source='user_id', required=True,
        help_text='Unique identifier for the user associated with this token'
    )
    accessToken = serializers.CharField(
        source='access_token', required=True,
        help_text='Current access token for user authentication'
    )
    refreshToken = serializers.CharField(
        source='refresh_token', required=True,
        help_text='Refresh token associated with the access token'
    )
    isActive = serializers.BooleanField(
        source='is_active', allow_null=True, required=False,
        help_text='Indicates whether the token is currently active or has been invalidated'
    )
    expiresAt = serializers.DateTimeField(
        source='expires_at', required=True,
        help_text='Expiration timestamp of the access token'
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at', allow_null=True, required=False,
    #     help_text='Timestamp when the token was created'
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at', allow_null=True, required=False,
    #     help_text='Timestamp when the token was last updated'
    # )

    class Meta:
        model = ConaiTarotServiceUserTokenMstMod
        fields = [
            'conaiTarotServiceUserTokenMstId', 'userId', 'accessToken', 'refreshToken', 'isActive',
            'expiresAt',
            # 'createdAt', 'updatedAt'
        ]


class ConaiTarotServiceUserTokenMstPutSerializer(serializers.ModelSerializer):
    conaiTarotServiceUserTokenMstId = serializers.UUIDField(
        source='conai_tarot_service_user_token_mst_id', required=False,
        help_text='Primary key and unique identifier for each token record'
    )
    userId = serializers.CharField(
        source='user_id', required=True,
        help_text='Unique identifier for the user associated with this token'
    )
    accessToken = serializers.CharField(
        source='access_token', required=True,
        help_text='Current access token for user authentication'
    )
    refreshToken = serializers.CharField(
        source='refresh_token', required=True,
        help_text='Refresh token associated with the access token'
    )
    isActive = serializers.BooleanField(
        source='is_active', allow_null=True, required=False,
        help_text='Indicates whether the token is currently active or has been invalidated'
    )
    expiresAt = serializers.DateTimeField(
        source='expires_at', required=True,
        help_text='Expiration timestamp of the access token'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False,
        help_text='Timestamp when the token was last updated'
    )

    class Meta:
        model = ConaiTarotServiceUserTokenMst
        fields = [
            'conaiTarotServiceUserTokenMstId', 'userId', 'accessToken', 'refreshToken', 'isActive',
            'expiresAt', 'updatedAt'
        ]


class ConaiTarotServiceUserTokenMstDeleteSerializer(serializers.ModelSerializer):
    conaiTarotServiceUserTokenMstId = serializers.UUIDField(
        source='conai_tarot_service_user_token_mst_id', required=True,
        help_text='Primary key and unique identifier for each token record'
    )

    class Meta:
        model = ConaiTarotServiceUserTokenMst
        fields = ['conaiTarotServiceUserTokenMstId']
