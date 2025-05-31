import uuid
from rest_framework import serializers

from app.custom_fields import OrderByField, CustomDateField


# from ..domain.CHAINTEST_SERIALIZERS import ChaintestSerializers, ChaintestSerializersMod


class ChainTestSerializersGetSerializer(serializers.Serializer):
    # 아래 형태로 ORM MODEL을 serailizers.TypeField로 Convert
    # source='original_field'(snake_case로 연결 시켜줘야 함)
    # GET Serializer 는 모든 field 데이터 리턴
    # brdId = serializers.UUIDField(source='brd_id', required=False, read_only=True, help_text='게시판아이디')
    # brdNm = serializers.CharField(source='brd_nm', required=False, help_text='게시판명')
    # cpId = serializers.CharField(source='cp_id', required=True, help_text='기업아이디')
    # shopId = serializers.CharField(source='shop_id', required=False, help_text='매장아이디')
    # authVal = serializers.JSONField(source='auth_val', required=False, help_text='권한')
    # isWidget = serializers.BooleanField(source='is_widget', required=False, help_text='위젯')
    # sortSeq = serializers.IntegerField(source='sort_seq', required=False, help_text='정렬순번')
    # useYn = serializers.CharField(source='use_yn', required=False, help_text='사용여부')
    # delReqYn = serializers.CharField(source='del_req_yn', required=False, help_text='삭제요청여부')
    # regDtm = serializers.DateTimeField(source='reg_dtm', required=False, help_text='작성일시')
    # regId = serializers.CharField(source='reg_id', required=False, help_text='작성자 아이디')
    # updDtm = serializers.DateTimeField(source='upd_dtm', required=False, help_text='수정일시')
    # updId = serializers.CharField(source='upd_id', required=False, help_text='수정자 아이디')
    promptText = serializers.CharField(required=False, help_text='프롬프트텍스트',
                                       default='Describe the content and purpose of LangChain.')
    modelPath = serializers.CharField(required=False, help_text='모델경로',
                                      default='/models/checkpoints/Llama3.2-11B-Vision-Instruct')
    testVal = serializers.CharField(required=False, help_text='테스트값')

    # New date range fields
    rangeQueryField = serializers.CharField(required=False,
                                            help_text='범위조회기준필드 Range query field name\nUse Snake case for field name\nExample: log_dtm')
    startDate = CustomDateField(required=False, help_text='조회시작일자 Start date in yyyyMMdd format')
    endDate = CustomDateField(required=False, help_text='조회종료일자 End date in yyyyMMdd format')
    # New orderBy field
    orderBy = OrderByField(required=False,
                           help_text='Field name and sort order for ordering,\nfield_name_asc or field_name_desc\nExample: regDtm_asc')

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
class ChainTestSerializersPostSerializer(serializers.Serializer):
    # 아래 형태로 ORM MODEL을 CamelCaseField로 Convert
    # source='original_field'(snake_case로 연결 시켜줘야 함)
    # POST Serializer 는 OBJ_ID, USER_OBJ_NO, REG_DTM, UPD_DTM 제외 field 데이터 리턴
    # brdId = serializers.UUIDField(source='brd_id', required=False, read_only=True, help_text='게시판아이디')
    # brdNm = serializers.CharField(source='brd_nm', required=False, help_text='게시판명')
    # cpId = serializers.CharField(source='cp_id', required=True, help_text='기업아이디')
    # shopId = serializers.CharField(source='shop_id', required=False, help_text='매장아이디')
    # authVal = serializers.JSONField(source='auth_val', required=False, help_text='권한')
    # isWidget = serializers.BooleanField(source='is_widget', required=False, help_text='위젯')
    # sortSeq = serializers.IntegerField(source='sort_seq', required=False, help_text='정렬순번')
    # useYn = serializers.CharField(source='use_yn', required=False, help_text='사용여부')
    # delReqYn = serializers.CharField(source='del_req_yn', required=False, help_text='삭제요청여부')
    # regDtm = serializers.DateTimeField(source='reg_dtm', required=False, help_text='작성일시')
    # regId = serializers.CharField(source='reg_id', required=False, help_text='작성자 아이디')
    # updDtm = serializers.DateTimeField(source='upd_dtm', required=False, help_text='수정일시')
    # updId = serializers.CharField(source='upd_id', required=False, help_text='수정자 아이디')
    promptText = serializers.JSONField(required=False, help_text='프롬프트텍스트 JSON',
                                       default={
                                           "question": "What is the purpose of LangChain?",
                                           "context": "LangChain is a language model that can generate text based on a prompt."
                                       })
    modelPath = serializers.CharField(required=False, help_text='모델경로',
                                      default='/models/checkpoints/Llama3.1-8B')
    task = serializers.CharField(required=False, help_text='수행 태스크 타입', default="text-generation")
    testVal = serializers.CharField(required=False, help_text='테스트값')

    # class Meta:
    # model = ChaintestSerializersMod
    # swagger 에 표시되길 원하는 필드명을 fields 리스트에 추가
    # fields = ['conaiUserMstId','userId','userName','userPhoneNumber',]

