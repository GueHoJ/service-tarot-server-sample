import requests
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import permissions, status
from rest_framework.views import APIView
from django.utils import timezone
from django.conf import settings

from ...serializers.conai_llama_api_serializer import ConaiLlamaApiRequestSerializer
import app.utils.common_utils as common_utils
from app.utils.decorator import check_token


class OllamasConaiLlamaApiControllerRestfulApiController(APIView):
    """
    # CLASS : OllamasConaiLlamaApiControllerRestfulApiController
    # AUTHOR : conai
    # TIME : 2024. 12. 6. 오후 5:01
    # DESCRIPTION
        - OllamasConaiLlamaApiControllerRestfulApiController
        - CONAI_LLAMA_API_CONTROLLER API
        - 디렉터리 : ollamas
        - 서비스 설명 : CONAI_LLAMA_API_CONTROLLER API
        - 서비스 호출 url : /ollamas/conaiLlamaApiController
        - 서비스 호출 method : GET POST PUT DELETE
        - 서비스 호출 body : json
        - 서비스 호출 파라미터 :
            model (AI 모델명)
            prompt (AI 프롬프트)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 6.          conai          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    ### System Type 입력(수행 서버), 전체 대문자
    swaggeer_tags = ['CONAI SYSTEM - OllamasConaiLlamaApiController Restful API']
    swagger_operation_summary = "OllamasConaiLlamaApiController Restful GET API"
    swagger_operation_description_add = "## 추가 정보\n" \
                                        "\n" \
                                        "### 필요한 내용 추가 정의 하여 사용\n" \
                                        "\n" \
                                        "PARAMETERS INFO\n" \
                                        "CONAI_LLAMA_API_CONTROLLER API 테이블\n" \
                                        "|NAME           | TYPE    | PK   |DESC                    |ETC     |\n" \
                                        "|:-------------:|:-------:|:----:|:----------------------:|:------:|\n" \
                                        "|conaiUserMstId |PUSH     |   V  |커나이 유저 마스터 고유 아이디 |-      |\n" \
                                        "|userId         |PUSH     |      |사용자 아이디              |-      |\n" \
                                        "|userName       |PUSH     |      |사용자 이름               |-      |\n" \
                                        "|userPhoneNumber|NTC      |      |사용자 전화번호             |-      |\n"

    @swagger_auto_schema(tags=swaggeer_tags,
                         operation_summary=swagger_operation_summary,
                         operation_description="# CONAI SEVER에서 OLLAMA MODEL DB 로 CONAI_LLAMA_API_CONTROLLER Restful POST API 요청\n" + swagger_operation_description_add,
                         request_body=ConaiLlamaApiRequestSerializer,
                         responses={
                             200: openapi.Response(
                                 description='Success',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiLlamaApiRequestSerializer().data  # Use your serializer here
                                     }
                                 }
                             ),
                             201: openapi.Response(
                                 description='Created',
                                 examples={
                                     'application/json': {
                                         'success': True,
                                         'data': ConaiLlamaApiRequestSerializer().data  # Use your serializer here
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
        serializer = ConaiLlamaApiRequestSerializer(data=request.data)
        print(f"{self.__class__.__name__} : Controller post post serializer.is_valid() ==> {serializer.is_valid()}")
        # if serializer.is_valid(raise_exception=True):

        if serializer.is_valid():
            model = serializer.validated_data.get("model")
            prompt = serializer.validated_data.get("prompt")
            # Ollama API endpoint
            ollama_url = f"{settings.OLLAMA_URL}/api/generate"

            try:
                # Send a POST request to the Ollama API
                response = requests.post(
                    ollama_url,
                    json={"model": model, "prompt": prompt},
                    timeout=60,  # Timeout for the request
                    # stream=True,
                )

                # Log the raw response
                print(f"Raw response content: {response.content}")

                # Raise HTTPError if the response contains an error
                response.raise_for_status()

                result_data = common_utils.process_streaming_response(response)

                # Return the JSON response from the API
                return Response(result_data, status=status.HTTP_200_OK)

            except requests.exceptions.RequestException as e:
                # Handle API errors
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except ValueError as json_error:
                # Handle JSON parsing errors
                return Response({"error": f"Invalid JSON response: {response.content}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
