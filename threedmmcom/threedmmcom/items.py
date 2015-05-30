# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThreedmmcomItem(scrapy.Item):
	thread_url = scrapy.Field()
	thread_id = scrapy.Field()
	name = scrapy.Field()
	files = scrapy.Field()
	meta = scrapy.Field()
