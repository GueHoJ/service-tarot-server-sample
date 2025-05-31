import sys
import inspect
import requests
import re
import json
import socket
import logging
from django.conf import settings
from django.db import connection, connections
from datetime import datetime

from django.http import FileResponse
from django.utils.encoding import iri_to_uri

logger = logging.getLogger('django')

# ANSI escape codes for colors
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'


def log_info(message):
    class_name, line_number = get_line_info()

    bar = "=" * 120
    formatted_message = f"\n{CYAN}{BOLD}{bar}\n{class_name} (line {line_number}): {message}\n{bar}{END}\n"
    logger.info(formatted_message)
    sys.stdout.flush()  # Ensure immediate printing of logs


def get_line_info():
    frame = inspect.currentframe()
    outer_frames = inspect.getouterframes(frame)
    calling_frame = outer_frames[1]
    class_name = calling_frame.frame.f_globals["__name__"]
    line_number = calling_frame.lineno
    return class_name, line_number


def log_error(message):
    class_name, line_number = get_line_info()

    bar = "=" * 120
    formatted_message = f"\n{RED}{BOLD}{bar}\n[ERROR] {class_name} (line {line_number}): {message}\n{bar}{END}\n"
    logger.error(formatted_message)
    sys.stdout.flush()  # Ensure immediate printing of logs


def call_crm_api(self, className, api_host, path, method, data, *args, **kwargs):
    """
    # call_crm_api 설명

    # PARAMS :
        className : 클래스 명
        path : API BASEURL 이하 경로
        method : POST 사용, GET, POST 등
        data : json data
    # RETURN :
        json
        - response.text
        - accessToken, refreshToken
    # DESCRIPTION

    ==================================================
    AUTHOR              DATE                NOTE
    --------------------------------------------------
    jung-gyuho              2023/07/21 10:13 PM       최초 작성
    """
    # APP 서버에서 호출 시 API_HOST = "http://172.16.0.43" 로 호출해야 API 호출 가능
    # API_HOST = "https://crm.junobiz.com"
    API_HOST = api_host

    url = API_HOST + path
    print(f"{className} : call_crm_api api_host ==> {api_host}, API_HOST ==> {API_HOST}, url ==> {url}")

    for key in kwargs.keys():
        print(f"{className} : call_crm_api get arg ==> {key} : {kwargs[key]}")

    hostname = socket.gethostbyname(socket.gethostname())
    print(f"{className} : call_crm_api gethostname ==> {hostname}")
    ip = socket.gethostbyname(socket.getfqdn())
    print(f"{className} : call_crm_api getfqdn ==> {ip}")
    static_origin = getattr(settings, "STATIC_ORIGIN", None)
    headers = {'Content-Type': 'application/json; charset=utf-8',
               'Origin': static_origin}
    # accessToken은 헤더 'Authorization'에 담아서 보낸다.
    if kwargs.get('accessToken') is not None:
        headers['Authorization'] = 'Bearer ' + kwargs['accessToken']

    # accessToken, refreshToken은 COOKIE 에 담아서 보낸다.
    if kwargs.get('refreshToken') is not None:
        requests.cookies = {'accessToken': kwargs['accessToken'], 'refreshToken': kwargs['refreshToken']}

    result = {}
    # is_verify = True
    is_verify = False
    print(f"{className} : call_crm_api ==> {data}")
    print("0. headers %r" % headers)

    # try:
    if method == 'GET':
        print(f"0. call_crm_api GET url ==> {url}")
        response = requests.get(url, headers=headers, params=data)
        print("0. response status %r" % response.status_code)
        print("0. response text %r" % response.text)
        print(f"0. {className} : call_crm_api response.cookies ==> {response.cookies}")

        return response_handler(className, response, result)
    elif method == 'ATTACHFILE':
        print(f"0. call_crm_api GET url/fileName ==> {url}{data['fileName']}")
        url = url + data['fileName']
        fileName = data['fileName']
        response = requests.get(url, headers=headers)
        print("0. response status %r" % response.status_code)
        print("0. response text %r" % response.text)
        print(f"0. {className} : call_crm_api response.cookies ==> {response.cookies}")
        file_response = FileResponse(response, status=response.status_code)
        file_response['Content-Disposition'] = f'attachment; filename="{fileName}"'

        # result['data'] = file_response
        # result['status_code'] = file_response.status_code
        print(f"3. {className} : call_crm_api file_response ==> {file_response}")
        return file_response
    elif method == 'POST':

        response = requests.post(url, json=data, headers=headers, verify=is_verify, timeout=300)

        print("0. response status %r" % response.status_code)
        print("0. response text %r" % response.text)
        print(f"0. {className} : call_crm_api response.cookies ==> {response.cookies}")
        return response_handler(className, response, result)
    # except Exception as ex:
    #     print(f"{className} : call_crm_api Exception ==> {ex}")
    # return {"data": str(ex)}


