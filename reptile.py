import requests
from PIL import Image
from bs4 import BeautifulSoup

# 引入selenium
from selenium import webdriver


def getQuestions(dir):
    questions = []
    with open(dir, 'r', encoding='utf-8') as f:
        for line in f:
            questions.append(line.strip())

    return questions


questions = getQuestions('data/question.txt')

for (i, question) in enumerate(questions):
    print('====== Start Create Image_%s ======' % i)

    response = requests.get('http://hanlp.com/?sentence=' + question)
    soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
    iframes = soup.find_all('iframe')

    # 使用webkit无界面浏览器
    # 如果路径为 exe 启动程序的路径，那么该路径需要加一个 r
    driver = webdriver.PhantomJS()
    driver.set_window_size(660, 130)
    # 获取指定网页的数据  start_urls
    driver.get(iframes[1]['src'])
    driver.maximize_window()

    element = driver.find_element_by_class_name('hasSVG')
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + 660
    bottom = element.location['y'] + 130

    driver.save_screenshot('images/%s.png' % i)
    driver.close()

    im = Image.open('images/%s.png' % i)
    im = im.crop((left, top, right, bottom))
    im.save('images/%s.png' % i)
