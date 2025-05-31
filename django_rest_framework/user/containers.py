from wired import ServiceRegistry

from user.domain.CONAI_USER_MST import ConaiUserMst
from user.serializers.conai_user_mst_restful_serializer import ConaiUserMstGetSerializer, ConaiUserMstPostSerializer, \
    ConaiUserMstPutSerializer, ConaiUserMstDeleteSerializer

from user.adapter.out.user_conai_user_mst_restful_db_adapter import UserConaiUserMstRestfulDbAdapter
from user.application.port.out.user_conai_user_mst_restful_out_port import UserConaiUserMstRestfulOutPort, \
    UserConaiUserMstRestfulOutPortImpl
from user.application.port._in.user_conai_user_mst_restful_in_port import UserConaiUserMstRestfulInPort, \
    UserConaiUserMstRestfulInPortImpl
from user.application.service.user_conai_user_mst_restful_service import UserConaiUserMstRestfulService

# from .adapter._in.user_conai_user_mst_restful_api_controller import UserConaiUserMstRestfulApiController

from wired import ServiceRegistry

from user.domain.CONAI_TAROT_SERVICE_USER_MST import ConaiTarotServiceUserMst
from user.serializers.conai_tarot_service_user_mst_restful_serializer import ConaiTarotServiceUserMstGetSerializer, ConaiTarotServiceUserMstPostSerializer, \
    ConaiTarotServiceUserMstPutSerializer, ConaiTarotServiceUserMstDeleteSerializer

from user.adapter.out.user_conai_tarot_service_user_mst_restful_db_adapter import UserConaiTarotServiceUserMstRestfulDbAdapter
from user.application.port.out.user_conai_tarot_service_user_mst_restful_out_port import UserConaiTarotServiceUserMstRestfulOutPort, \
    UserConaiTarotServiceUserMstRestfulOutPortImpl
from user.application.port._in.user_conai_tarot_service_user_mst_restful_in_port import UserConaiTarotServiceUserMstRestfulInPort, \
    UserConaiTarotServiceUserMstRestfulInPortImpl
from user.application.service.user_conai_tarot_service_user_mst_restful_service import UserConaiTarotServiceUserMstRestfulService

# from .adapter._in.user_restful_api_controller import UserConaiTarotServiceUserMstRestfulApiController

# Create the service registry
registry = ServiceRegistry()



def user_conai_user_mst_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiUserMst)
    # get_serializer = ConaiUserMstGetSerializer() # container.get(ConaiUserMstGetSerializer)
    # post_serializer = ConaiUserMstPostSerializer() # container.get(ConaiUserMstPostSerializer)
    # put_serializer = ConaiUserMstPutSerializer() # container.get(ConaiUserMstPutSerializer)
    # delete_serializer = ConaiUserMstDeleteSerializer() # container.get(ConaiUserMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return UserConaiUserMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def user_conai_user_mst_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    userConaiUserMstRestfulDbAdapter = container.get(UserConaiUserMstRestfulDbAdapter)

    return UserConaiUserMstRestfulOutPortImpl(userConaiUserMstRestfulDbAdapter=userConaiUserMstRestfulDbAdapter)

def user_conai_user_mst_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return UserConaiUserMstRestfulInPortImpl()

def user_conai_user_mst_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    userConaiUserMstRestfulOutPort = container.get(UserConaiUserMstRestfulOutPort)
    userConaiUserMstRestfulInPort = container.get(UserConaiUserMstRestfulInPort)

    return UserConaiUserMstRestfulService(portInImpl=userConaiUserMstRestfulInPort,
                                          portOutImpl=userConaiUserMstRestfulOutPort)


