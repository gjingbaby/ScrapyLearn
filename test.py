import requests
from bs4 import BeautifulSoup

target_url = "https://xa.fang.lianjia.com/"

url_content = requests.get(target_url).content

content_soup = BeautifulSoup(url_content,"html.parser")
print(content_soup.title)