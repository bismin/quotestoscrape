# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class QuotestoscrapeSpider(scrapy.Spider):
    name = 'quotestoscrape'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        jobs=response.xpath('//div[@class="quote"]')
        for job in jobs:
        	text=job.xpath('span[@class="text"]/text()').extract_first()
        	author=job.xpath('span/small[@class="author"]/text()').extract_first()
        	tags=job.xpath('div[@class="tags"]/a[@class="tag"]/text()').extract()
        	yield{'text':text,'author':author,'tags':tags}

    	relative_next_url = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').extract_first()
    	absolute_next_url = response.urljoin(relative_next_url)
    	yield{'absolute_next_url':absolute_next_url}
    	yield Request(absolute_next_url,callback=self.parse)
