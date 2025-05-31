from django.urls import path

from . import views
from .adapter._in.lang_langchain_test_api_controller import LangLangchainTestApiControllerRestfulApiController

# from .adapter._in.lang__restful_api_controller import LangRestfulApiController

app_name = 'lang'

"""
    # CLASS : Lang 
    # AUTHOR : conai
    # TIME : 2024. 11. 10. 오후 12:27
    # DESCRIPTION
        - Lang urls end point

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 11. 10.          conai          최초 생성
"""

# 진입점 설정
urlpatterns = [
    # 'should modify first letter into lowercase => example' path("lower_camel_table", upper_camel_classRestfulApiController.as_view()),
    path("langChaninTest", LangLangchainTestApiControllerRestfulApiController.as_view()),
]
