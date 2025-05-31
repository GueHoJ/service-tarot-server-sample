import uuid
from rest_framework import serializers
from ..domain.CONAI_USER_MST import ConaiUserMst, ConaiUserMstMod


class ConaiUserMstGetSerializer(serializers.Serializer):
    # 아래 형태로 ORM MODEL을 serailizers.TypeField로 Convert
    # source='original_field'(snake_case로 연결 시켜줘야 함)
    # GET Serializer 는 모든 field 데이터 리턴
    conaiUserMstId = serializers.UUIDField(source='conai_user_mst_id', required=False, help_text='코나이유저마스터 고유 아이디')
    userId = serializers.CharField(source='user_id', required=False, help_text='사용자 아이디')
    userName = serializers.CharField(source='user_name', required=False, help_text='사용자 이름')
    userPhoneNumber = serializers.IntegerField(source='user_phone_number', required=False,
                                               help_text='사용자 전화번호')

    def validate_orderBy(self, value):
        # Optionally, you can perform validation on the orderBy field here
        # For example, ensure that the field name is valid
        # You can raise a validation error if the field name is not valid
        # Example:
        # valid_field_names = ['eventUserPntId', 'cpId', 'userId', 'shopId', 'eventPnt', 'userEventPntNo', 'eventPntTpCd',
        #                      'eventCaseNm', 'eventCaseTpCd', 'eventId', 'regDtm', 'regId', 'updDtm', 'updId']
        # if value not in valid_field_names:
        #     raise serializers.ValidationError('Invalid field name for ordering.')
        return value


# ORM OBJ_ID null 값으로 날아가지 않게 하기위해서,
# models.UUIDField 를 models.BigAutoField 로 변경해줘야 함
class ConaiUserMstPostSerializer(serializers.ModelSerializer):
    # 아래 형태로 ORM MODEL을 CamelCaseField로 Convert
    # source='original_field'(snake_case로 연결 시켜줘야 함)
    conaiUserMstId = serializers.UUIDField(source='conai_user_mst_id', allow_null=True, help_text='코나이유저마스터 고유 아이디', default=uuid.uuid4)
    userId = serializers.CharField(source='user_id', required=False, help_text='사용자 아이디')
    userName = serializers.CharField(source='user_name', required=False, help_text='사용자 이름')
    userPhoneNumber = serializers.IntegerField(source='user_phone_number', required=False,
                                               help_text='사용자 전화번호')

    class Meta:
        model = ConaiUserMstMod
        fields = ['conaiUserMstId','userId','userName','userPhoneNumber',]
        # fields = '__all__'


class ConaiUserMstPutSerializer(serializers.ModelSerializer):
    # 아래 형태로 ORM MODEL을 CamelCaseField로 Convert
    # source='original_field'(snake_case로 연결 시켜줘야 함)
    # PUT Serializer 는 OBJ_ID, REG_DTM, UPD_DTM 제외 field 데이터 리턴
    conaiUserMstId = serializers.UUIDField(source='conai_user_mst_id', required=True, help_text='코나이유저마스터 고유 아이디')
    userId = serializers.CharField(source='user_id', required=False, help_text='사용자 아이디')
    userName = serializers.CharField(source='user_name', required=False, help_text='사용자 이름')
    userPhoneNumber = serializers.IntegerField(source='user_phone_number', required=False,
                                               help_text='사용자 전화번호')

    class Meta:
        model = ConaiUserMst
        fields = ['conaiUserMstId', 'userId', 'userName', 'userPhoneNumber', ]
        # fields = '__all__'


class ConaiUserMstDeleteSerializer(serializers.ModelSerializer):
    # 아래 형태로 ORM MODEL을 CamelCaseField로 Convert
    # source='original_field'(snake_case로 연결 시켜줘야 함)
    # DELETE Serializer 는 CP_ID, USER_ID, USER_OBJ_NO field 데이터 리턴
    conaiUserMstId = serializers.UUIDField(source='conai_user_mst_id', required=True, help_text='코나이유저마스터 고유 아이디')
    userId = serializers.CharField(source='user_id', required=False, help_text='사용자 아이디')
    userName = serializers.CharField(source='user_name', required=False, help_text='사용자 이름')
    userPhoneNumber = serializers.IntegerField(source='user_phone_number', required=False,
                                               help_text='사용자 전화번호')

    class Meta:
        model = ConaiUserMst
        fields = ['conaiUserMstId', 'userId', 'userName', 'userPhoneNumber', ]
        # fields = '__all__'
