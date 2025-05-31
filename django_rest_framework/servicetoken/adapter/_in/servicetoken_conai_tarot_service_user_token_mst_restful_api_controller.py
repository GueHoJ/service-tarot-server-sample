from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import permissions, status
from rest_framework.views import APIView
from django.utils import timezone

from ...application.service.servicetoken_conai_tarot_service_user_token_mst_restful_service import ServicetokenConaiTarotServiceUserTokenMstRestfulService
from ...domain.CONAI_TAROT_SERVICE_USER_TOKEN_MST import ConaiTarotServiceUserTokenMst
from ...serializers.conai_tarot_service_user_token_mst_restful_serializer import ConaiTarotServiceUserTokenMstGetSerializer, ConaiTarotServiceUserTokenMstPostSerializer, \
    ConaiTarotServiceUserTokenMstPutSerializer, ConaiTarotServiceUserTokenMstDeleteSerializer
import app.utils.common_utils as common_utils
from app.utils.decorator import check_token
from servicetoken.containers import registry


class ServicetokenConaiTarotServiceUserTokenMstRestfulApiController(APIView):
    """
    # CLASS : ServicetokenConaiTarotServiceUserTokenMstRestfulApiController
    # AUTHOR : conai
    # TIME : 2025. 1. 22. 오후 6:10
    # DESCRIPTION
        - ServicetokenConaiTarotServiceUserTokenMstRestfulApiController
        - CONAI_TAROT_SERVICE_USER_TOKEN_MST API
        - 디렉터리 : servicetoken
        - 서비스 설명 : CONAI_TAROT_SERVICE_USER_TOKEN_MST API
        - 서비스 호출 url : /servicetoken/conaiTarotServiceUserTokenMst
        - 서비스 호출 method : GET POST PUT DELETE
        - 서비스 호출 body : json
        - 서비스 호출 파라미터 :
            conaiTarotServiceUserTokenMstId (Primary key and unique identifier for each token record)
            userId (Unique identifier for the user associated with this token)
            accessToken (Current access token for user authentication)
            refreshToken (Refresh token associated with the access token)
            isActive (Indicates whether the token is currently active or has been invalidated)
            expiresAt (Expiration timestamp of the access token)
            createdAt (Timestamp when the token was created)
            updatedAt (Timestamp when the token was last updated)

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2025. 1. 22.          conai          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    ### System Type 입력(수행 서버), 전체 대문자
    swaggeer_tags = ['CONAI TAROT SYSTEM - ServicetokenConaiTarotServiceUserTokenMst Restful API']
    swagger_operation_summary = "ServicetokenConaiTarotServiceUserTokenMst Restful GET API"
    swagger_operation_description_add = "## 추가 정보\n" \
                                        "\n" \
                                        "### 필요한 내용 추가 정의 하여 사용\n" \
                                        "\n" \
                                        "PARAMETERS INFO\n" \
                                        "CONAI_TAROT_SERVICE_USER_TOKEN_MST API 테이블\n" \
                                        "| NAME                      | TYPE      | PK   | DESC                                         | ETC     |\n" \
                                        "|---------------------------|-----------|------|---------------------------------------------|---------|\n" \
                                        "| conaiTarotServiceUserTokenMstId | UUID      |  V   | Primary key and unique identifier for each token record | -       |\n" \
                                        "| userId                   | UUID      |      | Unique identifier for the user associated with this token | -       |\n" \
                                        "| accessToken              | TEXT      |      | Current access token for user authentication | -       |\n" \
                                        "| refreshToken             | TEXT      |      | Refresh token associated with the access token | -       |\n" \
                                        "| isActive                 | BOOLEAN   |      | Indicates whether the token is currently active or has been invalidated | -       |\n" \
                                        "| expiresAt                | TIMESTAMP |      | Expiration timestamp of the access token    | -       |\n" \
                                        "| createdAt                | TIMESTAMP |      | Timestamp when the token was created        | -       |\n" \
                                        "| updatedAt                | TIMESTAMP |      | Timestamp when the token was last updated   | -       |\n"

    def __init__(self, *args, **kwargs):
        self.service = None
        super().__init__(**kwargs)

    def setup(self, request, *args, **kwargs):
        # init method 에서 container 생성할 경우, registry 가 생성 되지 않은 상태 에서 불러서 빈 컨테이너 생성됨
        # Create a container from the registry
        container = registry.create_container()

        print(f"container ==> {container}")
        # Resolve MyService from the container
        self.service = container.get(ServicetokenConaiTarotServiceUserTokenMstRestfulService)
        # Call the parent class's setup method to assign request, args, and kwargs
        super().setup(request, *args, **kwargs)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary, ### DB Type 입력, 전체 대문자
                         operation_description="# CONAI TAROT SEVER에서 CONAI TAROT DB 로 CONAI_TAROT_SERVICE_USER_TOKEN_MST Restful GET API 요청\n" + swagger_operation_description_add,
                         query_serializer=ConaiTarotServiceUserTokenMstGetSerializer(),
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiTarotServiceUserTokenMstGetSerializer().data  # Use your serializer here
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

        result = self.service.servicetoken_conai_tarot_service_user_token_mst_get(string_params)

        print("result.data", result.data)

        return Response(result.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI TAROT SEVER에서 CONAI TAROT DB 로 CONAI_TAROT_SERVICE_USER_TOKEN_MST Restful POST API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiTarotServiceUserTokenMstPostSerializer,
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiTarotServiceUserTokenMstPostSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             201: openapi.Response(
                                 description='Created',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiTarotServiceUserTokenMstPostSerializer().data  # Use your serializer here
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
        serializer = self.service.servicetoken_conai_tarot_service_user_token_mst_post(request.data)
        print(f"{self.__class__.__name__} : Controller post post serializer.is_valid() ==> {serializer.is_valid()}")
        # if serializer.is_valid(raise_exception=True):

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI TAROT SEVER에서 CONAI TAROT DB 로 CONAI_TAROT_SERVICE_USER_TOKEN_MST Restful PUT API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiTarotServiceUserTokenMstPutSerializer,
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiTarotServiceUserTokenMstPutSerializer().data  # Use your serializer here
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

        result_object = self.service.servicetoken_conai_tarot_service_user_token_mst_put(request.data)
        print("{self.__class__.__name__} : Controller put result_object:", result_object)

        serializer = result_object.get('result_serializer')
        print("{self.__class__.__name__} : Controller put serializer:", serializer)

        # Response 객체가 리턴된 경우 에러로 간주, Response 객체를 그대로 리턴
        if isinstance(serializer, Response):
            return serializer

        print(f"{self.__class__.__name__} : Controller put type(serializer):", type(serializer))
        
        if isinstance(serializer.initial_data, list):
            print("{self.__class__.__name__} : Controller put serializer.initial_data is a list")
            ordered_instances = result_object.get('ordered_instances')
            print("{self.__class__.__name__} : Controller put ordered_instances:", ordered_instances)
            
            bulk_serializer = ConaiTarotServiceUserTokenMstPutSerializer(ordered_instances, data=serializer.initial_data, many=True, partial=True)
            print("{self.__class__.__name__} : Controller put bulk_serializer:", bulk_serializer)

            result_validated_data = []
            # Manually validate each instance using `is_valid` on each child
            for idx, child_serializer in enumerate(bulk_serializer.child.initial_data):
                instance = ordered_instances[idx]
                single_serializer = ConaiTarotServiceUserTokenMstPutSerializer(instance, data=child_serializer, partial=True)

                if not single_serializer.is_valid():
                    print(f"{self.__class__.__name__} : Controller put Child serializer {idx} is not valid: {single_serializer.errors}")
                    return Response(single_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                updated_instance = single_serializer.save()
                serialized_data = ConaiTarotServiceUserTokenMstPutSerializer(updated_instance).data
                result_validated_data.append(serialized_data)

            print("{self.__class__.__name__} : Controller put Returning Response with status:", status.HTTP_201_CREATED)
            return Response(result_validated_data, status=status.HTTP_201_CREATED)
        else:
            print("{self.__class__.__name__} : Controller put serializer.initial_data is not a list")
            if serializer.is_valid():
                print("{self.__class__.__name__} : Controller put serializer is valid")
                saved_instance = serializer.save()
                print("{self.__class__.__name__} : Controller put saved_instance:", saved_instance)
                
                print("{self.__class__.__name__} : Controller put serializer.data:", serializer.data)
                print("{self.__class__.__name__} : Controller put Returning Response with status:", status.HTTP_201_CREATED)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print("{self.__class__.__name__} : Controller put serializer is not valid, errors:", serializer.errors)
                print("{self.__class__.__name__} : Controller put Returning Response with status:", status.HTTP_400_BAD_REQUEST)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI TAROT SEVER에서 CONAI TAROT DB 로 CONAI_TAROT_SERVICE_USER_TOKEN_MST Restful DELETE API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiTarotServiceUserTokenMstDeleteSerializer,
                         responses={200: openapi.Response(
                             description='Success',
                             examples={
                                 'application/json': {
                                     'success': True,
                                     'data': ConaiTarotServiceUserTokenMstDeleteSerializer().data  # Use your serializer here
                                 }
                             }
                         ),
                             204: openapi.Response(
                                 description='No Content',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiTarotServiceUserTokenMstDeleteSerializer().data  # Use your serializer here
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

        tag_object = self.service.servicetoken_conai_tarot_service_user_token_mst_delete(request.data)

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
