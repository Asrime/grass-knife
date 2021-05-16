# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urls = scrapy.Field()
    # pages = scrapy.Field()
    # image_title = scrapy.Field()
    pass

class ImgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urls = scrapy.Field()
    dirname = scrapy.Field()
    filename = scrapy.Field()

    # pages = scrapy.Field()
    # image_title = scrapy.Field()
    pass