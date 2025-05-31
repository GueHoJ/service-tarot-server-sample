from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .adapter._in.chatbot_conai_chatbot_conversation_history_mst_restful_api_controller import \
    ChatbotConaiChatbotConversationHistoryMstRestfulApiController
from .adapter._in.chatbot_conai_chatbot_conversation_mst_restful_api_controller import \
    ChatbotConaiChatbotConversationMstRestfulApiController
from .adapter._in.chatbot_conai_chatbot_message_mst_restful_api_controller import \
    ChatbotConaiChatbotMessageMstRestfulApiController
from .adapter._in.chatbot_conai_tarot_service_cards_info_mst_restful_api_controller import \
    ChatbotConaiTarotServiceCardsInfoMstRestfulApiController
from .adapter._in.chatbot_conai_tarot_service_default_message_mst_restful_api_controller import \
    ChatbotConaiTarotServiceDefaultMessageMstRestfulApiController
from .views import GPTParameterViewSet
from .adapter._in.chatbot_conai_chatbot_gpt_parameters_mst_restful_api_controller import ChatbotConaiChatbotGptParametersMstRestfulApiController

app_name = 'chatbot'

"""
    # CLASS : Chatbot 
    # AUTHOR : conai
    # TIME : 2024. 12. 20. 오후 4:50
    # DESCRIPTION
        - Chatbot urls end point

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 20.          conai          최초 생성
"""

router = DefaultRouter()
router.register(r'gpt-parameters', GPTParameterViewSet, basename='gpt-parameters')

# 진입점 설정
urlpatterns = [
    # 'should modify first letter into lowercase => example' path("lower_camel_table", upper_camel_classRestfulApiController.as_view()),

    path('api/', include(router.urls)),
    path("conaiChatbotGptParametersMst", ChatbotConaiChatbotGptParametersMstRestfulApiController.as_view()),
    path("conaiChatbotConversationHistoryMst", ChatbotConaiChatbotConversationHistoryMstRestfulApiController.as_view()),
    path("conaiChatbotConversationMst", ChatbotConaiChatbotConversationMstRestfulApiController.as_view()),
    path("conaiChatbotMessageMst", ChatbotConaiChatbotMessageMstRestfulApiController.as_view()),
    path("conaiTarotServiceCardsInfoMst", ChatbotConaiTarotServiceCardsInfoMstRestfulApiController.as_view()),
    path("conaiTarotServiceDefaultMessageMst", ChatbotConaiTarotServiceDefaultMessageMstRestfulApiController.as_view()),
]
