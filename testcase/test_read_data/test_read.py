import pytest
import requests

from utils.read import base_data

url =base_data.read_ini()['host']['api_sit_url']

def test_mobile():
    params = base_data.read_data()['mobile_belong']
    r = requests.get(url + "/shouji/query", params=params)
    # r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query", params={"shouji": "13456755448","appkey":"0c818521d38759e1"})  #还可以这样写，直接把params写进去
    # print(r.status_code)
    # print(r.json())
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    # assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "北京"
    assert result['result']["company"] == "中国移动"
    assert result['result']["areacode"] == "0571"
