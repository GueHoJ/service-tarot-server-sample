from chatbot.domain.CONAI_CHATBOT_GPT_PARAMETERS_MST import ConaiChatbotGptParametersMst
from chatbot.serializers.conai_chatbot_gpt_parameters_mst_restful_serializer import ConaiChatbotGptParametersMstGetSerializer, ConaiChatbotGptParametersMstPostSerializer, \
    ConaiChatbotGptParametersMstPutSerializer, ConaiChatbotGptParametersMstDeleteSerializer

from chatbot.adapter.out.chatbot_conai_chatbot_gpt_parameters_mst_restful_db_adapter import ChatbotConaiChatbotGptParametersMstRestfulDbAdapter
from chatbot.application.port.out.chatbot_conai_chatbot_gpt_parameters_mst_restful_out_port import ChatbotConaiChatbotGptParametersMstRestfulOutPort, \
    ChatbotConaiChatbotGptParametersMstRestfulOutPortImpl
from chatbot.application.port._in.chatbot_conai_chatbot_gpt_parameters_mst_restful_in_port import ChatbotConaiChatbotGptParametersMstRestfulInPort, \
    ChatbotConaiChatbotGptParametersMstRestfulInPortImpl
from chatbot.application.service.chatbot_conai_chatbot_gpt_parameters_mst_restful_service import ChatbotConaiChatbotGptParametersMstRestfulService

# from .adapter._in.chatbot_restful_api_controller import ChatbotConaiChatbotGptParametersMstRestfulApiController

from chatbot.domain.CONAI_CHATBOT_CONVERSATION_HISTORY_MST import ConaiChatbotConversationHistoryMst
from chatbot.serializers.conai_chatbot_conversation_history_mst_restful_serializer import ConaiChatbotConversationHistoryMstGetSerializer, ConaiChatbotConversationHistoryMstPostSerializer, \
    ConaiChatbotConversationHistoryMstPutSerializer, ConaiChatbotConversationHistoryMstDeleteSerializer

from chatbot.adapter.out.chatbot_conai_chatbot_conversation_history_mst_restful_db_adapter import ChatbotConaiChatbotConversationHistoryMstRestfulDbAdapter
from chatbot.application.port.out.chatbot_conai_chatbot_conversation_history_mst_restful_out_port import ChatbotConaiChatbotConversationHistoryMstRestfulOutPort, \
    ChatbotConaiChatbotConversationHistoryMstRestfulOutPortImpl
from chatbot.application.port._in.chatbot_conai_chatbot_conversation_history_mst_restful_in_port import ChatbotConaiChatbotConversationHistoryMstRestfulInPort, \
    ChatbotConaiChatbotConversationHistoryMstRestfulInPortImpl
from chatbot.application.service.chatbot_conai_chatbot_conversation_history_mst_restful_service import ChatbotConaiChatbotConversationHistoryMstRestfulService

# from .adapter._in.chatbot_restful_api_controller import ChatbotConaiChatbotConversationHistoryMstRestfulApiController

from chatbot.domain.CONAI_CHATBOT_CONVERSATION_MST import ConaiChatbotConversationMst
from chatbot.serializers.conai_chatbot_conversation_mst_restful_serializer import ConaiChatbotConversationMstGetSerializer, ConaiChatbotConversationMstPostSerializer, \
    ConaiChatbotConversationMstPutSerializer, ConaiChatbotConversationMstDeleteSerializer

from chatbot.adapter.out.chatbot_conai_chatbot_conversation_mst_restful_db_adapter import ChatbotConaiChatbotConversationMstRestfulDbAdapter
from chatbot.application.port.out.chatbot_conai_chatbot_conversation_mst_restful_out_port import ChatbotConaiChatbotConversationMstRestfulOutPort, \
    ChatbotConaiChatbotConversationMstRestfulOutPortImpl
from chatbot.application.port._in.chatbot_conai_chatbot_conversation_mst_restful_in_port import ChatbotConaiChatbotConversationMstRestfulInPort, \
    ChatbotConaiChatbotConversationMstRestfulInPortImpl
from chatbot.application.service.chatbot_conai_chatbot_conversation_mst_restful_service import ChatbotConaiChatbotConversationMstRestfulService

