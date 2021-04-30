import scrapy

from myScrapy.items import MyscrapyItem

url_prefix = "http://xyz.com/Default/Contents/{}"

class GameSpider(scrapy.Spider):
	name = "game"
	allowed_domains = ["xyz.com"]
	start_urls = [
		url_prefix.format(i) for i in range(9754,9999)
	]
	custom_setting = {
		'DEFAULT_REQUESTZ_HEADERS' : {
			'Referer' : 'http://xyz.com/',
			'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)'
		}
	}

	def parse(self, response):
		for sel in response.xpath('//article'):
			item = MyscrapyItem()
			item['title'] = sel.xpath('h1/text()').extract()
			item['downLoadLink'] = sel.xpath('div/div/span/a/@href').extract()
			item['password'] = sel.xpath('div/div/span/font/text()').extract()
			yield item