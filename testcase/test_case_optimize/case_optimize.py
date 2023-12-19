import pytest
import requests

from api.api import mobile_query
from utils.read import base_data

url = base_data.read_ini()['host']['api_sit_url']


def test_mobile():
    params = base_data.read_data()['mobile_belong']
    print("测试手机归属地get请求")
    result = mobile_query(params)
    assert result.success is True
    assert result.body['status'] == 0
    assert result.body['msg'] == "ok"
    # assert result['result']["shouji"] == "13456755448"
    assert result.body['result']["province"] == "北京"
    assert result.body['result']["company"] == "中国移动"
    assert result.body['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