# from .adapter._in.chatbot_restful_api_controller import ChatbotConaiChatbotConversationMstRestfulApiController

from chatbot.domain.CONAI_CHATBOT_MESSAGE_MST import ConaiChatbotMessageMst
from chatbot.serializers.conai_chatbot_message_mst_restful_serializer import ConaiChatbotMessageMstGetSerializer, ConaiChatbotMessageMstPostSerializer, \
    ConaiChatbotMessageMstPutSerializer, ConaiChatbotMessageMstDeleteSerializer

from chatbot.adapter.out.chatbot_conai_chatbot_message_mst_restful_db_adapter import ChatbotConaiChatbotMessageMstRestfulDbAdapter
from chatbot.application.port.out.chatbot_conai_chatbot_message_mst_restful_out_port import ChatbotConaiChatbotMessageMstRestfulOutPort, \
    ChatbotConaiChatbotMessageMstRestfulOutPortImpl
from chatbot.application.port._in.chatbot_conai_chatbot_message_mst_restful_in_port import ChatbotConaiChatbotMessageMstRestfulInPort, \
    ChatbotConaiChatbotMessageMstRestfulInPortImpl
from chatbot.application.service.chatbot_conai_chatbot_message_mst_restful_service import ChatbotConaiChatbotMessageMstRestfulService

# from .adapter._in.chatbot_restful_api_controller import ChatbotConaiChatbotMessageMstRestfulApiController

from chatbot.domain.CONAI_TAROT_SERVICE_CARDS_INFO_MST import ConaiTarotServiceCardsInfoMst
from chatbot.serializers.conai_tarot_service_cards_info_mst_restful_serializer import ConaiTarotServiceCardsInfoMstGetSerializer, ConaiTarotServiceCardsInfoMstPostSerializer, \
    ConaiTarotServiceCardsInfoMstPutSerializer, ConaiTarotServiceCardsInfoMstDeleteSerializer

from chatbot.adapter.out.chatbot_conai_tarot_service_cards_info_mst_restful_db_adapter import ChatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter
from chatbot.application.port.out.chatbot_conai_tarot_service_cards_info_mst_restful_out_port import ChatbotConaiTarotServiceCardsInfoMstRestfulOutPort, \
    ChatbotConaiTarotServiceCardsInfoMstRestfulOutPortImpl
from chatbot.application.port._in.chatbot_conai_tarot_service_cards_info_mst_restful_in_port import ChatbotConaiTarotServiceCardsInfoMstRestfulInPort, \
    ChatbotConaiTarotServiceCardsInfoMstRestfulInPortImpl
from chatbot.application.service.chatbot_conai_tarot_service_cards_info_mst_restful_service import ChatbotConaiTarotServiceCardsInfoMstRestfulService

# from .adapter._in.chatbot_restful_api_controller import ChatbotConaiTarotServiceCardsInfoMstRestfulApiController

from wired import ServiceRegistry

from chatbot.domain.CONAI_TAROT_SERVICE_DEFAULT_MESSAGE_MST import ConaiTarotServiceDefaultMessageMst
from chatbot.serializers.conai_tarot_service_default_message_mst_restful_serializer import ConaiTarotServiceDefaultMessageMstGetSerializer, ConaiTarotServiceDefaultMessageMstPostSerializer, \
    ConaiTarotServiceDefaultMessageMstPutSerializer, ConaiTarotServiceDefaultMessageMstDeleteSerializer

from chatbot.adapter.out.chatbot_conai_tarot_service_default_message_mst_restful_db_adapter import ChatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter
from chatbot.application.port.out.chatbot_conai_tarot_service_default_message_mst_restful_out_port import ChatbotConaiTarotServiceDefaultMessageMstRestfulOutPort, \
    ChatbotConaiTarotServiceDefaultMessageMstRestfulOutPortImpl
from chatbot.application.port._in.chatbot_conai_tarot_service_default_message_mst_restful_in_port import ChatbotConaiTarotServiceDefaultMessageMstRestfulInPort, \
    ChatbotConaiTarotServiceDefaultMessageMstRestfulInPortImpl
