# -*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from hdcrawl.items import ArticleItem
from bs4 import BeautifulSoup

class HdSpider(CrawlSpider):
    name = "hd_img_crawler"
    start_urls = [
        "http://hornydragon.blogspot.com/search/label/雜七雜八短篇漫畫翻譯"
    ]
    rules = [
        Rule(LinkExtractor(allow=("/search/label/"), restrict_css=(".blog-pager-older-link")), callback="parse_list", follow=True)
    ]
    def parse_list(self, response):
        article_list_page = BeautifulSoup(response.body, "lxml")
        for div_a in article_list_page.select(".post-outer"):
            yield scrapy.Request(div_a.a["href"], self.parse_imgs)

    def parse_imgs(self, response):
        article_page = BeautifulSoup(response.body, "lxml")
        article = ArticleItem()
        article["name"] = article_page.find(class_="entry-title").get_text(strip=True).encode("utf-8")
        article["url"] = response.url

        article["imgs"] = []
        content = article_page.find(class_="post-body")
        for a in content.find_all("img"):
            article["imgs"].append(a["src"])
        return dict(article)