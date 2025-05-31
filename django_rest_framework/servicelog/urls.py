from django.urls import path

from . import views
from .adapter._in.servicelog_conai_tarot_service_log_mst_restful_api_controller import \
    ServicelogConaiTarotServiceLogMstRestfulApiController

app_name = 'servicelog'

"""
    # CLASS : Servicelog 
    # AUTHOR : conai
    # TIME : 2025. 1. 15. 오후 12:24
    # DESCRIPTION
        - Servicelog urls end point

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2025. 1. 15.          conai          최초 생성
"""

# 진입점 설정
urlpatterns = [
    # 'should modify first letter into lowercase => example' path("lower_camel_table", upper_camel_classRestfulApiController.as_view()),
    path("conaiTarotServiceLogMst", ServicelogConaiTarotServiceLogMstRestfulApiController.as_view()),
]