from chatbot.application.service.chatbot_conai_tarot_service_default_message_mst_restful_service import ChatbotConaiTarotServiceDefaultMessageMstRestfulService

# from .adapter._in.chatbot_restful_api_controller import ChatbotConaiTarotServiceDefaultMessageMstRestfulApiController

# Create the service registry
registry = ServiceRegistry()





def chatbot_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiChatbotGptParametersMst)
    # get_serializer = ConaiChatbotGptParametersMstGetSerializer() # container.get(ConaiChatbotGptParametersMstGetSerializer)
    # post_serializer = ConaiChatbotGptParametersMstPostSerializer() # container.get(ConaiChatbotGptParametersMstPostSerializer)
    # put_serializer = ConaiChatbotGptParametersMstPutSerializer() # container.get(ConaiChatbotGptParametersMstPutSerializer)
    # delete_serializer = ConaiChatbotGptParametersMstDeleteSerializer() # container.get(ConaiChatbotGptParametersMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return ChatbotConaiChatbotGptParametersMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def chatbot_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiChatbotGptParametersMstRestfulDbAdapter = container.get(ChatbotConaiChatbotGptParametersMstRestfulDbAdapter)

    return ChatbotConaiChatbotGptParametersMstRestfulOutPortImpl(chatbotConaiChatbotGptParametersMstRestfulDbAdapter=chatbotConaiChatbotGptParametersMstRestfulDbAdapter)

def chatbot_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return ChatbotConaiChatbotGptParametersMstRestfulInPortImpl()

def chatbot_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiChatbotGptParametersMstRestfulOutPort = container.get(ChatbotConaiChatbotGptParametersMstRestfulOutPort)
    chatbotConaiChatbotGptParametersMstRestfulInPort = container.get(ChatbotConaiChatbotGptParametersMstRestfulInPort)

    return ChatbotConaiChatbotGptParametersMstRestfulService(portInImpl=chatbotConaiChatbotGptParametersMstRestfulInPort,
                                          portOutImpl=chatbotConaiChatbotGptParametersMstRestfulOutPort)


# def chatbot_restful_controller_factory(container):
#     chatbotConaiChatbotGptParametersMstRestfulService = container.get(ChatbotConaiChatbotGptParametersMstRestfulService)
#
#     return ChatbotConaiChatbotGptParametersMstRestfulApiController(service=chatbotConaiChatbotGptParametersMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiChatbotGptParametersMst, ConaiChatbotGptParametersMst)
registry.register_factory(ConaiChatbotGptParametersMstGetSerializer, ConaiChatbotGptParametersMstGetSerializer)
registry.register_factory(ConaiChatbotGptParametersMstPostSerializer, ConaiChatbotGptParametersMstPostSerializer)
registry.register_factory(ConaiChatbotGptParametersMstPutSerializer, ConaiChatbotGptParametersMstPutSerializer)
registry.register_factory(ConaiChatbotGptParametersMstDeleteSerializer, ConaiChatbotGptParametersMstDeleteSerializer)
# Adapter
registry.register_factory(chatbot_restful_db_adapter_factory, ChatbotConaiChatbotGptParametersMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(chatbot_restful_out_port_factory, ChatbotConaiChatbotGptParametersMstRestfulOutPort)
registry.register_factory(chatbot_restful_in_port_factory, ChatbotConaiChatbotGptParametersMstRestfulInPort)
# Service
registry.register_factory(chatbot_restful_service_factory, ChatbotConaiChatbotGptParametersMstRestfulService)
# Controller
# registry.register_factory(ChatbotConaiChatbotGptParametersMstRestfulApiController, chatbot_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(ChatbotConaiChatbotGptParametersMstRestfulDbAdapter) ==> {registry.find_factory(ChatbotConaiChatbotGptParametersMstRestfulDbAdapter)}")



def chatbot_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiChatbotConversationHistoryMst)
    # get_serializer = ConaiChatbotConversationHistoryMstGetSerializer() # container.get(ConaiChatbotConversationHistoryMstGetSerializer)
    # post_serializer = ConaiChatbotConversationHistoryMstPostSerializer() # container.get(ConaiChatbotConversationHistoryMstPostSerializer)
    # put_serializer = ConaiChatbotConversationHistoryMstPutSerializer() # container.get(ConaiChatbotConversationHistoryMstPutSerializer)
    # delete_serializer = ConaiChatbotConversationHistoryMstDeleteSerializer() # container.get(ConaiChatbotConversationHistoryMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return ChatbotConaiChatbotConversationHistoryMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def chatbot_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter = container.get(ChatbotConaiChatbotConversationHistoryMstRestfulDbAdapter)

    return ChatbotConaiChatbotConversationHistoryMstRestfulOutPortImpl(chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter=chatbotConaiChatbotConversationHistoryMstRestfulDbAdapter)

