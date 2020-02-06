import json
from django.http import JsonResponse


class Response:
    __header__ = {}
    __body__ = {}

    def __init__(self):
        self.__clean_header__()
        self.__clean_body__()

    def __str__(self):
        pass

    def __clean_header__(self):
        self.__header__ = {'error_code': "None", 'status': "None"}

    def __clean_body__(self):
        self.__body__ = {}

    def get_header(self):
        return self.__header__

    def get_body(self):
        return self.__body__

    def construct_json_response(self):
        header_ret = json.loads(json.dumps(self.__header__, ensure_ascii=False))
        body_ret = json.loads(json.dumps(self.__body__, ensure_ascii=False))
        return JsonResponse({"header": header_ret, "body": body_ret}, json_dumps_params={'ensure_ascii': False})