def response_handler(className, response, result):
    if response.ok:
        # print("1. response status %r" % response.status_code)
        # print("1. response text %r" % response.text)
        # requests.cookies = response.cookies
        # csrftoken = response.cookies['csrftoken']
        print(f"1. {className} : call_crm_api response.cookies ==> {response.cookies}")

        # response.cookies 에 accessToken, refreshToken 값 있는 경우 result 에 저장
        for res in response.cookies:
            if res.name == 'accessToken':
                result['accessToken'] = res.value
                print(
                    f"2. {className} : call_crm_api response.cookie.name : value  ==> {res.name} : {res.value}")
            if res.name == 'refreshToken':
                result['refreshToken'] = res.value
                print(
                    f"2. {className} : call_crm_api response.cookie.name : value  ==> {res.name} : {res.value}")

        result['data'] = response.text
        result['status_code'] = response.status_code
        print(f"3. {className} : call_crm_api result ==> {result}")
        return result
    else:
        result['data'] = response.text
        result['status_code'] = response.status_code
        result['response'] = response
        print(f"4. {className} : call_crm_api response ==> {response}")
        return result


def call_hrm_api(self, className, api_host, path, method, data, *args, **kwargs):
    """
    # call_hrm_api 설명

    # PARAMS :
        className : 클래스 명
        path : API BASEURL 이하 경로
        method : POST 사용, GET, POST 등
        data : json data
    # RETURN :
        json
        - response.text
        - accessToken, refreshToken
    # DESCRIPTION

    ==================================================
    AUTHOR              DATE                NOTE
    --------------------------------------------------
    jung-gyuho              2023/07/21 10:13 PM       최초 작성
    """
    # API_HOST = "http://192.168.0.247:8000"
    API_HOST = api_host

    url = API_HOST + path

    for key in kwargs.keys():
        print(f"{className} : call_hrm_api get arg ==> {key} : {kwargs[key]}")

    hostname = socket.gethostbyname(socket.gethostname())
    print(f"{className} : call_crm_api gethostname ==> {hostname}")
    ip = socket.gethostbyname(socket.getfqdn())
    print(f"{className} : call_crm_api getfqdn ==> {ip}")

    headers = {'Content-Type': 'application/json; charset=utf-8',
               'Origin': ip}
    # # accessToken은 헤더 'Authorization'에 담아서 보낸다.
    # if kwargs.get('accessToken') is not None:
    #     headers['Authorization'] = 'Bearer ' + kwargs['accessToken']
    #
    # # accessToken, refreshToken은 COOKIE 에 담아서 보낸다.
    # if kwargs.get('refreshToken') is not None:
    #     requests.cookies = {'accessToken': kwargs['accessToken'], 'refreshToken': kwargs['refreshToken']}

    result = {}
    # is_verify = True
    is_verify = False
    print(f"{className} : call_hrm_api ==> {data}")

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':

            response = requests.post(url, json=data, headers=headers, verify=is_verify, timeout=8)

            print("0. response status %r" % response.status_code)
            print("0. response text %r" % response.text)
            print(f"0. {className} : call_hrm_api response.cookies ==> {response.cookies}")
            if response.ok:
                # print("1. response status %r" % response.status_code)
                # print("1. response text %r" % response.text)
                # requests.cookies = response.cookies
                # csrftoken = response.cookies['csrftoken']
                print(f"1. {className} : call_hrm_api response.cookies ==> {response.cookies}")

                # response.cookies 에 accessToken, refreshToken 값 있는 경우 result 에 저장
                for res in response.cookies:
                    if res.name == 'accessToken':
                        result['accessToken'] = res.value
                        print(
                            f"2. {className} : call_hrm_api response.cookie.name : value  ==> {res.name} : {res.value}")
                    if res.name == 'refreshToken':
                        result['refreshToken'] = res.value
                        print(
                            f"2. {className} : call_hrm_api response.cookie.name : value  ==> {res.name} : {res.value}")

                result['status_code'] = response.status_code
                result['data'] = response.text
                return result
            else:
                result['data'] = response.text
                result['status_code'] = response.status_code
                result['response'] = response
                print(f"4. {className} : call_hrm_api response ==> {response}")
                return result

    except Exception as ex:
        print(f"{className} : call_hrm_api Exception ==> {ex}")
        return {"Exception": str(ex)}


