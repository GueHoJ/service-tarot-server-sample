from wired import ServiceRegistry

from servicetoken.domain.CONAI_TAROT_SERVICE_USER_TOKEN_MST import ConaiTarotServiceUserTokenMst
from servicetoken.serializers.conai_tarot_service_user_token_mst_restful_serializer import ConaiTarotServiceUserTokenMstGetSerializer, ConaiTarotServiceUserTokenMstPostSerializer, \
    ConaiTarotServiceUserTokenMstPutSerializer, ConaiTarotServiceUserTokenMstDeleteSerializer

from servicetoken.adapter.out.servicetoken_conai_tarot_service_user_token_mst_restful_db_adapter import ServicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter
from servicetoken.application.port.out.servicetoken_conai_tarot_service_user_token_mst_restful_out_port import ServicetokenConaiTarotServiceUserTokenMstRestfulOutPort, \
    ServicetokenConaiTarotServiceUserTokenMstRestfulOutPortImpl
from servicetoken.application.port._in.servicetoken_conai_tarot_service_user_token_mst_restful_in_port import ServicetokenConaiTarotServiceUserTokenMstRestfulInPort, \
    ServicetokenConaiTarotServiceUserTokenMstRestfulInPortImpl
from servicetoken.application.service.servicetoken_conai_tarot_service_user_token_mst_restful_service import ServicetokenConaiTarotServiceUserTokenMstRestfulService

# from .adapter._in.servicetoken_restful_api_controller import ServicetokenConaiTarotServiceUserTokenMstRestfulApiController

# Create the service registry
registry = ServiceRegistry()



def servicetoken_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiTarotServiceUserTokenMst)
    # get_serializer = ConaiTarotServiceUserTokenMstGetSerializer() # container.get(ConaiTarotServiceUserTokenMstGetSerializer)
    # post_serializer = ConaiTarotServiceUserTokenMstPostSerializer() # container.get(ConaiTarotServiceUserTokenMstPostSerializer)
    # put_serializer = ConaiTarotServiceUserTokenMstPutSerializer() # container.get(ConaiTarotServiceUserTokenMstPutSerializer)
    # delete_serializer = ConaiTarotServiceUserTokenMstDeleteSerializer() # container.get(ConaiTarotServiceUserTokenMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return ServicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def servicetoken_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter = container.get(ServicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter)

    return ServicetokenConaiTarotServiceUserTokenMstRestfulOutPortImpl(servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter=servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter)

def servicetoken_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return ServicetokenConaiTarotServiceUserTokenMstRestfulInPortImpl()

def servicetoken_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    servicetokenConaiTarotServiceUserTokenMstRestfulOutPort = container.get(ServicetokenConaiTarotServiceUserTokenMstRestfulOutPort)
    servicetokenConaiTarotServiceUserTokenMstRestfulInPort = container.get(ServicetokenConaiTarotServiceUserTokenMstRestfulInPort)

    return ServicetokenConaiTarotServiceUserTokenMstRestfulService(portInImpl=servicetokenConaiTarotServiceUserTokenMstRestfulInPort,
                                          portOutImpl=servicetokenConaiTarotServiceUserTokenMstRestfulOutPort)


# def servicetoken_restful_controller_factory(container):
#     servicetokenConaiTarotServiceUserTokenMstRestfulService = container.get(ServicetokenConaiTarotServiceUserTokenMstRestfulService)
#
#     return ServicetokenConaiTarotServiceUserTokenMstRestfulApiController(service=servicetokenConaiTarotServiceUserTokenMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiTarotServiceUserTokenMst, ConaiTarotServiceUserTokenMst)
registry.register_factory(ConaiTarotServiceUserTokenMstGetSerializer, ConaiTarotServiceUserTokenMstGetSerializer)
registry.register_factory(ConaiTarotServiceUserTokenMstPostSerializer, ConaiTarotServiceUserTokenMstPostSerializer)
registry.register_factory(ConaiTarotServiceUserTokenMstPutSerializer, ConaiTarotServiceUserTokenMstPutSerializer)
registry.register_factory(ConaiTarotServiceUserTokenMstDeleteSerializer, ConaiTarotServiceUserTokenMstDeleteSerializer)
# Adapter
registry.register_factory(servicetoken_restful_db_adapter_factory, ServicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(servicetoken_restful_out_port_factory, ServicetokenConaiTarotServiceUserTokenMstRestfulOutPort)
registry.register_factory(servicetoken_restful_in_port_factory, ServicetokenConaiTarotServiceUserTokenMstRestfulInPort)
# Service
registry.register_factory(servicetoken_restful_service_factory, ServicetokenConaiTarotServiceUserTokenMstRestfulService)
# Controller
# registry.register_factory(ServicetokenConaiTarotServiceUserTokenMstRestfulApiController, servicetoken_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(ServicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter) ==> {registry.find_factory(ServicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter)}")
container = registry.create_container()
print(f"container ==> {container}")
print(f"container.__dict__ ==> {container.__dict__}")