def chatbot_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return ChatbotConaiChatbotConversationHistoryMstRestfulInPortImpl()

def chatbot_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiChatbotConversationHistoryMstRestfulOutPort = container.get(ChatbotConaiChatbotConversationHistoryMstRestfulOutPort)
    chatbotConaiChatbotConversationHistoryMstRestfulInPort = container.get(ChatbotConaiChatbotConversationHistoryMstRestfulInPort)

    return ChatbotConaiChatbotConversationHistoryMstRestfulService(portInImpl=chatbotConaiChatbotConversationHistoryMstRestfulInPort,
                                          portOutImpl=chatbotConaiChatbotConversationHistoryMstRestfulOutPort)


# def chatbot_restful_controller_factory(container):
#     chatbotConaiChatbotConversationHistoryMstRestfulService = container.get(ChatbotConaiChatbotConversationHistoryMstRestfulService)
#
#     return ChatbotConaiChatbotConversationHistoryMstRestfulApiController(service=chatbotConaiChatbotConversationHistoryMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiChatbotConversationHistoryMst, ConaiChatbotConversationHistoryMst)
registry.register_factory(ConaiChatbotConversationHistoryMstGetSerializer, ConaiChatbotConversationHistoryMstGetSerializer)
registry.register_factory(ConaiChatbotConversationHistoryMstPostSerializer, ConaiChatbotConversationHistoryMstPostSerializer)
registry.register_factory(ConaiChatbotConversationHistoryMstPutSerializer, ConaiChatbotConversationHistoryMstPutSerializer)
registry.register_factory(ConaiChatbotConversationHistoryMstDeleteSerializer, ConaiChatbotConversationHistoryMstDeleteSerializer)
# Adapter
registry.register_factory(chatbot_restful_db_adapter_factory, ChatbotConaiChatbotConversationHistoryMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(chatbot_restful_out_port_factory, ChatbotConaiChatbotConversationHistoryMstRestfulOutPort)
registry.register_factory(chatbot_restful_in_port_factory, ChatbotConaiChatbotConversationHistoryMstRestfulInPort)
# Service
registry.register_factory(chatbot_restful_service_factory, ChatbotConaiChatbotConversationHistoryMstRestfulService)
# Controller
# registry.register_factory(ChatbotConaiChatbotConversationHistoryMstRestfulApiController, chatbot_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(ChatbotConaiChatbotConversationHistoryMstRestfulDbAdapter) ==> {registry.find_factory(ChatbotConaiChatbotConversationHistoryMstRestfulDbAdapter)}")




def chatbot_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiChatbotConversationMst)
    # get_serializer = ConaiChatbotConversationMstGetSerializer() # container.get(ConaiChatbotConversationMstGetSerializer)
    # post_serializer = ConaiChatbotConversationMstPostSerializer() # container.get(ConaiChatbotConversationMstPostSerializer)
    # put_serializer = ConaiChatbotConversationMstPutSerializer() # container.get(ConaiChatbotConversationMstPutSerializer)
    # delete_serializer = ConaiChatbotConversationMstDeleteSerializer() # container.get(ConaiChatbotConversationMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return ChatbotConaiChatbotConversationMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def chatbot_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiChatbotConversationMstRestfulDbAdapter = container.get(ChatbotConaiChatbotConversationMstRestfulDbAdapter)

    return ChatbotConaiChatbotConversationMstRestfulOutPortImpl(chatbotConaiChatbotConversationMstRestfulDbAdapter=chatbotConaiChatbotConversationMstRestfulDbAdapter)

