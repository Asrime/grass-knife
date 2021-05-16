import scrapy
from imgScrapy.items import PageItem, ImgItem

url_prefix = "http://xyz.net/page/{}"

class ImgspiderSpider(scrapy.Spider):
    name = 'imgSpider'
    allowed_domains = ['xyz.net']
    # start_urls = ['http://xyz.net']
    start_urls = [url_prefix.format(i) for i in range(1,100)]

    def parse(self, response):
    	print('page.url:' + response.url)
    	for page_url in response.xpath('//div[@class="post-field-left box list"]'):
    		item = PageItem()
	    	item['urls'] = page_url.xpath('a/@href').extract()
	    	print(item['urls'])
	    	for url in item['urls']:
	    		yield scrapy.Request(url, callback = self.img_parse)

    def img_parse(self, response):
    	print('imageindex.url:' + response.url)
    	title = response.xpath('//title/text()').extract_first()
    	for img_url in response.xpath('//img'):
        	item = ImgItem()
        	item['urls'] = img_url.xpath('@src').extract()
        	item['dirname'] = title
        	item['filename'] = img_url.xpath('@alt').extract_first()
        	yield item