from abc import ABC, abstractmethod

from ....adapter.out.servicelog_conai_tarot_service_log_mst_restful_db_adapter import ServicelogConaiTarotServiceLogMstRestfulDbAdapter


class ServicelogConaiTarotServiceLogMstRestfulOutPort(ABC):
    """
    # CLASS : ServicelogConaiTarotServiceLogMstRestfulOutPort
    # AUTHOR : conai
    # TIME : 2025. 1. 15. 오후 12:36
    # DESCRIPTION
        - ServicelogConaiTarotServiceLogMst Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2025. 1. 15.          conai          최초 생성
    """

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_db_out_port(self, request):
        pass

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_db_out_port_get(self, request):
        pass

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_db_out_port_post(self, request):
        pass

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_db_out_port_put(self, request):
        pass

    @abstractmethod
    def servicelog_conai_tarot_service_log_mst_restful_db_out_port_delete(self, request):
        pass


class ServicelogConaiTarotServiceLogMstRestfulOutPortImpl(ServicelogConaiTarotServiceLogMstRestfulOutPort):

    def __init__(self, servicelogConaiTarotServiceLogMstRestfulDbAdapter: ServicelogConaiTarotServiceLogMstRestfulDbAdapter
                 ):
        self.servicelogConaiTarotServiceLogMstRestfulDbAdapter = servicelogConaiTarotServiceLogMstRestfulDbAdapter

    def servicelog_conai_tarot_service_log_mst_restful_db_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_db_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_db_out_port arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_db_out_port kwarg ==> {kwarg}")

        result = self.servicelog_conai_tarot_service_log_mstRestfulDbAdapter.servicelog_conai_tarot_service_log_mst_restful_db(self, *args, **kwargs)

        return result

    def servicelog_conai_tarot_service_log_mst_restful_db_out_port_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_out_port_get args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_out_port_get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_out_port_get kwarg ==> {kwarg}")

        result = self.servicelogConaiTarotServiceLogMstRestfulDbAdapter.servicelog_conai_tarot_service_log_mst_restful_db_get(self, *args, **kwargs)

        return result

    def servicelog_conai_tarot_service_log_mst_restful_db_out_port_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_db_out_port_post args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_db_out_port_post arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_db_out_port_post kwarg ==> {kwarg}")

        result = self.servicelogConaiTarotServiceLogMstRestfulDbAdapter.servicelog_conai_tarot_service_log_mst_restful_db_post(self, *args, **kwargs)

        return result

    def servicelog_conai_tarot_service_log_mst_restful_db_out_port_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_db_out_port_put args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_db_out_port_put arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_db_out_port_put kwarg ==> {kwarg}")

        result = self.servicelogConaiTarotServiceLogMstRestfulDbAdapter.servicelog_conai_tarot_service_log_mst_restful_db_put(self, *args, **kwargs)

        return result

    def servicelog_conai_tarot_service_log_mst_restful_db_out_port_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicelog_conai_tarot_service_log_mst_restful_db_out_port_delete args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_db_out_port_delete arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicelog_conai_tarot_service_log_mst_restful_db_out_port_delete kwarg ==> {kwarg}")

        result = self.servicelogConaiTarotServiceLogMstRestfulDbAdapter.servicelog_conai_tarot_service_log_mst_restful_db_delete(self, *args, **kwargs)

        return result