def execute_raw_sql_query(db, sql_query, params):
    connection = connections[db]
    print(f"execute_raw_sql_query params ==> {params}")
    print(f"execute_raw_sql_query params 파라미터 방식 사용하지 않음 ==> {params}")
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        results = dictfetchall(cursor)
        print(f"execute_raw_sql_query results ==> {results}")
    return results


def dictfetchall(cursor):
    # Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    print(f"dictfetchall columns ==> {columns}")
    camel_columns = convert_snake_to_camel(columns)
    print(f"dictfetchall camel_columns ==> {camel_columns}")
    return [
        dict(zip(camel_columns, row))
        for row in cursor.fetchall()
    ]


def convert_snake_to_camel(snake_str_list):
    camel_str_list = []
    for snake_str in snake_str_list:
        if "_" in snake_str:
            # print(f"convert_snake_to_camel snake_str ==> {snake_str}")
            components = snake_str.split('_')
            # print(f"convert_snake_to_camel components ==> {components}")
            camel_str_list.append(components[0].lower() + ''.join(x.title() for x in components[1:]))
        else:
            camel_str_list.append(snake_str)

    return camel_str_list


def field_name_to_label(field_name):
    if "_" in field_name:
        # print(f"convert_snake_to_camel field_name ==> {field_name}")
        components = field_name.split('_')
        # print(f"convert_snake_to_camel components ==> {components}")
        label = components[0].lower() + ''.join(x.title() for x in components[1:])
        # print(f"field_name_to_label label ==> {label}")
        return label
    else:
        # print(f"field_name_to_label field_name ==> {field_name}")
        return field_name


def camelcase_to_snakecase(value):
    return ''.join(['_' + i.lower() if i.isupper() else i for i in value]).lstrip('_')


def setParams(sql_query, dclre_map, params_map):
    print(f"setParams sql_query ==> {sql_query}")
    print(f"setParams dclre_map ==> {dclre_map}")
    print(f"setParams params_map ==> {params_map}")
    for key in dclre_map.keys():
        print(f"setParams dclre_map key ==> {key}")
        print(f"setParams dclre_map params_map.get(key, None) ==> {params_map.get(key, None)}")
        if params_map.get(key, None) is None:
            sql_query = sql_query.replace(dclre_map[key], 'NULL')
        elif params_map.get(key, None) == '':
            sql_query = sql_query.replace(dclre_map[key], 'NULL')
        else:
            sql_query = sql_query.replace(dclre_map[key], f"'{params_map[key]}'")
    print(f"setParams sql_query ==> {sql_query}")
    return sql_query


def get_target_params_map(params, target_params):
    print(f"get_target_params_map params ==> {params}")
    params_map = {}
    for param in target_params:
        print(f"get_target_params_map arg ==> {param}")
        print(f"get_target_params_map params.get(arg) ==> {params.get(param)}")
        params_map[param] = params.get(param)
    print(f"get_target_params_map params_map ==> {params_map}")
    return params_map


