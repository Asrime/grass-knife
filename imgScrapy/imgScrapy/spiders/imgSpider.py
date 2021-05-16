import scrapy
from imgScrapy.items import ImgscrapyItem

class ImgspiderSpider(scrapy.Spider):
    name = 'imgSpider'
    allowed_domains = ['xyz.net']
    start_urls = ['http://xyz.net']

    def parse(self, response):
    	for url in response.xpath('//img'):
    		item = ImgscrapyItem()
	    	item['image_urls'] = url.xpath('@src').extract()
	    	yield item