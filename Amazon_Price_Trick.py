import requests
from bs4 import BeautifulSoup
import time
import random

target_url = "https://www.amazon.cn/dp/B07YMNLXL3/ref=lp_665002051_1_1?s=wireless&ie=UTF8&qid=1580980278&sr=1-1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
def price_trick(target_url,headers):
    url_content = requests.get(target_url,headers = headers)
    content_soup = BeautifulSoup(url_content.content,"html.parser")
    target_price = content_soup.find("span",{"id":"priceblock_ourprice"})
    target_title = content_soup.select("#productTitle")[0]

    print(target_title.text.strip()+"\n"+target_price.text)

while True:
    price_trick(target_url,headers)
    sleeptime = random.randint(1,100)
    print(sleeptime)
    time.sleep(sleeptime)

