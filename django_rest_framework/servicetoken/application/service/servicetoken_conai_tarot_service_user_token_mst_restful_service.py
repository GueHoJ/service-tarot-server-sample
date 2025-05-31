from django.conf import settings
import logging

from ..port._in.servicetoken_conai_tarot_service_user_token_mst_restful_in_port import ServicetokenConaiTarotServiceUserTokenMstRestfulInPort
from ..port.out.servicetoken_conai_tarot_service_user_token_mst_restful_out_port import ServicetokenConaiTarotServiceUserTokenMstRestfulOutPort
import app.utils.common_utils as common_utils


logger = logging.getLogger("django.server")


class ServicetokenConaiTarotServiceUserTokenMstRestfulService:
    """
    # CLASS : ServicetokenConaiTarotServiceUserTokenMstRestfulService
    # AUTHOR : conai
    # TIME : 2025. 1. 22. 오후 6:15
    # DESCRIPTION
        - ServicetokenConaiTarotServiceUserTokenMst Restful Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2025. 1. 22.          conai          최초 생성
    """

    def __init__(self, portInImpl: ServicetokenConaiTarotServiceUserTokenMstRestfulInPort, portOutImpl: ServicetokenConaiTarotServiceUserTokenMstRestfulOutPort):
        self.servicetokenIn = portInImpl
        self.servicetokenOut = portOutImpl

    def servicetoken_conai_tarot_service_user_token_mst_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_get *args ==> {args[0]}")

        data = self.servicetokenIn.servicetoken_conai_tarot_service_user_token_mst_restful_in_port_get(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_get kwarg ==> {kwarg}")

        DB_ADR = common_utils.get_db_info()
        result = self.servicetokenOut.servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_get(self, DB_ADR, data)

        print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_get result ==> {result}")

        return result

    def servicetoken_conai_tarot_service_user_token_mst_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_post *args ==> {args[0]}")

        data = self.servicetokenIn.servicetoken_conai_tarot_service_user_token_mst_restful_in_port_post(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_post arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_post kwarg ==> {kwarg}")

        DB_ADR = common_utils.get_db_info()
        result = self.servicetokenOut.servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_post(self, DB_ADR, data)

        print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_post result ==> {result}")

        return result

    def servicetoken_conai_tarot_service_user_token_mst_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_put *args ==> {args[0]}")

        data = self.servicetokenIn.servicetoken_conai_tarot_service_user_token_mst_restful_in_port_put(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_put arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_put kwarg ==> {kwarg}")

        DB_ADR = common_utils.get_db_info()
        result = self.servicetokenOut.servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_put(self, DB_ADR, data)

        print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_put result ==> {result}")

        return result

    def servicetoken_conai_tarot_service_user_token_mst_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_delete *args ==> {args[0]}")

        data = self.servicetokenIn.servicetoken_conai_tarot_service_user_token_mst_restful_in_port_delete(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_delete arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} servicetoken_conai_tarot_service_user_token_mst_delete kwarg ==> {kwarg}")

        DB_ADR = common_utils.get_db_info()
        result = self.servicetokenOut.servicetoken_conai_tarot_service_user_token_mst_restful_db_out_port_delete(self, DB_ADR, data)

        print(f"{self.__class__.__name__} : servicetoken_conai_tarot_service_user_token_mst_delete result ==> {result}")

        return result
