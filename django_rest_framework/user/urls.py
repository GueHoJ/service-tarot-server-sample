from django.urls import path

from . import views
from .adapter._in.user_conai_tarot_service_user_mst_restful_api_controller import \
    UserConaiTarotServiceUserMstRestfulApiController
from .adapter._in.user_conai_user_mst_restful_api_controller import UserConaiUserMstRestfulApiController

app_name = 'user'

"""
    # CLASS : User 
    # AUTHOR : conai
    # TIME : 2024. 8. 16. 오후 12:52
    # DESCRIPTION
        - User urls end point

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 8. 16.          conai          최초 생성
"""

# 진입점 설정
urlpatterns = [
    # 'should modify first letter into lowercase => example' path("lower_camel_table", upper_camel_classRestfulApiController.as_view()),
    path("conaiUserMst", UserConaiUserMstRestfulApiController.as_view()),
    path("conaiTarotServiceUserMst", UserConaiTarotServiceUserMstRestfulApiController.as_view()),
]
