from abc import ABC, abstractmethod

from user.adapter.out.user_conai_tarot_service_user_mst_restful_db_adapter import UserConaiTarotServiceUserMstRestfulDbAdapter


class UserConaiTarotServiceUserMstRestfulOutPort(ABC):
    """
    # CLASS : UserConaiTarotServiceUserMstRestfulOutPort
    # AUTHOR : conai
    # TIME : 2024. 12. 26. 오후 4:27
    # DESCRIPTION
        - UserConaiTarotServiceUserMst Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 12. 26.          conai          최초 생성
    """

    @abstractmethod
    def user_conai_tarot_service_user_mst_restful_db_out_port(self, request):
        pass

    @abstractmethod
    def user_conai_tarot_service_user_mst_restful_db_out_port_get(self, request):
        pass

    @abstractmethod
    def user_conai_tarot_service_user_mst_restful_db_out_port_post(self, request):
        pass

    @abstractmethod
    def user_conai_tarot_service_user_mst_restful_db_out_port_put(self, request):
        pass

    @abstractmethod
    def user_conai_tarot_service_user_mst_restful_db_out_port_delete(self, request):
        pass


class UserConaiTarotServiceUserMstRestfulOutPortImpl(UserConaiTarotServiceUserMstRestfulOutPort):

    def __init__(self, userConaiTarotServiceUserMstRestfulDbAdapter: UserConaiTarotServiceUserMstRestfulDbAdapter
                 ):
        self.userConaiTarotServiceUserMstRestfulDbAdapter = userConaiTarotServiceUserMstRestfulDbAdapter

    def user_conai_tarot_service_user_mst_restful_db_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_tarot_service_user_mst_restful_db_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_db_out_port arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_db_out_port kwarg ==> {kwarg}")

        result = self.user_conai_tarot_service_user_mstRestfulDbAdapter.user_conai_tarot_service_user_mst_restful_db(self, *args, **kwargs)

        return result

    def user_conai_tarot_service_user_mst_restful_db_out_port_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_tarot_service_user_mst_restful_out_port_get args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_out_port_get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_out_port_get kwarg ==> {kwarg}")

        result = self.userConaiTarotServiceUserMstRestfulDbAdapter.user_conai_tarot_service_user_mst_restful_db_get(self, *args, **kwargs)

        return result

    def user_conai_tarot_service_user_mst_restful_db_out_port_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_tarot_service_user_mst_restful_db_out_port_post args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_db_out_port_post arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_db_out_port_post kwarg ==> {kwarg}")

        result = self.userConaiTarotServiceUserMstRestfulDbAdapter.user_conai_tarot_service_user_mst_restful_db_post(self, *args, **kwargs)

        return result

    def user_conai_tarot_service_user_mst_restful_db_out_port_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_tarot_service_user_mst_restful_db_out_port_put args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_db_out_port_put arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_db_out_port_put kwarg ==> {kwarg}")

        result = self.userConaiTarotServiceUserMstRestfulDbAdapter.user_conai_tarot_service_user_mst_restful_db_put(self, *args, **kwargs)

        return result

    def user_conai_tarot_service_user_mst_restful_db_out_port_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_tarot_service_user_mst_restful_db_out_port_delete args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_db_out_port_delete arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : user_conai_tarot_service_user_mst_restful_db_out_port_delete kwarg ==> {kwarg}")

        result = self.userConaiTarotServiceUserMstRestfulDbAdapter.user_conai_tarot_service_user_mst_restful_db_delete(self, *args, **kwargs)

        return result
