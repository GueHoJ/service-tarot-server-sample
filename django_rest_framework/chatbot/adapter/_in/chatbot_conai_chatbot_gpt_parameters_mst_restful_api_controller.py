from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import permissions, status
from rest_framework.views import APIView
from django.utils import timezone

from ...application.service.chatbot_conai_chatbot_gpt_parameters_mst_restful_service import \
    ChatbotConaiChatbotGptParametersMstRestfulService
from ...domain.CONAI_CHATBOT_GPT_PARAMETERS_MST import ConaiChatbotGptParametersMst
from ...serializers.conai_chatbot_gpt_parameters_mst_restful_serializer import \
    ConaiChatbotGptParametersMstGetSerializer, ConaiChatbotGptParametersMstPostSerializer, \
    ConaiChatbotGptParametersMstPutSerializer, ConaiChatbotGptParametersMstDeleteSerializer
import app.utils.common_utils as common_utils
from app.utils.decorator import check_token
from chatbot.containers import registry


class ChatbotConaiChatbotGptParametersMstRestfulApiController(APIView):
    """
    # CLASS : ChatbotConaiChatbotGptParametersMstRestfulApiController
    # AUTHOR : conai
    # TIME : 2024. 12. 20. 오후 4:34
    # DESCRIPTION
        - ChatbotConaiChatbotGptParametersMstRestfulApiController
        - CONAI_CHATBOT_GPT_PARAMETERS_MST API
        - 디렉터리 : chatbot
        - 서비스 설명 : CONAI_CHATBOT_GPT_PARAMETERS_MST API
        - 서비스 호출 url : /chatbot/conaiChatbotGptParametersMst
        - 서비스 호출 method : GET POST PUT DELETE
        - 서비스 호출 body : json
        - 서비스 호출 파라미터 :
            conaiChatbotGptParametersId (Unique identifier for each parameter set.)
            userId (Unique identifier for each user.)
            sessionId (Identifier for the chatbot session.)
            configName (Name of the configuration preset.)
            model (AI model used for chatbot interactions.)
            temperature (Controls randomness in model output.)
            maxTokens (Maximum number of tokens to generate in a response.)
            stopSequences (Stop sequences as a JSON array.)
            topP (Top-p sampling for nucleus sampling.)
            frequencyPenalty (Penalty for token frequency repetition.)
            presencePenalty (Penalty for encouraging new topics.)
            description (Explanation or description of the preset.)
            createdAt (Timestamp when the row was created.)
            updatedAt (Timestamp when the row was last updated.)

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 20.          conai          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    ### System Type 입력(수행 서버), 전체 대문자
    swaggeer_tags = ['CONAI TAROT SYSTEM - ChatbotConaiChatbotGptParametersMst Restful API']
    swagger_operation_summary = "ChatbotConaiChatbotGptParametersMst Restful GET API"
    swagger_operation_description_add = "## 추가 정보\n" \
                                        "\n" \
                                        "### 필요한 내용 추가 정의 하여 사용\n" \
                                        "\n" \
                                        "PARAMETERS INFO\n" \
                                        "CONAI_CHATBOT_GPT_PARAMETERS_MST API 테이블\n" \
                                        "|NAME                   | TYPE    | PK   |DESC                                |ETC     |\n" \
                                        "|:---------------------:|:-------:|:----:|:----------------------------------:|:------:|\n" \
                                        "|conaiChatbotGptParametersId |UUID    |   V  |Unique identifier for each parameter set. |-      |\n" \
                                        "|userId                |CHAR     |      |Unique identifier for each user.    |-      |\n" \
                                        "|sessionId             |CHAR     |      |Identifier for the chatbot session. |-      |\n" \
                                        "|configName            |CHAR     |      |Name of the configuration preset.   |-      |\n" \
                                        "|model                 |CHAR     |      |AI model used for chatbot interactions. |-      |\n" \
                                        "|temperature           |FLOAT    |      |Controls randomness in model output.|-      |\n" \
                                        "|maxTokens             |INT      |      |Maximum number of tokens to generate in a response. |-      |\n" \
                                        "|stopSequences         |JSON     |      |Stop sequences as a JSON array.     |-      |\n" \
                                        "|topP                  |FLOAT    |      |Top-p sampling for nucleus sampling.|-      |\n" \
                                        "|frequencyPenalty      |FLOAT    |      |Penalty for token frequency repetition. |-      |\n" \
                                        "|presencePenalty       |FLOAT    |      |Penalty for encouraging new topics. |-      |\n" \
                                        "|description           |TEXT     |      |Explanation or description of the preset. |-      |\n" \
                                        "|createdAt             |DATETIME |      |Timestamp when the row was created. |-      |\n" \
                                        "|updatedAt             |DATETIME |      |Timestamp when the row was last updated. |-      |\n"

    def __init__(self, *args, **kwargs):
        self.service = None
        super().__init__(**kwargs)

    def setup(self, request, *args, **kwargs):
        # init method 에서 container 생성할 경우, registry 가 생성 되지 않은 상태 에서 불러서 빈 컨테이너 생성됨
        # Create a container from the registry
        container = registry.create_container()

        print(f"container ==> {container}")
        # Resolve MyService from the container
        self.service = container.get(ChatbotConaiChatbotGptParametersMstRestfulService)
        # Call the parent class's setup method to assign request, args, and kwargs
        super().setup(request, *args, **kwargs)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,  ### DB Type 입력, 전체 대문자
                         operation_description="# CONAI TAROT SEVER에서 CONAI TAROT DB 로 CONAI_CHATBOT_GPT_PARAMETERS_MST Restful GET API 요청\n" + swagger_operation_description_add,
                         query_serializer=ConaiChatbotGptParametersMstGetSerializer(),
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiChatbotGptParametersMstGetSerializer().data
                                         # Use your serializer here
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

        result = self.service.chatbot_conai_chatbot_gpt_parameters_mst_get(string_params)

        print("result.data", result.data)

        return Response(result.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI TAROT SEVER에서 CONAI TAROT DB 로 CONAI_CHATBOT_GPT_PARAMETERS_MST Restful POST API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiChatbotGptParametersMstPostSerializer,
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiChatbotGptParametersMstPostSerializer().data
                                         # Use your serializer here
                                     }
                                 }
                             ),
                             201: openapi.Response(
                                 description='Created',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiChatbotGptParametersMstPostSerializer().data
                                         # Use your serializer here
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
        serializer = self.service.chatbot_conai_chatbot_gpt_parameters_mst_post(request.data)
        print(f"{self.__class__.__name__} : Controller post post serializer.is_valid() ==> {serializer.is_valid()}")
        # if serializer.is_valid(raise_exception=True):

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI TAROT SEVER에서 CONAI TAROT DB 로 CONAI_CHATBOT_GPT_PARAMETERS_MST Restful PUT API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiChatbotGptParametersMstPutSerializer,
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiChatbotGptParametersMstPutSerializer().data
                                         # Use your serializer here
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

        result_object = self.service.chatbot_conai_chatbot_gpt_parameters_mst_put(request.data)
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

            bulk_serializer = ConaiChatbotGptParametersMstPutSerializer(ordered_instances, data=serializer.initial_data,
                                                                        many=True, partial=True)
            print("{self.__class__.__name__} : Controller put bulk_serializer:", bulk_serializer)

            result_validated_data = []
            # Manually validate each instance using `is_valid` on each child
            for idx, child_serializer in enumerate(bulk_serializer.child.initial_data):
                instance = ordered_instances[idx]
                single_serializer = ConaiChatbotGptParametersMstPutSerializer(instance, data=child_serializer,
                                                                              partial=True)

                if not single_serializer.is_valid():
                    print(
                        f"{self.__class__.__name__} : Controller put Child serializer {idx} is not valid: {single_serializer.errors}")
                    return Response(single_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                updated_instance = single_serializer.save()
                serialized_data = ConaiChatbotGptParametersMstPutSerializer(updated_instance).data
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
                print("{self.__class__.__name__} : Controller put Returning Response with status:",
                      status.HTTP_201_CREATED)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print("{self.__class__.__name__} : Controller put serializer is not valid, errors:", serializer.errors)
                print("{self.__class__.__name__} : Controller put Returning Response with status:",
                      status.HTTP_400_BAD_REQUEST)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI TAROT SEVER에서 CONAI TAROT DB 로 CONAI_CHATBOT_GPT_PARAMETERS_MST Restful DELETE API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiChatbotGptParametersMstDeleteSerializer,
                         responses={200: openapi.Response(
                             description='Success',
                             examples={
                                 'application/json': {
                                     'success': True,
                                     'data': ConaiChatbotGptParametersMstDeleteSerializer().data
                                     # Use your serializer here
                                 }
                             }
                         ),
                             204: openapi.Response(
                                 description='No Content',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiChatbotGptParametersMstDeleteSerializer().data
                                         # Use your serializer here
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

        tag_object = self.service.chatbot_conai_chatbot_gpt_parameters_mst_delete(request.data)

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
