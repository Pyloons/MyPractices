# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis, json


class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        item_dict = {
            'url': item['url'],
            'name': item['name'],
            'summary': item['summary'],
            'score': item['score']
        }
        self.r.lpush('has_crawled', item['url'])
        if float(item_dict['score']) >= 8.0:
            self.r.lpush('douban_movie:items', json.dumps(item_dict))
        return item

    def open_spider(self, spider):
        self.r = redis.Redis(host='localhost', port=6379)