def chatbot_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return ChatbotConaiChatbotConversationMstRestfulInPortImpl()

def chatbot_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiChatbotConversationMstRestfulOutPort = container.get(ChatbotConaiChatbotConversationMstRestfulOutPort)
    chatbotConaiChatbotConversationMstRestfulInPort = container.get(ChatbotConaiChatbotConversationMstRestfulInPort)

    return ChatbotConaiChatbotConversationMstRestfulService(portInImpl=chatbotConaiChatbotConversationMstRestfulInPort,
                                          portOutImpl=chatbotConaiChatbotConversationMstRestfulOutPort)


# def chatbot_restful_controller_factory(container):
#     chatbotConaiChatbotConversationMstRestfulService = container.get(ChatbotConaiChatbotConversationMstRestfulService)
#
#     return ChatbotConaiChatbotConversationMstRestfulApiController(service=chatbotConaiChatbotConversationMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiChatbotConversationMst, ConaiChatbotConversationMst)
registry.register_factory(ConaiChatbotConversationMstGetSerializer, ConaiChatbotConversationMstGetSerializer)
registry.register_factory(ConaiChatbotConversationMstPostSerializer, ConaiChatbotConversationMstPostSerializer)
registry.register_factory(ConaiChatbotConversationMstPutSerializer, ConaiChatbotConversationMstPutSerializer)
registry.register_factory(ConaiChatbotConversationMstDeleteSerializer, ConaiChatbotConversationMstDeleteSerializer)
# Adapter
registry.register_factory(chatbot_restful_db_adapter_factory, ChatbotConaiChatbotConversationMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(chatbot_restful_out_port_factory, ChatbotConaiChatbotConversationMstRestfulOutPort)
registry.register_factory(chatbot_restful_in_port_factory, ChatbotConaiChatbotConversationMstRestfulInPort)
# Service
registry.register_factory(chatbot_restful_service_factory, ChatbotConaiChatbotConversationMstRestfulService)
# Controller
# registry.register_factory(ChatbotConaiChatbotConversationMstRestfulApiController, chatbot_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(ChatbotConaiChatbotConversationMstRestfulDbAdapter) ==> {registry.find_factory(ChatbotConaiChatbotConversationMstRestfulDbAdapter)}")




def chatbot_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiChatbotMessageMst)
    # get_serializer = ConaiChatbotMessageMstGetSerializer() # container.get(ConaiChatbotMessageMstGetSerializer)
    # post_serializer = ConaiChatbotMessageMstPostSerializer() # container.get(ConaiChatbotMessageMstPostSerializer)
    # put_serializer = ConaiChatbotMessageMstPutSerializer() # container.get(ConaiChatbotMessageMstPutSerializer)
    # delete_serializer = ConaiChatbotMessageMstDeleteSerializer() # container.get(ConaiChatbotMessageMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return ChatbotConaiChatbotMessageMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def chatbot_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiChatbotMessageMstRestfulDbAdapter = container.get(ChatbotConaiChatbotMessageMstRestfulDbAdapter)

    return ChatbotConaiChatbotMessageMstRestfulOutPortImpl(chatbotConaiChatbotMessageMstRestfulDbAdapter=chatbotConaiChatbotMessageMstRestfulDbAdapter)

def chatbot_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return ChatbotConaiChatbotMessageMstRestfulInPortImpl()

def chatbot_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiChatbotMessageMstRestfulOutPort = container.get(ChatbotConaiChatbotMessageMstRestfulOutPort)
    chatbotConaiChatbotMessageMstRestfulInPort = container.get(ChatbotConaiChatbotMessageMstRestfulInPort)

    return ChatbotConaiChatbotMessageMstRestfulService(portInImpl=chatbotConaiChatbotMessageMstRestfulInPort,
                                          portOutImpl=chatbotConaiChatbotMessageMstRestfulOutPort)


