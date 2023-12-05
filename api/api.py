import requests

from core.api_util import api_util





def mobile_query(params):
    response = api_util.get_mobile_belong(params=params)
    return response.json()

def test_json(json_data):
    """
    这个方法测试json传参
    :param json_data:
    :return:
    """
    response = api_util.post_data(json=json_data)
    return response.json()