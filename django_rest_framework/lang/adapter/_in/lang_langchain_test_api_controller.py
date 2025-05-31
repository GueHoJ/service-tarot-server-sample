from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.views import APIView

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from langchain.schema.runnable import RunnableSequence


from lang.serializers.langchain_test_serializers import ChainTestSerializersGetSerializer, \
    ChainTestSerializersPostSerializer

from lang.utils.load_lama_model import get_model



class LangLangchainTestApiControllerRestfulApiController(APIView):
    """
    # CLASS : LangLangchainTestApiControllerRestfulApiController
    # AUTHOR : conai
    # TIME : 2024. 11. 10. 오후 12:53
    # DESCRIPTION
        - LangLangchainTestApiControllerRestfulApiController
        - LANGCHAIN_TEST_API_CONTROLLER API
        - 디렉터리 : lang
        - 서비스 설명 :
        - 서비스 호출 url : /lang/langchainTestApiController
        - 서비스 호출 method : GET POST PUT DELETE
        - 서비스 호출 body : json
        - 서비스 호출 파라미터 :

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 11. 10.          conai          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    ### System Type 입력(수행 서버), 전체 대문자
    swaggeer_tags = [' SYSTEM - LangLangchainTestApiController Restful API']
    swagger_operation_summary = "LangLangchainTestApiController Restful GET API"
    swagger_operation_description_add = "## 추가 정보\n" \
                                        "\n" \
                                        "### 필요한 내용 추가 정의 하여 사용\n" \
                                        "\n" \
                                        "PARAMETERS INFO\n" \
                                        " 테이블\n" \
                                        "|NAME           | TYPE    | PK   |DESC                    |ETC     |\n" \
                                        "|:-------------:|:-------:|:----:|:----------------------:|:------:|\n" \
                                        "|conaiUserMstId |PUSH     |   V  |커나이 유저 마스터 고유 아이디 |-      |\n" \
                                        "|userId         |PUSH     |      |사용자 아이디              |-      |\n" \
                                        "|userName       |PUSH     |      |사용자 이름               |-      |\n" \
                                        "|userPhoneNumber|NTC      |      |사용자 전화번호             |-      |\n"

    def __init__(self, *args, **kwargs):
        self.service = None
        super().__init__(**kwargs)

    # def setup(self, request, *args, **kwargs):
        # init method 에서 container 생성할 경우, registry 가 생성 되지 않은 상태 에서 불러서 빈 컨테이너 생성됨
        # Create a container from the registry
        # container = registry.create_container()

        # print(f"container ==> {container}")
        # Resolve MyService from the container
        # self.service = container.get(LangLangchainTestApiControllerRestfulService)
        # Call the parent class's setup method to assign request, args, and kwargs
        # super().setup(request, *args, **kwargs)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary, ### DB Type 입력, 전체 대문자
                         operation_description="#  SEVER에서 LANGCHAIN AI 로 LANGCHAIN_TEST_API_CONTROLLER Restful GET API 요청\n" + swagger_operation_description_add,
                         query_serializer=ChainTestSerializersGetSerializer(),
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ChainTestSerializersGetSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             400: openapi.Response(description='Bad Request'),
                             401: openapi.Response(description='Unauthorized'),
                             403: openapi.Response(description='Forbidden'),
                             404: openapi.Response(description='Not Found'),
                             500: openapi.Response(description='Internal Server Error'), })


    def get(self, request):
        # Get all query parameters from the request
        query_params = request.query_params

        # Filter only string parameters
        string_params = {key: value for key, value in query_params.items() if isinstance(value, str)}

        # Do something with the string parameters
        # For example, print them or use them in your logic
        print("String parameters:", string_params)

        print("get request.data", request.data)

        # result = self.service.lang_langchain_test_api_controller_get(string_params)
        #
        # print("result.data", result.data)

        params = request.data

        model_path = params.get("modelPath")

        # Load Llama3.2-90B-Vision-Instruct
        model_90b_path = "meta-llama/Llama-3.2-90B-Vision-Instruct"
        llm = get_model

        # Example usage with LLaMA models
        prompt = "Describe the content and purpose of LangChain."
        response_90b = llm(prompt)
        print("Llama3.2-90B-Vision-Instruct Response:", response_90b)

        return Response(response_90b, status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="#  SEVER에서 LANGCHAIN AI 로 LANGCHAIN_TEST_API_CONTROLLER Restful POST API 요청\n" + swagger_operation_description_add,
                         request_body=ChainTestSerializersPostSerializer,
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ChainTestSerializersPostSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             201: openapi.Response(
                                 description='Created',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ChainTestSerializersPostSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             400: openapi.Response(description='Bad Request'),
                             401: openapi.Response(description='Unauthorized'),
                             403: openapi.Response(description='Forbidden'),
                             404: openapi.Response(description='Not Found'),
                             500: openapi.Response(description='Internal Server Error'), })


    def post(self, request, *args, **kwargs):

        print("post request.data", request.data)

        print(f"{self.__class__.__name__} : Controller post post request.data ==> {request.data}")
        # serializer = self.service.lang_langchain_test_api_controller_post(request.data)
        # print(f"{self.__class__.__name__} : Controller post post serializer.is_valid() ==> {serializer.is_valid()}")
        # if serializer.is_valid(raise_exception=True):

        params = request.data

        model_path = params.get("modelPath")
        task = params.get("task")

        # Use the preloaded model
        llm = get_model()

        # Example usage with LLaMA models
        prompt_json = params.get("promptText") if params.get("promptText") else "Describe the content and purpose of LangChain."
        question = prompt_json.get("question")
        context = prompt_json.get("context")
        prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
        print(f"prompt : {prompt}")
        # response = llm(prompt)
        # Define the LangChain prompt template
        # Create a prompt template
        template = PromptTemplate(
            template="{context}\n{question}\nAnswer:",
            input_variables=["context", "question"]
        )

        # Initialize LangChain
        llm_chain = template | llm
        response = llm_chain.invoke({"context": context, "question": question})
        print(f"model_path : {model_path}\n"
              f"task : {task}\n"
              f"Response: {response}")

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status.HTTP_201_CREATED)

    # @swagger_auto_schema(tags=swaggeer_tags,
    #                      operation_summary=swagger_operation_summary,
    #                      operation_description="#  SEVER에서  DB 로 LANGCHAIN_TEST_API_CONTROLLER Restful PUT API 요청\n" + swagger_operation_description_add,
    #                      request_body=LangchainTestApiControllerPutSerializer,
    #                      responses={
    #                          200: openapi.Response(
    #                              description='Success',
    #                              examples={
    #                                  'application/json': {
    #                                      'success': True,
    #                                      'data': LangchainTestApiControllerPutSerializer().data  # Use your serializer here
    #                                  }
    #                              }
    #                          ),
    #                          400: openapi.Response(description='Bad Request'),
    #                          401: openapi.Response(description='Unauthorized'),
    #                          403: openapi.Response(description='Forbidden'),
    #                          404: openapi.Response(description='Not Found'),
    #                          500: openapi.Response(description='Internal Server Error'), })

    # @check_token
    # def put(self, request, *args, **kwargs):
    #
    #     print("put request.data", request.data)
    #
    #     result_object = self.service.lang_langchain_test_api_controller_put(request.data)
    #     print("{self.__class__.__name__} : Controller put result_object:", result_object)
    #
    #     serializer = result_object.get('result_serializer')
    #     print("{self.__class__.__name__} : Controller put serializer:", serializer)
    #
    #     # Response 객체가 리턴된 경우 에러로 간주, Response 객체를 그대로 리턴
    #     if isinstance(serializer, Response):
    #         return serializer
    #
    #     print(f"{self.__class__.__name__} : Controller put type(serializer):", type(serializer))
    #
    #     if isinstance(serializer.initial_data, list):
    #         print("{self.__class__.__name__} : Controller put serializer.initial_data is a list")
    #         ordered_instances = result_object.get('ordered_instances')
    #         print("{self.__class__.__name__} : Controller put ordered_instances:", ordered_instances)
    #
    #         bulk_serializer = LangchainTestApiControllerPutSerializer(ordered_instances, data=serializer.initial_data, many=True, partial=True)
    #         print("{self.__class__.__name__} : Controller put bulk_serializer:", bulk_serializer)
    #
    #         result_validated_data = []
    #         # Manually validate each instance using `is_valid` on each child
    #         for idx, child_serializer in enumerate(bulk_serializer.child.initial_data):
    #             instance = ordered_instances[idx]
    #             single_serializer = LangchainTestApiControllerPutSerializer(instance, data=child_serializer, partial=True)
    #
    #             if not single_serializer.is_valid():
    #                 print(f"{self.__class__.__name__} : Controller put Child serializer {idx} is not valid: {single_serializer.errors}")
    #                 return Response(single_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #             updated_instance = single_serializer.save()
    #             serialized_data = LangchainTestApiControllerPutSerializer(updated_instance).data
    #             result_validated_data.append(serialized_data)
    #
    #         print("{self.__class__.__name__} : Controller put Returning Response with status:", status.HTTP_201_CREATED)
    #         return Response(result_validated_data, status=status.HTTP_201_CREATED)
    #     else:
    #         if serializer.is_valid():
    #             # Update the upd_dtm field with the current time in the UTC timezone
    #             # serializer.validated_data['upd_dtm'] = timezone.now()
    #             print("{self.__class__.__name__} : Controller put serializer.initial_data is not a list")
    #         if serializer.is_valid():
    #             print("{self.__class__.__name__} : Controller put serializer is valid")
    #             saved_instance = serializer.save()
    #             print("{self.__class__.__name__} : Controller put saved_instance:", saved_instance)
    #
    #             print("{self.__class__.__name__} : Controller put serializer.data:", serializer.data)
    #             print("{self.__class__.__name__} : Controller put Returning Response with status:", status.HTTP_201_CREATED)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             print("{self.__class__.__name__} : Controller put serializer is not valid, errors:", serializer.errors)
    #             print("{self.__class__.__name__} : Controller put Returning Response with status:", status.HTTP_400_BAD_REQUEST)
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # @swagger_auto_schema(tags=swaggeer_tags,
    #                      operation_summary=swagger_operation_summary,
    #                      operation_description="#  SEVER에서  DB 로 LANGCHAIN_TEST_API_CONTROLLER Restful DELETE API 요청\n" + swagger_operation_description_add,
    #                      request_body=LangchainTestApiControllerDeleteSerializer,
    #                      responses={200: openapi.Response(
    #                          description='Success',
    #                          examples={
    #                              'application/json': {
    #                                  'success': True,
    #                                  'data': LangchainTestApiControllerDeleteSerializer().data  # Use your serializer here
    #                              }
    #                          }
    #                      ),
    #                          204: openapi.Response(
    #                              description='No Content',
    #                              examples={
    #                                  'application/json': {
    #                                      'success': True,
    #                                      'data': LangchainTestApiControllerDeleteSerializer().data  # Use your serializer here
    #                                  }
    #                              }
    #                          ),
    #                          400: openapi.Response(description='Bad Request'),
    #                          401: openapi.Response(description='Unauthorized'),
    #                          403: openapi.Response(description='Forbidden'),
    #                          404: openapi.Response(description='Not Found'),
    #                          500: openapi.Response(description='Internal Server Error'),
    #                      })
    #
    # @check_token
    # def delete(self, request, *args, **kwargs):
    #
    #     print("delete request.data", request.data)
    #
    #     tag_object = self.service.lang_langchain_test_api_controller_delete(request.data)
    #
    #     # Response 객체가 리턴된 경우 에러로 간주, Response 객체를 그대로 리턴
    #     if isinstance(tag_object, Response):
    #         return tag_object
    #
    #     deleted_objects_count, _ = tag_object.delete()
    #
    #     if deleted_objects_count >= 1:
    #         # Deletion was successful
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         # Deletion was not successful
    #         return Response({'detail': 'Object not found or not deleted.'}, status=status.HTTP_404_NOT_FOUND)