# class ChaintestSerializersPutSerializer(serializers.ModelSerializer):
# 아래 형태로 ORM MODEL을 CamelCaseField로 Convert
# source='original_field'(snake_case로 연결 시켜줘야 함)
# PUT Serializer 는 OBJ_ID, REG_DTM, UPD_DTM 제외 field 데이터 리턴
# brdId = serializers.UUIDField(source='brd_id', required=False, read_only=True, help_text='게시판아이디')
# brdNm = serializers.CharField(source='brd_nm', required=False, help_text='게시판명')
# cpId = serializers.CharField(source='cp_id', required=True, help_text='기업아이디')
# shopId = serializers.CharField(source='shop_id', required=False, help_text='매장아이디')
# authVal = serializers.JSONField(source='auth_val', required=False, help_text='권한')
# isWidget = serializers.BooleanField(source='is_widget', required=False, help_text='위젯')
# sortSeq = serializers.IntegerField(source='sort_seq', required=False, help_text='정렬순번')
# useYn = serializers.CharField(source='use_yn', required=False, help_text='사용여부')
# delReqYn = serializers.CharField(source='del_req_yn', required=False, help_text='삭제요청여부')
# regDtm = serializers.DateTimeField(source='reg_dtm', required=False, help_text='작성일시')
# regId = serializers.CharField(source='reg_id', required=False, help_text='작성자 아이디')
# updDtm = serializers.DateTimeField(source='upd_dtm', required=False, help_text='수정일시')
# updId = serializers.CharField(source='upd_id', required=False, help_text='수정자 아이디')

# class Meta:
# model = ChaintestSerializers
# swagger 에 표시되길 원하는 필드명을 fields 리스트에 추가
# fields = ['conaiUserMstId','userId','userName','userPhoneNumber',]


# class ChaintestSerializersDeleteSerializer(serializers.ModelSerializer):
# 아래 형태로 ORM MODEL을 CamelCaseField로 Convert
# source='original_field'(snake_case로 연결 시켜줘야 함)
# DELETE Serializer 는 CP_ID, USER_ID, USER_OBJ_NO field 데이터 리턴
# brdId = serializers.UUIDField(source='brd_id', required=False, read_only=True, help_text='게시판아이디')
# brdNm = serializers.CharField(source='brd_nm', required=False, help_text='게시판명')
# cpId = serializers.CharField(source='cp_id', required=True, help_text='기업아이디')
# shopId = serializers.CharField(source='shop_id', required=False, help_text='매장아이디')
# authVal = serializers.JSONField(source='auth_val', required=False, help_text='권한')
# isWidget = serializers.BooleanField(source='is_widget', required=False, help_text='위젯')
# sortSeq = serializers.IntegerField(source='sort_seq', required=False, help_text='정렬순번')
# useYn = serializers.CharField(source='use_yn', required=False, help_text='사용여부')
# delReqYn = serializers.CharField(source='del_req_yn', required=False, help_text='삭제요청여부')
# regDtm = serializers.DateTimeField(source='reg_dtm', required=False, help_text='작성일시')
# regId = serializers.CharField(source='reg_id', required=False, help_text='작성자 아이디')
# updDtm = serializers.DateTimeField(source='upd_dtm', required=False, help_text='수정일시')
# updId = serializers.CharField(source='upd_id', required=False, help_text='수정자 아이디')

# class Meta:
#     model = ChaintestSerializers
# swagger 에 표시되길 원하는 필드명을 fields 리스트에 추가
# fields = ['conaiUserMstId','userId','userName','userPhoneNumber',]
