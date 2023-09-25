import requests
params = {
    "shouji": "13456755448",
    "appkey":"0c818521d38759e1"
}
r = requests.post(url="http://sellshop.5istudy.online/sell/shouji/query",params=params)
print(r.status_code)
print(r.json())