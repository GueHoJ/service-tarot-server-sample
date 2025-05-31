from abc import ABC, abstractmethod


class UserConaiUserMstRestfulInPort(ABC):
    """
    # CLASS : UserConaiUserMstRestfulInPort
    # AUTHOR : conai
    # TIME : 2024. 8. 16. conai
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2024. 8. 16.          conai          최초 생성
    """

    @abstractmethod
    def user_conai_user_mst_restful_in_port(self, *args, **kwargs):
        pass

    @abstractmethod
    def user_conai_user_mst_restful_in_port_get(self, *args, **kwargs):
        pass

    @abstractmethod
    def user_conai_user_mst_restful_in_port_post(self, *args, **kwargs):
        pass

    @abstractmethod
    def user_conai_user_mst_restful_in_port_put(self, *args, **kwargs):
        pass

    @abstractmethod
    def user_conai_user_mst_restful_in_port_delete(self, *args, **kwargs):
        pass


class UserConaiUserMstRestfulInPortImpl(UserConaiUserMstRestfulInPort):

    def __init__(self):
        pass

    def user_conai_user_mst_restful_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_user_mst_restful_in_port request params ==> {args[0]}")
        result = args[1]

        return result

    def user_conai_user_mst_restful_in_port_get(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_user_mst_restful_in_port_get request params ==> {args[1]}")
        result = args[1]

        return result

    def user_conai_user_mst_restful_in_port_post(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_user_mst_restful_in_port_post request params ==> {args[1]}")
        result = args[1]

        return result

    def user_conai_user_mst_restful_in_port_put(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_user_mst_restful_in_port_put request params ==> {args[1]}")
        result = args[1]

        return result

    def user_conai_user_mst_restful_in_port_delete(self, *args, **kwargs):
        print(f"{self.__class__.__name__} user_conai_user_mst_restful_in_port_delete request params ==> {args[1]}")
        result = args[1]

        return result
