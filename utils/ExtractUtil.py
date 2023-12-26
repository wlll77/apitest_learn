import json
import time

from utils.AssertUtil import AssertUtil
from utils.YamlUtil import YamlUtil
from utils.log_util import logger


class ExtractUtil:
    def __init__(self):
        self.jsonpath_util = AssertUtil()
        self.yaml_util = YamlUtil()

    def extract_data(self, res, extract):
        """
        根据extract表达式，获取接口内容并存入yaml
        :param res: res.json()
        :param extract: eg$.token
        :return:
        """
        if extract:
            for key, expression in extract.items():
                try:
                    value = self.jsonpath_util.extract_by_jsonpath(res, expression)
                    # 写入value
                    self.yaml_util.write_extra_yaml({key: value})
                except Exception as e:
                    logger.error(f"变量{key}写入extract.yaml失败，请检查，error={e}")

    def get_extract_value(self, key):
        """从extract.yaml中获取内容"""
        try:
            data = self.yaml_util.read_extract_yaml()
            return data[key]
        except Exception as e:
            logger.error(f"从yaml中根据{key}获取不到内容，error={e}")

    def extract_url(self, url):
        if "${" in url and "}" in url:
            return self.process_data(url)
        return url
        # / orders /${get_extract_value(order_id)} /

    def process_data(self, data):
        """处理函数"""
        for i in range(data.count('${')):
            if '${' in data and '}' in data:
                start_index = data.index('$')
                end_index = data.index('}')
                # 获取函数中的方法
                func_full_name = data[start_index: end_index + 1]
                # 获取函数名
                func_name = data[start_index + 2:data.index('(')]
                # 获取函数中的参数
                func_params = data[data.index('(') + 1:data.index(')')]
                # 先进行getattr
                extract_data = getattr(self, func_name, None)
                if extract_data is not None:
                    # 将参数拆分为列表
                    func_params = func_params.split(',') if func_params else []
                    # 尝试将参数转换为整数，能转则进行转换
                    func_params = [int(param) if param.isdigit() else param for param in func_params]
                    extract_data = extract_data(*func_params)
                # # getattr不支持函数参数为int型
                # extract_data = getattr(self, func_name)(*func_params.split(','))
                data = data.replace(func_full_name, str(extract_data))
        return data

    def get_time(self):
        timestamp = int(time.time())
        return timestamp

    def test_add(self, a, b):
        return a+b

    def extract_case(self, case_info):
        # 转换成str类型
        str_case_info = json.dumps(case_info)
        data = self.process_data(str_case_info)
        # 换回json类型
        return  json.loads(data)

if __name__ == '__main__':
    # print(ExtractUtil().get_extract_value())
    # print(getattr(ExtractUtil(), "get_extract_value")("1111","2222"))
    # print(ExtractUtil().get_extract_value(("order_id")))
    # print(ExtractUtil().process_data('${test_add(1, 2)}'))
    print(ExtractUtil().get_time())
    # pass