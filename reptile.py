import requests
from PIL import Image
from bs4 import BeautifulSoup

# 引入selenium
from selenium import webdriver

response = requests.get('http://hanlp.com/')
soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
iframes = soup.find_all('iframe')

# 使用webkit无界面浏览器
# 如果路径为 exe 启动程序的路径，那么该路径需要加一个 r
driver = webdriver.PhantomJS(executable_path=r'F:/CodeSoftware/phantomjs/bin/phantomjs.exe')
# 获取指定网页的数据  start_urls
driver.get(iframes[1]['src'])
driver.maximize_window()

element = driver.find_element_by_class_name('hasSVG')
left = element.location['x']
top = element.location['y']
right = element.location['x'] + 540
bottom = element.location['y'] + 130

driver.save_screenshot('E:/Projects/PyCharmProjects/GitHub/TripleIE/images/1.png')
driver.close()

im = Image.open('E:/Projects/PyCharmProjects/GitHub/TripleIE/images/1.png')
im = im.crop((left, top, right, bottom))
im.save('E:/Projects/PyCharmProjects/GitHub/TripleIE/images/1.png')
