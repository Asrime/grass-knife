# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class ImgscrapyPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

	# def file_path(self, request, response = None, info = None):
	# 	images_path_name = request.meta['item']['images_folder_name']
	# 	path = 'http://codesawllow.cn' + request.url
	# 	print(path)
	# 	return path

	# def item_completed(self, results, item, info):
	# 	image_path = [x['path'] for ok, x in results if ok] ##
	# 	if not image_path:
	# 		raise DropItem('Item contains no images')
	# 	item['images_folder_name'] = image_path
	# 	return item
    # def process_item(self, item, spider):
    #     return item