def get_db_info():
    DB_HOST = getattr(settings, "POSTGRES_HOST", None)
    DB_PORT = getattr(settings, "POSTGRES_PORT", None)
    DB_ADR = DB_HOST + ":" + DB_PORT
    print(f"DB HOST ==> {DB_ADR}")
    return DB_ADR


# convert json to object
def convert_json_to_obj(data):
    """
    json string 을 object 로 변환
    :param data: request data 혹은 interface response data
    :return: object
    """
    try:
        if isinstance(data, str):
            return json.loads(data)
        # elif isinstance(data, dict):
        #     return data
        else:
            return json.loads(data.body.decode('utf-8'))
    except Exception as ex:
        print(f"convert_json_to_obj Exception ==> {ex}")
        return {"Exception": str(ex)}


def convert_dict_to_json(data):
    """
    dictionary data 를 json 형식으로 변환
    :param data: dictionary type data
    :return: object
    """
    if isinstance(data, dict):
        return json.dumps(data, ensure_ascii=False)
    else:
        return data


def manage_tokens(self, kwargs, request):
    """
    # manage_tokens 설명

    # PARAMS :
        kwargs : accessToken, refreshToken 을 담을 dynamic parameter
        request : accessToken, refreshToken 을 담고 있는 request 요청
    # RETURN :
        kwargs
    # DESCRIPTION

    ==================================================
    AUTHOR              DATE                NOTE
    --------------------------------------------------
    jung-gyuho              2023/07/27 4:24 PM       최초 작성
    """
    # accessToekn, refreshToken 을 request 에서 가져온다.
    # accessToken 은 쿠키로 관리
    if request.COOKIES.get('accessToken'):
        print(
            f"{self.__class__.__name__} : Controller post get request.COOKIES['accessToken'] ==> {request.COOKIES['accessToken']}")
        kwargs['accessToken'] = request.COOKIES['accessToken']
    # refreshToken 은 쿠키로 관리
    if request.COOKIES.get('refreshToken'):
        print(
            f"{self.__class__.__name__} : Controller post get request.COOKIES['refreshToken'] ==> {request.COOKIES['refreshToken']}")
        kwargs['refreshToken'] = request.COOKIES['refreshToken']

    return kwargs


def filter_result_by_user_id(self, response_data, request_param):
    # print(f"response_data : {response_data}")
    # print(f"request_param : {request_param}")

    chart_data = response_data['chartData']
    user_data = {'chartData': []}

    for data in chart_data:
        if data['salesUserId'] == request_param['salesUserId']:
            user_data['chartData'].append(data)

    return user_data


def order_result_data_by_date(self, response_data):
    print(f"response_data : {response_data}")

    tmp_data = response_data['chartData']
    tmp_data.sort(key=lambda x: x['ordDt'])

    print(f"tmp_data : {tmp_data}")

    response_data['chartData'] = tmp_data

    return response_data


def order_result_data_by_month(self, response_data):
    print(f"response_data : {response_data}")

    tmp_data = response_data['chartData']
    tmp_data.sort(key=lambda x: x['ordYyyymm'])

    print(f"tmp_data : {tmp_data}")

    response_data['chartData'] = tmp_data

    return response_data


