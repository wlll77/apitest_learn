import requests

a = {"type":"movie", "tag": "热门", "page_limit": 50, "page_start": 0}
b = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

r = requests.get("https://movie.douban.com/j/search_subjects",params=a,headers= b)
print(r.status_code)
print(r.json())