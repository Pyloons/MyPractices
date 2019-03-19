# -*- coding: utf-8 -*-
import scrapy, redis
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from douban_movie.items import MovieItem


class AwesomeMovieSpider(CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']
    r = redis.Redis(host='localhost', port=6379)

    rules = (
        Rule(LinkExtractor(allow='https://movie.douban.com/subject/\d+/\?from=subject-page'), callback='parse_page'),
    )

    def parse_movie_item(self, response):
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first()
        item['summary'] = response.xpath('//span[@property="v:summary"]/text()').extract_first().strip()
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()
        return item

    def parse_start_url(self, response):
        yield self.parse_movie_item(response)

    def parse_page(self, response):
        if self.r.llen('douban_movie:items') > 35:
            raise CloseSpider('above 30 items is enough...')
        urls = response.xpath('//*[@class="recommendations-bd"]/dl/dt/a/@href').extract()
        has_crawled = self.r.lrange('has_crawled', 0, -1)
        for url in urls:
            if url not in has_crawled:
                yield scrapy.Request(url, self.parse_page)
        yield self.parse_movie_item(response)

