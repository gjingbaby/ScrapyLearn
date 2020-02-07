import requests
import json
import os
import time
log_file = "log.txt"
target_url = "http://query.sse.com.cn/security/stock/queryCompanyBulletin.do?jsonCallBack=jsonpCallback3674&isPagination=true&productId=&securityType=0101%2C120100%2C020100%2C020200%2C120200&reportType2=LSGG&reportType=FXSSGG&beginDate=2020-01-17&endDate=2020-01-23&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5&_=1581086651599"
headers = {"Referer": "http://www.sse.com.cn/disclosure/listedinfo/listing/",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
def notice_download(target_url,headers,log_file):
    url_response = requests.get(target_url,headers=headers)
    #获取json数据
    json_response = json.loads(url_response.text[18:-1])
    for item in json_response["result"]:
        pdf_url = "http://static.sse.com.cn"+item["URL"]
        pdf_content = requests.get(pdf_url).content
        pdf_title = item["TITLE"] + ".pdf"
        #检测路径，创建路径
        filepath = r"C:\Users\Administrator\Desktop\notice"
        if not os.path.isdir(filepath):
            os.mkdir(filepath)
        #拼接文件路径
        filename = os.path.join(filepath,pdf_title)
        #下载文件
        with open(filename,"wb") as f:
            f.write(pdf_content)
        f.close()
        #日志文件
        with open(log_file,"a") as l:
            l.write(time.asctime()+"下载成功"+pdf_title+pdf_url+"\n")
        l.close()
        print("已下载完成"+pdf_title)

if __name__ == "__main__":
    notice_download(target_url,headers,log_file)