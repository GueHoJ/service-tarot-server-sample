from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import permissions, status
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
# from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from ...application.service.user_conai_user_mst_restful_service import UserConaiUserMstRestfulService
from ...domain.CONAI_USER_MST import ConaiUserMst
from ...serializers.conai_user_mst_restful_serializer import ConaiUserMstGetSerializer, ConaiUserMstPostSerializer, \
    ConaiUserMstPutSerializer, ConaiUserMstDeleteSerializer
import app.utils.common_utils as common_utils
from app.utils.decorator import check_token
from user.containers import registry


class UserConaiUserMstRestfulApiController(APIView):
    # authentication_classes = [OAuth2Authentication]
    # permission_classes = [IsAuthenticated]
    """
    # CLASS : UserConaiUserMstRestfulApiController
    # AUTHOR : conai
    # TIME : 2024. 8. 20. 오후 4:04
    # DESCRIPTION
        - UserConaiUserMstRestfulApiController
        - CONAI_USER_MST API
        - 디렉터리 : user
        - 서비스 설명 : CONAI_USER_MST RESTFUL API
        - 서비스 호출 url : /user/conaiUserMst
        - 서비스 호출 method : GET POST PUT DELETE
        - 서비스 호출 body : json
        - 서비스 호출 파라미터 :
            conaiUserMstId (코나이 유저 마스터 고유 아이디)
            userId (사용자 아이디)
            userName (사용자 이름)
            userPhoneNumber (사용자 전화번호)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 8. 20.          conai          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    ### System Type 입력(수행 서버), 전체 대문자
    swaggeer_tags = ['CONAI SYSTEM - UserConaiUserMst Restful API']
    swagger_operation_summary = "UserConaiUserMst Restful GET API"
    swagger_operation_description_add = "## 추가 정보\n" \
                                        "\n" \
                                        "### 필요한 내용 추가 정의 하여 사용\n" \
                                        "\n" \
                                        "PARAMETERS INFO\n" \
                                        "RESTFUL ORM 테스트용 테이블\n" \
                                        "|NAME           | TYPE    | PK   |DESC                    |ETC     |\n" \
                                        "|:-------------:|:-------:|:----:|:----------------------:|:------:|\n" \
                                        "|conaiUserMstId |CHAR     |   V  |커나이 유저 마스터 고유 아이디 |-      |\n" \
                                        "|userId         |CHAR     |      |사용자 아이디              |-      |\n" \
                                        "|userName       |CHAR     |      |사용자 이름               |-      |\n" \
                                        "|userPhoneNumber|INTEGER  |      |사용자 전화번호             |-      |\n"

    def __init__(self, *args, **kwargs):
        self.service = None
        super().__init__(**kwargs)

    def setup(self, request, *args, **kwargs):
        # init method 에서 container 생성할 경우, registry 가 생성 되지 않은 상태 에서 불러서 빈 컨테이너 생성됨
        # Create a container from the registry
        container = registry.create_container()

        print(f"container ==> {container}")
        # Resolve MyService from the container
        self.service = container.get(UserConaiUserMstRestfulService)
        # Call the parent class's setup method to assign request, args, and kwargs
        super().setup(request, *args, **kwargs)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary, ### DB Type 입력, 전체 대문자
                         operation_description="# CONAI SEVER에서 CONAI DB 로 CONAI_USER_MST Restful GET API 요청\n" + swagger_operation_description_add,
                         query_serializer=ConaiUserMstGetSerializer(),
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiUserMstGetSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             400: openapi.Response(description='Bad Request'),
                             401: openapi.Response(description='Unauthorized'),
                             403: openapi.Response(description='Forbidden'),
                             404: openapi.Response(description='Not Found'),
                             500: openapi.Response(description='Internal Server Error'), })

    @check_token
    def get(self, request):
        # Get all query parameters from the request
        query_params = request.query_params

        # Filter only string parameters
        string_params = {key: value for key, value in query_params.items() if isinstance(value, str)}

        # Do something with the string parameters
        # For example, print them or use them in your logic
        print("String parameters:", string_params)

        print("get request.data", request.data)

        result = self.service.user_conai_user_mst_get(string_params)

        print("result.data", result.data)

        return Response(result.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI SEVER에서 CONAI DB 로 CONAI_USER_MST Restful POST API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiUserMstPostSerializer,
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiUserMstPostSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             201: openapi.Response(
                                 description='Created',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiUserMstPostSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             400: openapi.Response(description='Bad Request'),
                             401: openapi.Response(description='Unauthorized'),
                             403: openapi.Response(description='Forbidden'),
                             404: openapi.Response(description='Not Found'),
                             500: openapi.Response(description='Internal Server Error'), })

    @check_token
    def post(self, request, *args, **kwargs):

        print("post request.data", request.data)

        print(f"{self.__class__.__name__} : Controller post post request.data ==> {request.data}")
        serializer = self.service.user_conai_user_mst_post(request.data)
        print(f"{self.__class__.__name__} : Controller post post serializer.is_valid() ==> {serializer.is_valid()}")
        # if serializer.is_valid(raise_exception=True):

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI SEVER에서 CONAI DB 로 CONAI_USER_MST Restful PUT API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiUserMstPutSerializer,
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiUserMstPutSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             400: openapi.Response(description='Bad Request'),
                             401: openapi.Response(description='Unauthorized'),
                             403: openapi.Response(description='Forbidden'),
                             404: openapi.Response(description='Not Found'),
                             500: openapi.Response(description='Internal Server Error'), })

    @check_token
    def put(self, request, *args, **kwargs):

        print("put request.data", request.data)

        serializer = self.service.user_conai_user_mst_put(request.data)

        # Response 객체가 리턴된 경우 에러로 간주, Response 객체를 그대로 리턴
        if isinstance(serializer, Response):
            return serializer

        if serializer.is_valid():
            # Update the upd_dtm field with the current time in the UTC timezone
            # serializer.validated_data['upd_dtm'] = timezone.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI SEVER에서 CONAI DB 로 CONAI_USER_MST Restful DELETE API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiUserMstDeleteSerializer,
                         responses={200: openapi.Response(
                             description='Success',
                             examples={
                                 'application/json': {
                                     'success': True,
                                     'data': ConaiUserMstDeleteSerializer().data  # Use your serializer here
                                 }
                             }
                         ),
                             204: openapi.Response(
                                 description='No Content',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiUserMstDeleteSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             400: openapi.Response(description='Bad Request'),
                             401: openapi.Response(description='Unauthorized'),
                             403: openapi.Response(description='Forbidden'),
                             404: openapi.Response(description='Not Found'),
                             500: openapi.Response(description='Internal Server Error'),
                         })

    @check_token
    def delete(self, request, *args, **kwargs):

        print("delete request.data", request.data)

        tag_object = self.service.user_conai_user_mst_delete(request.data)

        # Response 객체가 리턴된 경우 에러로 간주, Response 객체를 그대로 리턴
        if isinstance(tag_object, Response):
            return tag_object

        deleted_objects_count, _ = tag_object.delete()

        if deleted_objects_count >= 1:
            # Deletion was successful
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            # Deletion was not successful
            return Response({'detail': 'Object not found or not deleted.'}, status=status.HTTP_404_NOT_FOUND)
