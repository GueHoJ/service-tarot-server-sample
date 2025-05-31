from abc import ABC, abstractmethod

from ....adapter.out.chatbot_conai_chatbot_conversation_history_mst_restful_db_adapter import ChatbotConaiChatbotConversationHistoryMstRestfulDbAdapter


class ChatbotConaiChatbotConversationHistoryMstRestfulOutPort(ABC):
    """
    # CLASS : ChatbotConaiChatbotConversationHistoryMstRestfulOutPort
    # AUTHOR : conai
    # TIME : 2024. 12. 24. 오후 12:56
    # DESCRIPTION
        - ChatbotConaiChatbotConversationHistoryMst Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 24.          conai          최초 생성
    """

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port(self, request):
        pass

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_get(self, request):
        pass

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_post(self, request):
        pass

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_put(self, request):
        pass

    @abstractmethod
    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_delete(self, request):
        pass


class ChatbotConaiChatbotConversationHistoryMstRestfulOutPortImpl(ChatbotConaiChatbotConversationHistoryMstRestfulOutPort):

    def __init__(self, chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter: ChatbotConaiChatbotConversationHistoryMstRestfulDbAdapter
                 ):
        self.chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter = chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter

    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port kwarg ==> {kwarg}")

        result = self.chatbot_conai_chatbot_conversation_history_mstRestfulDbAdapter.chatbot_conai_chatbot_conversation_history_mst_restful_db(self, *args, **kwargs)

        return result

    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_out_port_get args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_out_port_get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_out_port_get kwarg ==> {kwarg}")

        result = self.chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter.chatbot_conai_chatbot_conversation_history_mst_restful_db_get(self, *args, **kwargs)

        return result

    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_post args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_post arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_post kwarg ==> {kwarg}")

        result = self.chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter.chatbot_conai_chatbot_conversation_history_mst_restful_db_post(self, *args, **kwargs)

        return result

    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_put args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_put arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_put kwarg ==> {kwarg}")

        result = self.chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter.chatbot_conai_chatbot_conversation_history_mst_restful_db_put(self, *args, **kwargs)

        return result

    def chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_delete args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_delete arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : chatbot_conai_chatbot_conversation_history_mst_restful_db_out_port_delete kwarg ==> {kwarg}")

        result = self.chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter.chatbot_conai_chatbot_conversation_history_mst_restful_db_delete(self, *args, **kwargs)

        return result
