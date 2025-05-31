import uuid
from rest_framework import serializers
from user.domain.CONAI_TAROT_SERVICE_USER_MST import ConaiTarotServiceUserMst, ConaiTarotServiceUserMstMod


class ConaiTarotServiceUserMstGetSerializer(serializers.Serializer):
    conaiTarotServiceUserMstId = serializers.UUIDField(
        source='conai_tarot_service_user_mst_id',
        required=False,
        help_text='Primary key and unique identifier for each user',
    )
    userId = serializers.CharField(
        source='user_id',
        required=False,
        help_text='User`s unique id',
    )
    username = serializers.CharField(
        required=False,
        help_text='User`s unique username',
    )
    nickname = serializers.CharField(
        required=False,
        help_text='User`s unique nickname',
    )
    age = serializers.IntegerField(
        required=False,
        help_text='User`s age',
    )
    gender = serializers.CharField(
        required=False,
        help_text='User`s gender',
    )
    job = serializers.CharField(
        required=False,
        help_text='User`s job',
    )
    email = serializers.CharField(
        required=False,
        help_text='User`s email address',
    )
    phoneNumber = serializers.CharField(
        source='phone_number',
        allow_null=True,
        required=False,
        help_text='Optional phone number for user contact',
    )
    password = serializers.CharField(
        allow_null=True,
        required=False,
        help_text='User`s password (hashed)',
    )
    profilePictureUrl = serializers.CharField(
        source='profile_picture_url',
        allow_null=True,
        required=False,
        help_text='URL to the user`s profile picture',
    )
    status = serializers.CharField(
        allow_null=True,
        required=False,
        help_text='Account status (e.g., active, inactive, banned)',
    )
    isPremium = serializers.BooleanField(
        source='is_premium',
        allow_null=True,
        required=False,
        help_text='Indicates if the user is a premium member',
    )
    isAdmin = serializers.BooleanField(
        source='is_admin',
        allow_null=True,
        required=False,
        help_text='Indicates if the user is a admin member',
    )
    languagePreference = serializers.CharField(
        source='language_preference',
        allow_null=True,
        required=False,
        help_text='Preferred language for chatbot interactions',
    )
    lastSeen = serializers.DateTimeField(
        source='last_seen',
        allow_null=True,
        required=False,
        help_text='Timestamp of the user`s last activity',
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at',
    #     allow_null=True,
    #     required=False,
    #     help_text='Timestamp of account creation',
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at',
    #     allow_null=True,
    #     required=False,
    #     help_text='Timestamp of last update',
    # )
    chatbotPersona = serializers.JSONField(
        source='chatbot_persona',
        allow_null=True,
        required=False,
        help_text='Configuration for chatbot preferences (e.g., tone, style)',
    )
    metadata = serializers.JSONField(
        allow_null=True,
        required=False,
        help_text='Additional metadata for user (e.g., app-specific settings)',
    )


class ConaiTarotServiceUserMstPostSerializer(serializers.ModelSerializer):
    conaiTarotServiceUserMstId = serializers.UUIDField(
        source='conai_tarot_service_user_mst_id',
        default=uuid.uuid4,
        required=False,
        help_text='Primary key and unique identifier for each user',
    )
    userId = serializers.CharField(
        source='user_id',
        required=False,
        help_text='User`s unique id',
    )
    username = serializers.CharField(
        required=False,
        allow_null=True,
        help_text='User`s unique username',
    )
    nickname = serializers.CharField(
        required=False,
        help_text='User`s unique nickname',
    )
    age = serializers.IntegerField(
        required=False,
        help_text='User`s age',
    )
    gender = serializers.CharField(
        required=False,
        help_text='User`s gender',
    )
    job = serializers.CharField(
        required=False,
        help_text='User`s job',
    )
    email = serializers.CharField(
        required=False,
        allow_null=True,
        help_text='User`s email address',
    )
    phoneNumber = serializers.CharField(
        source='phone_number',
        allow_null=True,
        required=False,
        help_text='Optional phone number for user contact',
    )
    password = serializers.CharField(
        allow_null=True,
        required=False,
        help_text='User`s password (hashed)',
    )
    profilePictureUrl = serializers.CharField(
        source='profile_picture_url',
        allow_null=True,
        required=False,
        help_text='URL to the user`s profile picture',
    )
    status = serializers.CharField(
        allow_null=True,
        required=False,
        default='active',
        help_text='Account status (e.g., active, inactive, banned)',
    )
    isPremium = serializers.BooleanField(
        source='is_premium',
        allow_null=True,
        required=False,
        default=False,
        help_text='Indicates if the user is a premium member',
    )
    isAdmin = serializers.BooleanField(
        source='is_admin',
        allow_null=True,
        required=False,
        default=False,
        help_text='Indicates if the user is a admin member',
    )
    languagePreference = serializers.CharField(
        source='language_preference',
        allow_null=True,
        required=False,
        help_text='Preferred language for chatbot interactions',
    )
    lastSeen = serializers.DateTimeField(
        source='last_seen',
        allow_null=True,
        required=False,
        help_text='Timestamp of the user`s last activity',
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at',
    #     allow_null=True,
    #     required=False,
    #     help_text='Timestamp of account creation',
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at',
    #     allow_null=True,
    #     required=False,
    #     help_text='Timestamp of last update',
    # )
    chatbotPersona = serializers.JSONField(
        source='chatbot_persona',
        allow_null=True,
        required=False,
        help_text='Configuration for chatbot preferences (e.g., tone, style)',
    )
    metadata = serializers.JSONField(
        allow_null=True,
        required=False,
        help_text='Additional metadata for user (e.g., app-specific settings)',
    )

    class Meta:
        model = ConaiTarotServiceUserMstMod
        fields = [
            'conaiTarotServiceUserMstId',
            'userId',
            'username',
            'nickname',
            'age',
            'gender',
            'job',
            'email',
            'phoneNumber',
            'password',
            'profilePictureUrl',
            'status',
            'isPremium',
            'isAdmin',
            'languagePreference',
            'lastSeen',
            # 'createdAt',
            # 'updatedAt',
            'chatbotPersona',
            'metadata',
        ]


class ConaiTarotServiceUserMstPutSerializer(ConaiTarotServiceUserMstPostSerializer):
    conaiTarotServiceUserMstId = serializers.UUIDField(
        source='conai_tarot_service_user_mst_id',
        default=uuid.uuid4,
        required=False,
        help_text='Primary key and unique identifier for each user',
    )
    userId = serializers.CharField(
        source='user_id',
        required=False,
        help_text='User`s unique id',
    )
    username = serializers.CharField(
        required=False,
        allow_null=True,
        help_text='User`s unique username',
    )
    nickname = serializers.CharField(
        required=False,
        help_text='User`s unique nickname',
    )
    age = serializers.IntegerField(
        required=False,
        help_text='User`s age',
    )
    gender = serializers.CharField(
        required=False,
        help_text='User`s gender',
    )
    job = serializers.CharField(
        required=False,
        help_text='User`s job',
    )
    email = serializers.CharField(
        required=False,
        help_text='User`s email address',
    )
    phoneNumber = serializers.CharField(
        source='phone_number',
        allow_null=True,
        required=False,
        help_text='Optional phone number for user contact',
    )
    password = serializers.CharField(
        allow_null=True,
        required=False,
        help_text='User`s password (hashed)',
    )
    profilePictureUrl = serializers.CharField(
        source='profile_picture_url',
        allow_null=True,
        required=False,
        help_text='URL to the user`s profile picture',
    )
    status = serializers.CharField(
        allow_null=True,
        required=False,
        default='active',
        help_text='Account status (e.g., active, inactive, banned)',
    )
    isPremium = serializers.BooleanField(
        source='is_premium',
        allow_null=True,
        required=False,
        help_text='Indicates if the user is a premium member',
    )
    isAdmin = serializers.BooleanField(
        source='is_admin',
        allow_null=True,
        required=False,
        help_text='Indicates if the user is a admin member',
    )
    languagePreference = serializers.CharField(
        source='language_preference',
        allow_null=True,
        required=False,
        help_text='Preferred language for chatbot interactions',
    )
    lastSeen = serializers.DateTimeField(
        source='last_seen',
        allow_null=True,
        required=False,
        help_text='Timestamp of the user`s last activity',
    )
    createdAt = serializers.DateTimeField(
        source='created_at',
        allow_null=True,
        required=False,
        help_text='Timestamp of account creation',
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at',
        allow_null=True,
        required=False,
        help_text='Timestamp of last update',
    )
    chatbotPersona = serializers.JSONField(
        source='chatbot_persona',
        allow_null=True,
        required=False,
        help_text='Configuration for chatbot preferences (e.g., tone, style)',
    )
    metadata = serializers.JSONField(
        allow_null=True,
        required=False,
        help_text='Additional metadata for user (e.g., app-specific settings)',
    )

    class Meta:
        model = ConaiTarotServiceUserMst
        fields = [
            'conaiTarotServiceUserMstId',
            'userId',
            'username',
            'nickname',
            'age',
            'gender',
            'job',
            'email',
            'phoneNumber',
            'password',
            'profilePictureUrl',
            'status',
            'isPremium',
            'isAdmin',
            'languagePreference',
            'lastSeen',
            'createdAt',
            'updatedAt',
            'chatbotPersona',
            'metadata',
        ]


class ConaiTarotServiceUserMstDeleteSerializer(serializers.ModelSerializer):
    conaiTarotServiceUserMstId = serializers.UUIDField(
        source='conai_tarot_service_user_mst_id',
        required=True,
        help_text='Primary key and unique identifier for each user',
    )

    class Meta:
        model = ConaiTarotServiceUserMst
        fields = ['conaiTarotServiceUserMstId']
