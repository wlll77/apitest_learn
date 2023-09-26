import requests

def test_mobile():
    params = {
        "shouji": "13456755448",
        "appkey":"0c818521d38759e1"
    }
    r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query", params=params)
    # r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query", params={"shouji": "13456755448","appkey":"0c818521d38759e1"})  #还可以这样写，直接把params写进去
    # print(r.status_code)
    # print(r.json())
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "北京"
    assert result['result']["company"] == "中国移动"
    assert result['result']["areacode"] == "0571"

def test_mobile_post():
    params = {
        "shouji": "13456755448",
        "appkey":"0c818521d38759e1"
    }
    r = requests.post(url="http://sellshop.5istudy.online/sell/shouji/query",params=params)
    print(r.status_code)
    print(r.json())
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "北京"
    assert result['result']["company"] == "中国移动"
    assert result['result']["areacode"] == "0571"