from core.rest_client_new import RestClient
from utils.AssertUtil import AssertUtil


class ApiService:
    def __init__(self):
        self.session = RestClient()

    def handle_case(self, test_data):
        # 获取url
        url = test_data['request_info']['url']
        # 获取method
        method = test_data['request_info']['method']
        # 获取url
        headers = test_data['request_info']['headers']

        # 获取case_info
        case_info = test_data['case_info']
        #  获取validate
        validate = case_info.pop('validate', None)
        res = self.session.do_request(url=url, method=method, headers=headers, **case_info)
        # 断言逻辑
        AssertUtil().validate_response(res, validate)
        return res