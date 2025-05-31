from abc import ABC, abstractmethod

from ....adapter.out.servicetoken_conai_tarot_service_user_token_mst_restful_db_adapter import ServicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter


class ServicetokenConaiTarotServiceUserTokenMstRestfulOutPort(ABC):
    """
    # CLASS : ServicetokenConaiTarotServiceUserTokenMstRestfulOutPort
    # AUTHOR : conai
    # TIME : 2025. 1. 22. 오후 6:15
    # DESCRIPTION
        - ServicetokenConaiTarotServiceUserTokenMst Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2025. 1. 22.          conai          최초 생성
    """

    @abstractmethod
    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port(self, request):
        pass

    @abstractmethod
    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_get(self, request):
        pass

    @abstractmethod
    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_post(self, request):
        pass

    @abstractmethod
    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_put(self, request):
        pass

    @abstractmethod
    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_delete(self, request):
        pass


class ServicetokenConaiTarotServiceUserTokenMstRestfulOutPortImpl(ServicetokenConaiTarotServiceUserTokenMstRestfulOutPort):

    def __init__(self, servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter: ServicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter
                 ):
        self.servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter = servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter

    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port kwarg ==> {kwarg}")

        result = self.servicetoken_conai_tarot_service_user_token_mstRestfulDbAdapter.servicetoken_conai_tarot_service_user_token_mst_restful_db(self, *args, **kwargs)

        return result

    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_restful_out_port_get args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_out_port_get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_out_port_get kwarg ==> {kwarg}")

        result = self.servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter.servicetoken_conai_tarot_service_user_token_mst_restful_db_get(self, *args, **kwargs)

        return result

    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_post args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_post arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_post kwarg ==> {kwarg}")

        result = self.servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter.servicetoken_conai_tarot_service_user_token_mst_restful_db_post(self, *args, **kwargs)

        return result

    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_put args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_put arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_put kwarg ==> {kwarg}")

        result = self.servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter.servicetoken_conai_tarot_service_user_token_mst_restful_db_put(self, *args, **kwargs)

        return result

    def servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_delete args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_delete arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_delete kwarg ==> {kwarg}")

        result = self.servicetokenConaiTarotServiceUserTokenMstRestfulDbAdapter.servicetoken_conai_tarot_service_user_token_mst_restful_db_delete(self, *args, **kwargs)

        return result
