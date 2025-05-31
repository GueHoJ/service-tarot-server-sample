from wired import ServiceRegistry

from servicelog.domain.CONAI_TAROT_SERVICE_LOG_MST import ConaiTarotServiceLogMst
from servicelog.serializers.conai_tarot_service_log_mst_restful_serializer import ConaiTarotServiceLogMstGetSerializer, ConaiTarotServiceLogMstPostSerializer, \
    ConaiTarotServiceLogMstPutSerializer, ConaiTarotServiceLogMstDeleteSerializer

from servicelog.adapter.out.servicelog_conai_tarot_service_log_mst_restful_db_adapter import ServicelogConaiTarotServiceLogMstRestfulDbAdapter
from servicelog.application.port.out.servicelog_conai_tarot_service_log_mst_restful_out_port import ServicelogConaiTarotServiceLogMstRestfulOutPort, \
    ServicelogConaiTarotServiceLogMstRestfulOutPortImpl
from servicelog.application.port._in.servicelog_conai_tarot_service_log_mst_restful_in_port import ServicelogConaiTarotServiceLogMstRestfulInPort, \
    ServicelogConaiTarotServiceLogMstRestfulInPortImpl
from servicelog.application.service.servicelog_conai_tarot_service_log_mst_restful_service import ServicelogConaiTarotServiceLogMstRestfulService

# from .adapter._in.servicelog_restful_api_controller import ServicelogConaiTarotServiceLogMstRestfulApiController

# Create the service registry
registry = ServiceRegistry()



def servicelog_restful_db_adapter_factory(container):
    # Resolve AnotherService from the container
    # db_object = container.get(ConaiTarotServiceLogMst)
    # get_serializer = ConaiTarotServiceLogMstGetSerializer() # container.get(ConaiTarotServiceLogMstGetSerializer)
    # post_serializer = ConaiTarotServiceLogMstPostSerializer() # container.get(ConaiTarotServiceLogMstPostSerializer)
    # put_serializer = ConaiTarotServiceLogMstPutSerializer() # container.get(ConaiTarotServiceLogMstPutSerializer)
    # delete_serializer = ConaiTarotServiceLogMstDeleteSerializer() # container.get(ConaiTarotServiceLogMstDeleteSerializer)

    # Assume the configuration is available here
    # config_value = "some_config_value"

    # Return an instance of MyService with dependencies
    return ServicelogConaiTarotServiceLogMstRestfulDbAdapter(
        # db_object_class=db_object,
        # get_serializer=get_serializer,
        # post_serializer=post_serializer,
        # put_serializer=put_serializer,
        # delete_serializer=delete_serializer
                                            )


def servicelog_restful_out_port_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    servicelogConaiTarotServiceLogMstRestfulDbAdapter = container.get(ServicelogConaiTarotServiceLogMstRestfulDbAdapter)

    return ServicelogConaiTarotServiceLogMstRestfulOutPortImpl(servicelogConaiTarotServiceLogMstRestfulDbAdapter=servicelogConaiTarotServiceLogMstRestfulDbAdapter)

def servicelog_restful_in_port_factory(container):
    # No dependencies required, so just return an instance
    return ServicelogConaiTarotServiceLogMstRestfulInPortImpl()

def servicelog_restful_service_factory(container):
    # Resolve AbstractService, which will give us an instance of ConcreteServiceA
    servicelogConaiTarotServiceLogMstRestfulOutPort = container.get(ServicelogConaiTarotServiceLogMstRestfulOutPort)
    servicelogConaiTarotServiceLogMstRestfulInPort = container.get(ServicelogConaiTarotServiceLogMstRestfulInPort)

    return ServicelogConaiTarotServiceLogMstRestfulService(portInImpl=servicelogConaiTarotServiceLogMstRestfulInPort,
                                          portOutImpl=servicelogConaiTarotServiceLogMstRestfulOutPort)


# def servicelog_restful_controller_factory(container):
#     servicelogConaiTarotServiceLogMstRestfulService = container.get(ServicelogConaiTarotServiceLogMstRestfulService)
#
#     return ServicelogConaiTarotServiceLogMstRestfulApiController(service=servicelogConaiTarotServiceLogMstRestfulService)

# Register the services in the registry
# registry.register_factory(class or function, key)
# construct key class by calling class or function
# ORM, Serializer
registry.register_factory(ConaiTarotServiceLogMst, ConaiTarotServiceLogMst)
registry.register_factory(ConaiTarotServiceLogMstGetSerializer, ConaiTarotServiceLogMstGetSerializer)
registry.register_factory(ConaiTarotServiceLogMstPostSerializer, ConaiTarotServiceLogMstPostSerializer)
registry.register_factory(ConaiTarotServiceLogMstPutSerializer, ConaiTarotServiceLogMstPutSerializer)
registry.register_factory(ConaiTarotServiceLogMstDeleteSerializer, ConaiTarotServiceLogMstDeleteSerializer)
# Adapter
registry.register_factory(servicelog_restful_db_adapter_factory, ServicelogConaiTarotServiceLogMstRestfulDbAdapter)
# Out/In Port Interface
registry.register_factory(servicelog_restful_out_port_factory, ServicelogConaiTarotServiceLogMstRestfulOutPort)
registry.register_factory(servicelog_restful_in_port_factory, ServicelogConaiTarotServiceLogMstRestfulInPort)
# Service
registry.register_factory(servicelog_restful_service_factory, ServicelogConaiTarotServiceLogMstRestfulService)
# Controller
# registry.register_factory(ServicelogConaiTarotServiceLogMstRestfulApiController, servicelog_restful_controller_factory)

print(f"registry ==> {registry}")
print(f"registry.find_factory(ServicelogConaiTarotServiceLogMstRestfulDbAdapter) ==> {registry.find_factory(ServicelogConaiTarotServiceLogMstRestfulDbAdapter)}")
container = registry.create_container()
print(f"container ==> {container}")
print(f"container.__dict__ ==> {container.__dict__}")