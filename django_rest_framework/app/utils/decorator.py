# from functools import wraps

from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
import logging

logger = logging.getLogger("django.server")


def check_token(func):
    """
    # check_token 설명

    # PARAMS :

    # RETURN :

    # DESCRIPTION
        API 동작을 수행 하기 전에, 토큰이 유효한지 확인하는 decorator
    ==================================================
    AUTHOR              DATE                NOTE
    --------------------------------------------------
    jung-gyuho              2023/08/14 11:59 AM       최초 작성
    """

    # @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        logger.info(f"decorator : Controller post get request.headers ==> {request.headers}")
        logger.info(f"decorator : Controller post get request.COOKIES ==> {request.COOKIES}")
        get_client_ip(request)
        # accessToken, refreshToken 있는지 체크
        if request.COOKIES.get('accessToken') and request.COOKIES.get('refreshToken'):
            print(
                f"decorator token YES : Controller post get request.COOKIES['accessToken'] ==> {request.COOKIES['accessToken']}")
            print(
                f"decorator token YES : Controller post get request.COOKIES['refreshToken'] ==> {request.COOKIES['refreshToken']}")
            return func(self, request, *args, **kwargs)
        else:
            print(
                f"decorator token NO : Controller post get request.COOKIES['accessToken'] ==> {request.COOKIES.get('accessToken', 'None')}")
            print(
                f"decorator token NO : Controller post get request.COOKIES['refreshToken'] ==> {request.COOKIES.get('refreshToken', 'None')}")
            # raise PermissionDenied # 주석 해제시, 토큰 없을 시, 403 에러 발생
            return func(self, request, *args, **kwargs)  # by pass, 체크만 진행, 에러 발생 시키지 않고 통과

    return wrapper


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    logger.info(f"get_client_ip ==> {ip}")
    return ip


def check_request(func):
    def wrapper(self, request, *args, **kwargs):
        logger.info(f"decorator : Controller post get request.headers ==> {request.headers}")
        logger.info(f"decorator : Controller post get request.data ==> {request.data}")

    return wrapper
