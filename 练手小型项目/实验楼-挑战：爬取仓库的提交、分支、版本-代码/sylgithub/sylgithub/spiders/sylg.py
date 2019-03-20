# -*- coding: utf-8 -*-
import scrapy
from sylgithub.items import SylgithubItem


class SylgSpider(scrapy.Spider):
    name = 'sylg'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for repo in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            item = SylgithubItem()
            name_path = './/div[1]/div[1]/h3/a/text()'
            item['name'] = repo.xpath(name_path).extract_first().strip()
            time_path = './/div[1]/div[3]/relative-time/@datetime'
            item['update_time'] = repo.xpath(time_path).extract_first()
            
            more_url = './/div[1]/div[1]/h3/a/@href'
            more_url = repo.xpath(more_url).extract_first()
            more_url = response.urljoin(more_url)

            more_request = scrapy.Request(more_url, callback=self.more_parse)
            more_request.meta['item'] = item
            yield more_request

        follow_url = '//*[@id="user-repositories-list"]/div/div/a[contains(text(),"Next")]/@href'
        follow_url = response.xpath(follow_url).extract_first()
        if follow_url:
            yield response.follow(follow_url, callback=self.parse)

    def more_parse(self, response):
        item = response.meta['item']
        empty_tag = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div/h3/text()')
        if empty_tag and 'empty' in empty_tag.extract_first():
            item['commits'] = "-1"
            item['branches'] = "-1"
            item['releases'] = "-1"
        else:
            xpaths = '//ul[@class="numbers-summary"]/li[{}]/a/span/text()'
            item['commits'] = response.xpath(xpaths.format(1)).extract_first().strip()
            item['branches'] = response.xpath(xpaths.format(2)).extract_first().strip()
            item['releases'] = response.xpath(xpaths.format(3)).extract_first().strip()
        yield item