def sum_month_result_data_by_year(self, response_data):
    print(f"sum_month_result_data_by_year response_data : {response_data}")

    tmp_data = response_data['chartData']

    rowNum = 0
    shopNm = ""
    salesUserId = 0
    salesUserNm = ""
    salesNckNm = ""
    ofdtyNm = ""
    ofcStateNm = ""
    acdmySeq = 0
    ordYyyymm = ""
    tmFnlPayAmt = 0
    tmBrndBnfAmt = 0
    etcFnlPayAmt = 0
    etcBrndBnfAmt = 0
    empFnlPayAmt = 0
    totAmt = 0

    yyyy = ""

    year_list = []
    year_object = {}

    for i, data in enumerate(tmp_data):
        print(f"sum_month_result_data_by_year data : {data}")
        ordYyyymm = data['ordYyyymm']
        if yyyy == "":
            yyyy = ordYyyymm[0:4]
        elif yyyy != ordYyyymm[0:4]:
            rowNum += 1
            year_object = sum_data_object(data, empFnlPayAmt, etcBrndBnfAmt, etcFnlPayAmt, rowNum, tmBrndBnfAmt,
                                          tmFnlPayAmt,
                                          totAmt, yyyy)

            year_list.append(year_object)

            tmFnlPayAmt = 0
            tmBrndBnfAmt = 0
            etcFnlPayAmt = 0
            etcBrndBnfAmt = 0
            empFnlPayAmt = 0
            totAmt = 0

            yyyy = ordYyyymm[0:4]

        print(f"sum_month_result_data_by_year yyyy : {yyyy}")
        tmFnlPayAmt += float(data['tmFnlPayAmt'])
        tmBrndBnfAmt += float(data['tmBrndBnfAmt'])
        etcFnlPayAmt += float(data['etcFnlPayAmt'])
        etcBrndBnfAmt += float(data['etcBrndBnfAmt'])
        empFnlPayAmt += float(data['empFnlPayAmt'])
        totAmt += float(data['totAmt'])

        if i == len(tmp_data) - 1:
            rowNum += 1
            year_object = sum_data_object(data, empFnlPayAmt, etcBrndBnfAmt, etcFnlPayAmt, rowNum, tmBrndBnfAmt,
                                          tmFnlPayAmt,
                                          totAmt, yyyy)

            year_list.append(year_object)

    print(f"sum_month_result_data_by_year tmp_data : {tmp_data}")
    print(f"sum_month_result_data_by_year year_list : {year_list}")

    response_data['chartData'] = year_list

    return response_data


def sum_data_object(data, empFnlPayAmt, etcBrndBnfAmt, etcFnlPayAmt, rowNum, tmBrndBnfAmt, tmFnlPayAmt, totAmt,
                    yyyy):
    year_object = {'rowNum': rowNum, 'shopNm': data['shopNm'], 'salesUserId': data['salesUserId'],
                   'salesUserNm': data['salesUserNm'], 'salesNckNm': data['salesNckNm'], 'ofdtyNm': data['ofdtyNm'],
                   'ofcStateNm': data['ofcStateNm'], 'acdmySeq': data['acdmySeq'], 'ordYyyy': yyyy,
                   'tmFnlPayAmt': tmFnlPayAmt,
                   'tmBrndBnfAmt': tmBrndBnfAmt, 'etcFnlPayAmt': etcFnlPayAmt, 'etcBrndBnfAmt': etcBrndBnfAmt,
                   'empFnlPayAmt': empFnlPayAmt, 'totAmt': totAmt}
    return year_object


def regenerate_row_num(self, response_data):
    print(f"regenerate_row_num response_data : {response_data}")

    tmp_data = response_data['chartData']

    for i, data in enumerate(tmp_data):
        data['rowNum'] = i + 1

    print(f"tmp_data : {tmp_data}")

    response_data['chartData'] = tmp_data

    return response_data


def generate_product_month_params(self, request_param):
    print(f"generate_product_month_params request_param : {request_param}")

    start_year = request_param['searchStDt']
    end_year = request_param['searchEdDt']

    searchStDt = start_year + '01'
    searchEdDt = end_year + '12'

    request_param['searchStDt'] = searchStDt
    request_param['searchEdDt'] = searchEdDt

    return request_param


def process_streaming_response(response):
    # Split the response into individual JSON objects and process each one
    json_strings = response.content.decode().split('\n')
    combined_response = ""
    json_list = []

    for json_str in json_strings:
        if not json_str.strip():  # Skip empty lines
            continue
        try:
            json_obj = json.loads(json_str)
            json_list.append(json_obj)
            if 'response' in json_obj:
                combined_response += json_obj['response']
        except json.JSONDecodeError:
            print(f"Error parsing JSON: {json_str}")
            continue

    json_list.append({"combined_response": combined_response})

    return json_list