# def chatbot_restful_controller_factory(container):
#     chatbotConaiChatbotMessageMstRestfulService = container.get(ChatbotConaiChatbotMessageMstRestfulService)
#
#     return ChatbotConaiChatbotMessageMstRestfulApiController(service=chatbotConaiChatbotMessageMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiChatbotMessageMst, ConaiChatbotMessageMst)
registry.register_factory(ConaiChatbotMessageMstGetSerializer, ConaiChatbotMessageMstGetSerializer)
registry.register_factory(ConaiChatbotMessageMstPostSerializer, ConaiChatbotMessageMstPostSerializer)
registry.register_factory(ConaiChatbotMessageMstPutSerializer, ConaiChatbotMessageMstPutSerializer)
registry.register_factory(ConaiChatbotMessageMstDeleteSerializer, ConaiChatbotMessageMstDeleteSerializer)
# Adapter
registry.register_factory(chatbot_restful_db_adapter_factory, ChatbotConaiChatbotMessageMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(chatbot_restful_out_port_factory, ChatbotConaiChatbotMessageMstRestfulOutPort)
registry.register_factory(chatbot_restful_in_port_factory, ChatbotConaiChatbotMessageMstRestfulInPort)
# Service
registry.register_factory(chatbot_restful_service_factory, ChatbotConaiChatbotMessageMstRestfulService)
# Controller
# registry.register_factory(ChatbotConaiChatbotMessageMstRestfulApiController, chatbot_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(ChatbotConaiChatbotMessageMstRestfulDbAdapter) ==> {registry.find_factory(ChatbotConaiChatbotMessageMstRestfulDbAdapter)}")


def chatbot_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiTarotServiceCardsInfoMst)
    # get_serializer = ConaiTarotServiceCardsInfoMstGetSerializer() # container.get(ConaiTarotServiceCardsInfoMstGetSerializer)
    # post_serializer = ConaiTarotServiceCardsInfoMstPostSerializer() # container.get(ConaiTarotServiceCardsInfoMstPostSerializer)
    # put_serializer = ConaiTarotServiceCardsInfoMstPutSerializer() # container.get(ConaiTarotServiceCardsInfoMstPutSerializer)
    # delete_serializer = ConaiTarotServiceCardsInfoMstDeleteSerializer() # container.get(ConaiTarotServiceCardsInfoMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return ChatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def chatbot_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter = container.get(ChatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter)

    return ChatbotConaiTarotServiceCardsInfoMstRestfulOutPortImpl(chatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter=chatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter)

def chatbot_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return ChatbotConaiTarotServiceCardsInfoMstRestfulInPortImpl()

def chatbot_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiTarotServiceCardsInfoMstRestfulOutPort = container.get(ChatbotConaiTarotServiceCardsInfoMstRestfulOutPort)
    chatbotConaiTarotServiceCardsInfoMstRestfulInPort = container.get(ChatbotConaiTarotServiceCardsInfoMstRestfulInPort)

    return ChatbotConaiTarotServiceCardsInfoMstRestfulService(portInImpl=chatbotConaiTarotServiceCardsInfoMstRestfulInPort,
                                          portOutImpl=chatbotConaiTarotServiceCardsInfoMstRestfulOutPort)


