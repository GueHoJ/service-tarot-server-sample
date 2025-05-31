from django.urls import path

from . import views
from .adapter._in.ollamas_conai_llama_api_controller import OllamasConaiLlamaApiControllerRestfulApiController

app_name = 'ollamas'

"""
    # CLASS : Ollamas 
    # AUTHOR : conai
    # TIME : 2024. 12. 6. 오후 3:34
    # DESCRIPTION
        - Ollamas urls end point

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 6.          conai          최초 생성
"""

# 진입점 설정
urlpatterns = [
    # 'should modify first letter into lowercase => example' path("lower_camel_table", upper_camel_classRestfulApiController.as_view()),
    path("generate/", OllamasConaiLlamaApiControllerRestfulApiController.as_view()),
]
