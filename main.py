from wsgiref import headers
import requests
from bs4 import BeautifulSoup

def pasr(url):
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }

    req = requests.get(url, headers = headers)

    with open("study.html", "w", encoding='utf-8') as file:
        file.write(req.text)




pasr("https://www.youtube.com/")