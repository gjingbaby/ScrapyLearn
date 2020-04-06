
# import requests
# from bs4 import BeautifulSoup
#
# target_url = "https://xa.fang.lianjia.com/"
#
# url_content = requests.get(target_url).content
#
# content_soup = BeautifulSoup(url_content,"html.parser")
# print(content_soup.title)

'''
http://query.sse.com.cn/security/stock/queryCompanyBulletin.do?
jsonCallBack=jsonpCallback49696&
isPagination=true&
productId=600068&
keyWord=&
securityType=0101%2C120100%2C020100%2C020200%2C120200
reportType2=&
reportType=ALL&\
beginDate=2017-02-06&\
endDate=2020-02-06&\
pageHelp.pageSize=25&\
pageHelp.pageCount=50&\
pageHelp.pageNo=1&\
pageHelp.beginPage=1&\
pageHelp.cacheSize=1&\
pageHelp.endPage=5&\
_=1580987782279
'''

'''
import numpy as np
#
# universe = np.zeros((30,30))
# moon = [[1,1,0,0],
#         [1,1,1,0],
#         [0,0,1,1],
#         [0,0,1,1]]
#
# earth = [[1,1,0,0,1],
#         [1,1,1,0,1],
#         [0,0,1,1,1],
#         [0,0,1,1,1]]
# #此处的位置moon是从y轴11-14，x轴12-15，同理earth，实际就是从i+1到j
# universe[10:14,11:15] = moon
# universe[16:20,17:22] = earth
#
# print(universe)

str = "hello"

print(str.isalpha())

str1 = "你好，America"
print(str1.isalpha())


print(ord("9"))

message = "gjingbaby"
num = message.find("g")
print(num)


print(chr(95))

li = [1]
li.insert(0,0)
ls = li
print(ls)


ipt = input('Please Input Integer：')
ipt_num = int(ipt)
ipt_flt = float(ipt)

print(ipt_num,ipt_flt)
'''

str = '中国'
s1 = str.encode('gbk')    #以gbk格式对str编码，获得bytes类型对象
print(type(s1))
print(s1)

s2 = s1.decode('gbk')     #以gbk格式对s1解码，获得unicode格式的str
print(s2)
print(type(s2))



