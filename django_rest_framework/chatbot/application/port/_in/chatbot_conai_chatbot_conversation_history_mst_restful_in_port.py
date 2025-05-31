from abc import ABC, abstractmethod


class ChatbotConaiChatbotConversationHistoryMstRestfulInPort(ABC):
    """
    # CLASS : ChatbotConaiChatbotConversationHistoryMstRestfulInPort
    # AUTHOR : conai
    # TIME : 2024. 12. 24. conai
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 24.          conai          최초 생성
    """

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port(self, *args, **kwargs):
        pass

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port_get(self, *args, **kwargs):
        pass

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port_post(self, *args, **kwargs):
        pass

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port_put(self, *args, **kwargs):
        pass

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port_delete(self, *args, **kwargs):
        pass


class ChatbotConaiChatbotConversationHistoryMstRestfulInPortImpl(ChatbotConaiChatbotConversationHistoryMstRestfulInPort):

    def __init__(self):
        pass

    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_in_port request params ==> {args[1]}")
        result = args[1]

        return result

    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_in_port_get request params ==> {args[1]}")
        result = args[1]

        return result

    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_in_port_post request params ==> {args[1]}")
        result = args[1]

        return result

    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_in_port_put request params ==> {args[1]}")
        result = args[1]

        return result

    def chatbot_conai_chatbot_conversation_history_mst_restful_in_port_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_in_port_delete request params ==> {args[1]}")
        result = args[1]

        return result