# def chatbot_restful_controller_factory(container):
#     chatbotConaiTarotServiceCardsInfoMstRestfulService = container.get(ChatbotConaiTarotServiceCardsInfoMstRestfulService)
#
#     return ChatbotConaiTarotServiceCardsInfoMstRestfulApiController(service=chatbotConaiTarotServiceCardsInfoMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiTarotServiceCardsInfoMst, ConaiTarotServiceCardsInfoMst)
registry.register_factory(ConaiTarotServiceCardsInfoMstGetSerializer, ConaiTarotServiceCardsInfoMstGetSerializer)
registry.register_factory(ConaiTarotServiceCardsInfoMstPostSerializer, ConaiTarotServiceCardsInfoMstPostSerializer)
registry.register_factory(ConaiTarotServiceCardsInfoMstPutSerializer, ConaiTarotServiceCardsInfoMstPutSerializer)
registry.register_factory(ConaiTarotServiceCardsInfoMstDeleteSerializer, ConaiTarotServiceCardsInfoMstDeleteSerializer)
# Adapter
registry.register_factory(chatbot_restful_db_adapter_factory, ChatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(chatbot_restful_out_port_factory, ChatbotConaiTarotServiceCardsInfoMstRestfulOutPort)
registry.register_factory(chatbot_restful_in_port_factory, ChatbotConaiTarotServiceCardsInfoMstRestfulInPort)
# Service
registry.register_factory(chatbot_restful_service_factory, ChatbotConaiTarotServiceCardsInfoMstRestfulService)
# Controller
# registry.register_factory(ChatbotConaiTarotServiceCardsInfoMstRestfulApiController, chatbot_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(ChatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter) ==> {registry.find_factory(ChatbotConaiTarotServiceCardsInfoMstRestfulDbAdapter)}")



def chatbot_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiTarotServiceDefaultMessageMst)
    # get_serializer = ConaiTarotServiceDefaultMessageMstGetSerializer() # container.get(ConaiTarotServiceDefaultMessageMstGetSerializer)
    # post_serializer = ConaiTarotServiceDefaultMessageMstPostSerializer() # container.get(ConaiTarotServiceDefaultMessageMstPostSerializer)
    # put_serializer = ConaiTarotServiceDefaultMessageMstPutSerializer() # container.get(ConaiTarotServiceDefaultMessageMstPutSerializer)
    # delete_serializer = ConaiTarotServiceDefaultMessageMstDeleteSerializer() # container.get(ConaiTarotServiceDefaultMessageMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return ChatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def chatbot_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter = container.get(ChatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter)

    return ChatbotConaiTarotServiceDefaultMessageMstRestfulOutPortImpl(chatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter=chatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter)

def chatbot_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return ChatbotConaiTarotServiceDefaultMessageMstRestfulInPortImpl()

def chatbot_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    chatbotConaiTarotServiceDefaultMessageMstRestfulOutPort = container.get(ChatbotConaiTarotServiceDefaultMessageMstRestfulOutPort)
    chatbotConaiTarotServiceDefaultMessageMstRestfulInPort = container.get(ChatbotConaiTarotServiceDefaultMessageMstRestfulInPort)

    return ChatbotConaiTarotServiceDefaultMessageMstRestfulService(portInImpl=chatbotConaiTarotServiceDefaultMessageMstRestfulInPort,
                                          portOutImpl=chatbotConaiTarotServiceDefaultMessageMstRestfulOutPort)


# def chatbot_restful_controller_factory(container):
#     chatbotConaiTarotServiceDefaultMessageMstRestfulService = container.get(ChatbotConaiTarotServiceDefaultMessageMstRestfulService)
#
#     return ChatbotConaiTarotServiceDefaultMessageMstRestfulApiController(service=chatbotConaiTarotServiceDefaultMessageMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiTarotServiceDefaultMessageMst, ConaiTarotServiceDefaultMessageMst)
registry.register_factory(ConaiTarotServiceDefaultMessageMstGetSerializer, ConaiTarotServiceDefaultMessageMstGetSerializer)
registry.register_factory(ConaiTarotServiceDefaultMessageMstPostSerializer, ConaiTarotServiceDefaultMessageMstPostSerializer)
registry.register_factory(ConaiTarotServiceDefaultMessageMstPutSerializer, ConaiTarotServiceDefaultMessageMstPutSerializer)
registry.register_factory(ConaiTarotServiceDefaultMessageMstDeleteSerializer, ConaiTarotServiceDefaultMessageMstDeleteSerializer)
# Adapter
registry.register_factory(chatbot_restful_db_adapter_factory, ChatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(chatbot_restful_out_port_factory, ChatbotConaiTarotServiceDefaultMessageMstRestfulOutPort)
registry.register_factory(chatbot_restful_in_port_factory, ChatbotConaiTarotServiceDefaultMessageMstRestfulInPort)
# Service
registry.register_factory(chatbot_restful_service_factory, ChatbotConaiTarotServiceDefaultMessageMstRestfulService)
# Controller
# registry.register_factory(ChatbotConaiTarotServiceDefaultMessageMstRestfulApiController, chatbot_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(ChatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter) ==> {registry.find_factory(ChatbotConaiTarotServiceDefaultMessageMstRestfulDbAdapter)}")
container = registry.create_container()
print(f"container ==> {container}")
print(f"container.__dict__ ==> {container.__dict__}")