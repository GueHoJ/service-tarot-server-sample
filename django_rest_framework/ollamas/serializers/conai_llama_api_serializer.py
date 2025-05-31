import uuid
from rest_framework import serializers

from app.custom_fields import OrderByField, CustomDateField


class ConaiLlamaApiRequestSerializer(serializers.Serializer):
    # 아래 형태로 ORM MODEL을 serailizers.TypeField로 Convert
    # source='original_field'(snake_case로 연결 시켜줘야 함)
    # GET Serializer 는 모든 field 데이터 리턴
    model = serializers.CharField(required=False, help_text='모델명')
    prompt = serializers.CharField(required=False, help_text='프롬프트')

class ConaiLlamaApiResponseSerializer(serializers.Serializer):
    # 아래 형태로 ORM MODEL을 serailizers.TypeField로 Convert
    # source='original_field'(snake_case로 연결 시켜줘야 함)
    # GET Serializer 는 모든 field 데이터 리턴
    llamaResponses = serializers.UUIDField(required=False, help_text='커나이 유저 마스터 고유 아이디')