from abc import ABC, abstractmethod


class ServicelogConaiTarotServiceLogMstRestfulInPort(ABC):
    """
    # CLASS : ServicelogConaiTarotServiceLogMstRestfulInPort
    # AUTHOR : conai
    # TIME : 2025. 1. 15. conai
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2025. 1. 15.          conai          최초 생성
    """

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_in_port(self, *args, **kwargs):
        pass

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_in_port_get(self, *args, **kwargs):
        pass

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_in_port_post(self, *args, **kwargs):
        pass

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_in_port_put(self, *args, **kwargs):
        pass

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_in_port_delete(self, *args, **kwargs):
        pass


class ServicelogConaiTarotServiceLogMstRestfulInPortImpl(ServicelogConaiTarotServiceLogMstRestfulInPort):

    def __init__(self):
        pass

    def servicelog_conai_tarot_service_log_mst_restful_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_in_port request params ==> {args[1]}")
        result = args[1]

        return result

    def servicelog_conai_tarot_service_log_mst_restful_in_port_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_in_port_get request params ==> {args[1]}")
        result = args[1]

        return result

    def servicelog_conai_tarot_service_log_mst_restful_in_port_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_in_port_post request params ==> {args[1]}")
        result = args[1]

        return result

    def servicelog_conai_tarot_service_log_mst_restful_in_port_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_in_port_put request params ==> {args[1]}")
        result = args[1]

        return result

    def servicelog_conai_tarot_service_log_mst_restful_in_port_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_in_port_delete request params ==> {args[1]}")
        result = args[1]

        return result
