# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HdcrawlPipeline(object):
    def open_spider(self, spider):
        self.data = []

    def process_item(self, item, spider):
        self.data.append(item)
        return item
    
    def close_spider(self, spider):
        with open("imgs.json", "w") as f:
            f.write(json.dumps(self.data, ensure_ascii=False))
