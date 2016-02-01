# -*-coding:utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup

try:
    with open("articles.json","r") as f:
        articles = json.loads(f.read())
except IOError:
    print("ERROR:run get_articles.py first.")

imgs = []

for index, article in enumerate(articles):
    res = requests.get(articles[index]["url"])
    soup = BeautifulSoup(res.text, "lxml")
    blog = soup.find(class_="post-body")
    imgs.append({})
    imgs[index]["url"] = articles[index]["url"].encode("utf-8")
    imgs[index]["name"] = articles[index]["name"].encode("utf-8")
    imgs[index]["imgs"] = []
    for img in blog.find_all("img"):
        imgs[index]["imgs"].append(img["src"].encode("utf-8"))
with open("imgs.json", "w") as f:
    f.write(json.dumps(imgs, ensure_ascii=False))