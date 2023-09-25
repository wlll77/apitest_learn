import requests
params = {
    "shouji": "13456755448",
    "appkey":"0c818521d38759e1"
}
r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query", params=params)
# r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query", params={"shouji": "13456755448","appkey":"0c818521d38759e1"})  #还可以这样写，直接把params写进去
print(r.status_code)
print(r.json())