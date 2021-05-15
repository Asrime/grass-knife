import scrapy
from imgScrapy.items import ImgscrapyItem

class ImgspiderSpider(scrapy.Spider):
    name = 'imgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
    	item = ImgscrapyItem()
    	urls = response.css(".post img::attr(src)").extract()
    	item['image_urls'] = urls
    	yield item
    	pass