from django.conf import settings
import logging

from ..port._in.chatbot_conai_chatbot_gpt_parameters_mst_restful_in_port import ChatbotConaiChatbotGptParametersMstRestfulInPort
from ..port.out.chatbot_conai_chatbot_gpt_parameters_mst_restful_out_port import ChatbotConaiChatbotGptParametersMstRestfulOutPort
import app.utils.common_utils as common_utils


logger = logging.getLogger("django.server")


class ChatbotConaiChatbotGptParametersMstRestfulService:
    """
    # CLASS : ChatbotConaiChatbotGptParametersMstRestfulService
    # AUTHOR : conai
    # TIME : 2024. 12. 20. 오후 4:41
    # DESCRIPTION
        - ChatbotConaiChatbotGptParametersMst Restful Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 20.          conai          최초 생성
    """

    def __init__(self, portInImpl: ChatbotConaiChatbotGptParametersMstRestfulInPort, portOutImpl: ChatbotConaiChatbotGptParametersMstRestfulOutPort):
        self.chatbotIn = portInImpl
        self.chatbotOut = portOutImpl

    def chatbot_conai_chatbot_gpt_parameters_mst_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_get *args ==> {args[0]}")

        data = self.chatbotIn.chatbot_conai_chatbot_gpt_parameters_mst_restful_in_port_get(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_get kwarg ==> {kwarg}")

        DB_ADR = common_utils.get_db_info()
        result = self.chatbotOut.chatbot_conai_chatbot_gpt_parameters_mst_restful_db_out_port_get(self, DB_ADR, data)

        print(f"{self.__class__.__name__} : chatbot_conai_chatbot_gpt_parameters_mst_get result ==> {result}")

        return result

    def chatbot_conai_chatbot_gpt_parameters_mst_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_post *args ==> {args[0]}")

        data = self.chatbotIn.chatbot_conai_chatbot_gpt_parameters_mst_restful_in_port_post(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_post arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_post kwarg ==> {kwarg}")

        DB_ADR = common_utils.get_db_info()
        result = self.chatbotOut.chatbot_conai_chatbot_gpt_parameters_mst_restful_db_out_port_post(self, DB_ADR, data)

        print(f"{self.__class__.__name__} : chatbot_conai_chatbot_gpt_parameters_mst_post result ==> {result}")

        return result

    def chatbot_conai_chatbot_gpt_parameters_mst_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_put *args ==> {args[0]}")

        data = self.chatbotIn.chatbot_conai_chatbot_gpt_parameters_mst_restful_in_port_put(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_put arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_put kwarg ==> {kwarg}")

        DB_ADR = common_utils.get_db_info()
        result = self.chatbotOut.chatbot_conai_chatbot_gpt_parameters_mst_restful_db_out_port_put(self, DB_ADR, data)

        print(f"{self.__class__.__name__} : chatbot_conai_chatbot_gpt_parameters_mst_put result ==> {result}")

        return result

    def chatbot_conai_chatbot_gpt_parameters_mst_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_delete *args ==> {args[0]}")

        data = self.chatbotIn.chatbot_conai_chatbot_gpt_parameters_mst_restful_in_port_delete(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_delete arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} chatbot_conai_chatbot_gpt_parameters_mst_delete kwarg ==> {kwarg}")

        DB_ADR = common_utils.get_db_info()
        result = self.chatbotOut.chatbot_conai_chatbot_gpt_parameters_mst_restful_db_out_port_delete(self, DB_ADR, data)

        print(f"{self.__class__.__name__} : chatbot_conai_chatbot_gpt_parameters_mst_delete result ==> {result}")

        return result
