from django.urls import path

from . import views
from .adapter._in.servicetoken_conai_tarot_service_user_token_mst_restful_api_controller import ServicetokenConaiTarotServiceUserTokenMstRestfulApiController

app_name = 'servicetoken'

"""
    # CLASS : Servicetoken 
    # AUTHOR : conai
    # TIME : 2025. 1. 22. 오후 6:06
    # DESCRIPTION
        - Servicetoken urls end point

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2025. 1. 22.          conai          최초 생성
"""

# 진입점 설정
urlpatterns = [
    # 'should modify first letter into lowercase => example' path("lower_camel_table", upper_camel_classRestfulApiController.as_view()),
    path("conaiTarotServiceUserTokenMst", ServicetokenConaiTarotServiceUserTokenMstRestfulApiController.as_view()),
]
