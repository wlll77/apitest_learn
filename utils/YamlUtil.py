import os

import yaml


class YamlUtil:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data/")

    def read_testcases_yaml(self, yaml_name, key_name=None):
        with open(self.data_path + yaml_name, mode='r', encoding='utf8') as f:
            value = yaml.safe_load(f)
            if key_name:
                return value[key_name]
            return value

    def read_extract_yaml(self):
        with open(self.data_path + "extract.yaml", mode='r', encoding='utf8') as f:
            value = yaml.safe_load(f)
            return value

    def extract_case(self, yaml_name, key_name):
        case_value = self.read_testcases_yaml(yaml_name, key_name)[0]
        new_case = []
        for value in case_value['case_info']:
            new_case.append({"request_info": case_value['request_info'], "case_info": value})
        return new_case

    def write_extra_yaml(self, data):
        with open(self.data_path + "extract.yaml", mode='a', encoding='utf8') as f:
            # 读取之前yaml的内容
            old_value = self.read_extract_yaml()
            if old_value:
                # 和新传入的数据做结合
                for key,value in data.items():
                    old_value[key] = value
                # 清空数据
                self.clear_extract_yaml()
                # 写入新数据
                yaml.dump(data=old_value, stream=f, allow_unicode=True, sort_keys=False)
            else:
                yaml.dump(data=data, stream=f, allow_unicode=True, sort_keys=False)

    def clear_extract_yaml(self):
        """清理extract.yaml"""
        with open(self.data_path + "extract.yaml", mode='w', encoding='utf8') as f:
            f.truncate()



if __name__ == '__main__':
    # data = YamlUtil().extract_case("user_center.yaml", 'user_login_new')
    # print(data)

    data = {"code2": 300, "data": {"id": 3386, "address": "北京市朝阳区"}}
    YamlUtil().write_extra_yaml(data)
    # print(YamlUtil().read_extract_yaml())