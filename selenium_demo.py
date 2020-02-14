from selenium import webdriver
#设置driver路径时直接放到项目目录下
browser = webdriver.Chrome(executable_path="E:\pyworkspace\ScrapyLearn\chromedriver.exe")
#模拟请求，请求数据
test_url = "https://www.hao123.com/"
test_content = browser.get(test_url)
test_element = browser.find_element_by_css_selector("body")
print(test_element.text)
#以上方式简化了爬虫向服务器的请求方式，未使用requests，bs4等底层实现方式，同样可以进行交互，避免了某些极端query构造参数的情况



test_element.click()
