# -*-coding:utf-8 -*-
from time import sleep
import json
from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

article_list = []

def get_article(source):
    global article_list
    soup = BeautifulSoup(source)
    for div in soup.find_all(class_="post-outer"):
        # print("%s"%div.a.text.encode("big5"))
        temp = {}
        temp["name"] = div.a.text.encode("utf-8")
        temp["url"] = div.a["href"].encode("utf-8")
        article_list.append(temp)

browser = webdriver.Firefox()
browser.get("http://hornydragon.blogspot.com/search/label/雜七雜八短篇漫畫翻譯")
get_article(browser.page_source)
browser.find_element_by_css_selector("span > b").click()
get_article(browser.page_source)

try:
    page_num = 5
    while True:
        browser.find_element_by_link_text(str(page_num)).click()
        sleep(3)
        get_article(browser.page_source)
        page_num += 1
except NoSuchElementException:
    print("stop in " + page_num)

browser.close()

with open("articles.json","w") as f:
    f.write(json.dumps(article_list, ensure_ascii=False))