# def user_conai_user_mst_restful_controller_factory(container):
#     userConaiUserMstRestfulService = container.get(UserConaiUserMstRestfulService)
#
#     return UserConaiUserMstRestfulApiController(service=userConaiUserMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiUserMst, ConaiUserMst)
registry.register_factory(ConaiUserMstGetSerializer, ConaiUserMstGetSerializer)
registry.register_factory(ConaiUserMstPostSerializer, ConaiUserMstPostSerializer)
registry.register_factory(ConaiUserMstPutSerializer, ConaiUserMstPutSerializer)
registry.register_factory(ConaiUserMstDeleteSerializer, ConaiUserMstDeleteSerializer)
# Adapter
registry.register_factory(user_conai_user_mst_restful_db_adapter_factory, UserConaiUserMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(user_conai_user_mst_restful_out_port_factory, UserConaiUserMstRestfulOutPort)
registry.register_factory(user_conai_user_mst_restful_in_port_factory, UserConaiUserMstRestfulInPort)
# Service
registry.register_factory(user_conai_user_mst_restful_service_factory, UserConaiUserMstRestfulService)
# Controller
# registry.register_factory(UserConaiUserMstRestfulApiController, user_conai_user_mst_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(UserConaiUserMstRestfulDbAdapter) ==> {registry.find_factory(UserConaiUserMstRestfulDbAdapter)}")



def user_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiTarotServiceUserMst)
    # get_serializer = ConaiTarotServiceUserMstGetSerializer() # container.get(ConaiTarotServiceUserMstGetSerializer)
    # post_serializer = ConaiTarotServiceUserMstPostSerializer() # container.get(ConaiTarotServiceUserMstPostSerializer)
    # put_serializer = ConaiTarotServiceUserMstPutSerializer() # container.get(ConaiTarotServiceUserMstPutSerializer)
    # delete_serializer = ConaiTarotServiceUserMstDeleteSerializer() # container.get(ConaiTarotServiceUserMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return UserConaiTarotServiceUserMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def user_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    userConaiTarotServiceUserMstRestfulDbAdapter = container.get(UserConaiTarotServiceUserMstRestfulDbAdapter)

    return UserConaiTarotServiceUserMstRestfulOutPortImpl(userConaiTarotServiceUserMstRestfulDbAdapter=userConaiTarotServiceUserMstRestfulDbAdapter)

def user_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return UserConaiTarotServiceUserMstRestfulInPortImpl()

def user_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    userConaiTarotServiceUserMstRestfulOutPort = container.get(UserConaiTarotServiceUserMstRestfulOutPort)
    userConaiTarotServiceUserMstRestfulInPort = container.get(UserConaiTarotServiceUserMstRestfulInPort)

    return UserConaiTarotServiceUserMstRestfulService(portInImpl=userConaiTarotServiceUserMstRestfulInPort,
                                          portOutImpl=userConaiTarotServiceUserMstRestfulOutPort)


# def user_restful_controller_factory(container):
#     userConaiTarotServiceUserMstRestfulService = container.get(UserConaiTarotServiceUserMstRestfulService)
#
#     return UserConaiTarotServiceUserMstRestfulApiController(service=userConaiTarotServiceUserMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiTarotServiceUserMst, ConaiTarotServiceUserMst)
registry.register_factory(ConaiTarotServiceUserMstGetSerializer, ConaiTarotServiceUserMstGetSerializer)
registry.register_factory(ConaiTarotServiceUserMstPostSerializer, ConaiTarotServiceUserMstPostSerializer)
registry.register_factory(ConaiTarotServiceUserMstPutSerializer, ConaiTarotServiceUserMstPutSerializer)
registry.register_factory(ConaiTarotServiceUserMstDeleteSerializer, ConaiTarotServiceUserMstDeleteSerializer)
# Adapter
registry.register_factory(user_restful_db_adapter_factory, UserConaiTarotServiceUserMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(user_restful_out_port_factory, UserConaiTarotServiceUserMstRestfulOutPort)
registry.register_factory(user_restful_in_port_factory, UserConaiTarotServiceUserMstRestfulInPort)
# Service
registry.register_factory(user_restful_service_factory, UserConaiTarotServiceUserMstRestfulService)
# Controller
# registry.register_factory(UserConaiTarotServiceUserMstRestfulApiController, user_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(UserConaiTarotServiceUserMstRestfulDbAdapter) ==> {registry.find_factory(UserConaiTarotServiceUserMstRestfulDbAdapter)}")
container = registry.create_container()
print(f"container ==> {container}")
print(f"container.__dict__ ==> {container.__dict__}")