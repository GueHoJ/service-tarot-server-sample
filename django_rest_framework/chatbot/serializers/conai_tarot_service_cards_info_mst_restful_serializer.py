import uuid

from rest_framework import serializers
from ..domain.CONAI_TAROT_SERVICE_CARDS_INFO_MST import ConaiTarotServiceCardsInfoMst, ConaiTarotServiceCardsInfoMstMod


class ConaiTarotServiceCardsInfoMstGetSerializer(serializers.Serializer):
    conaiTarotServiceCardsInfoMstId = serializers.UUIDField(
        source='conai_tarot_service_cards_info_mst_id', required=False,
        help_text='Primary key and unique identifier for each tarot card'
    )
    name = serializers.CharField(
        required=False, help_text='English name of the tarot card'
    )
    koreanName = serializers.CharField(
        source='korean_name', allow_null=True, required=False,
        help_text='Korean name of the tarot card'
    )
    cardIndex = serializers.IntegerField(
        source='card_index', required=False, help_text='Index of the tarot card within the deck'
    )
    imageUrl = serializers.CharField(
        source='image_url', allow_null=True, required=False, help_text='Path to the tarot card image'
    )
    # image = serializers.ImageField(
    #     required=False, allow_null=True, help_text='Full path for image'
    # )
    referenceUrls = serializers.JSONField(
        source='reference_urls', allow_null=True, required=False,
        help_text='JSONB field for storing additional reference URLs related to the tarot card'
    )
    deckName = serializers.CharField(
        source='deck_name', required=False, help_text='Name of the deck the tarot card belongs to'
    )
    type = serializers.CharField(
        required=False, help_text='Type identifier for the front or back'
    )
    version = serializers.CharField(
        required=False, help_text='Version identifier for the deck or card'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', allow_null=True, required=False, help_text='Timestamp of record creation'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False, help_text='Timestamp of last record update'
    )

class ConaiTarotServiceCardsInfoMstPostSerializer(serializers.ModelSerializer):
    conaiTarotServiceCardsInfoMstId = serializers.UUIDField(
        source='conai_tarot_service_cards_info_mst_id',
        default=uuid.uuid4,
        required=False,
        help_text='Primary key and unique identifier for each tarot card'
    )
    name = serializers.CharField(
        required=True, help_text='English name of the tarot card'
    )
    koreanName = serializers.CharField(
        source='korean_name', allow_null=True, required=False,
        help_text='Korean name of the tarot card'
    )
    cardIndex = serializers.IntegerField(
        source='card_index', required=True, help_text='Index of the tarot card within the deck'
    )
    imageUrl = serializers.CharField(
        source='image_url', allow_null=True, required=False, help_text='Path to the tarot card image'
    )
    image = serializers.ImageField(
        required=False, allow_null=True, help_text='Full path for image'
    )
    referenceUrls = serializers.JSONField(
        source='reference_urls', allow_null=True, required=False,
        help_text='JSONB field for storing additional reference URLs related to the tarot card'
    )
    deckName = serializers.CharField(
        source='deck_name', required=True, help_text='Name of the deck the tarot card belongs to'
    )
    type = serializers.CharField(
        required=False, help_text='Type identifier for the front or back'
    )
    version = serializers.CharField(
        required=True, help_text='Version identifier for the deck or card'
    )
    # createdAt = serializers.DateTimeField(
    #     source='created_at', allow_null=True, required=False, help_text='Timestamp of record creation'
    # )
    # updatedAt = serializers.DateTimeField(
    #     source='updated_at', allow_null=True, required=False, help_text='Timestamp of last record update'
    # )

    class Meta:
        model = ConaiTarotServiceCardsInfoMstMod
        fields = [
            'conaiTarotServiceCardsInfoMstId',
            'name',
            'koreanName',
            'cardIndex',
            'imageUrl',
            'image',
            'referenceUrls',
            'deckName',
            'type',
            'version',
            # 'createdAt',
            # 'updatedAt'
        ]

class ConaiTarotServiceCardsInfoMstPutSerializer(serializers.ModelSerializer):
    conaiTarotServiceCardsInfoMstId = serializers.UUIDField(
        source='conai_tarot_service_cards_info_mst_id', required=False,
        help_text='Primary key and unique identifier for each tarot card'
    )
    name = serializers.CharField(
        required=False, help_text='English name of the tarot card'
    )
    koreanName = serializers.CharField(
        source='korean_name', allow_null=True, required=False,
        help_text='Korean name of the tarot card'
    )
    cardIndex = serializers.IntegerField(
        source='card_index', required=False, help_text='Index of the tarot card within the deck'
    )
    imageUrl = serializers.CharField(
        source='image_url', allow_null=True, required=False, help_text='Path to the tarot card image'
    )
    image = serializers.ImageField(
        required=False, allow_null=True, help_text='Full path for image'
    )
    referenceUrls = serializers.JSONField(
        source='reference_urls', allow_null=True, required=False,
        help_text='JSONB field for storing additional reference URLs related to the tarot card'
    )
    deckName = serializers.CharField(
        source='deck_name', required=False, help_text='Name of the deck the tarot card belongs to'
    )
    type = serializers.CharField(
        required=False, help_text='Type identifier for the front or back'
    )
    version = serializers.CharField(
        required=False, help_text='Version identifier for the deck or card'
    )
    createdAt = serializers.DateTimeField(
        source='created_at', allow_null=True, required=False, help_text='Timestamp of record creation'
    )
    updatedAt = serializers.DateTimeField(
        source='updated_at', allow_null=True, required=False, help_text='Timestamp of last record update'
    )

    class Meta:
        model = ConaiTarotServiceCardsInfoMst
        fields = [
            'conaiTarotServiceCardsInfoMstId', 'name', 'koreanName', 'cardIndex', 'imageUrl', 'image',
            'referenceUrls', 'deckName', 'type', 'version', 'createdAt', 'updatedAt'
        ]

class ConaiTarotServiceCardsInfoMstDeleteSerializer(serializers.ModelSerializer):
    conaiTarotServiceCardsInfoMstId = serializers.UUIDField(
        source='conai_tarot_service_cards_info_mst_id', required=True,
        help_text='Primary key and unique identifier for each tarot card'
    )

    class Meta:
        model = ConaiTarotServiceCardsInfoMst
        fields = ['conaiTarotServiceCardsInfoMstId']
