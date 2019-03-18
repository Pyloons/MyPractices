# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import redis
import json


class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        item_dict = {
            'url': item['url'],
            'text': item['text']
        }
        item_json = json.dumps(item_dict)
        self.r.lpush('flask_doc:items', item_json)
        return item

    def open_spider(self, spider):
        self.r = redis.StrictRedis(host='localhost', port=6379)
