# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem
import re


class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/1.0/']

    rules = (
        Rule(LinkExtractor(allow='[^http|\.].*?\/',), callback='parse_page'),
    )

    def parse_page(self, response):
        item = PageItem()
        item['url'] = response.url
        nom = re.sub('<[^>]*>', ' ', response.text)
        nos = re.sub('\s+', ' ', nom)
        item['text'] = nos
        yield item

