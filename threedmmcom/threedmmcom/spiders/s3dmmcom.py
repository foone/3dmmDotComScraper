
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from threedmmcom.items import ThreedmmcomItem
from w3lib.url import url_query_parameter

def firstOrNone(xp):
	try:
		return xp.extract()[0]
	except IndexError:
		return None


class S3dmmcomSpider(CrawlSpider):
	name = 's3dmmcom'
	allowed_domains = ['3dmm.com']
	start_urls = ['http://3dmm.com/forumdisplay.php?f=6']

	rules = [
		Rule(LxmlLinkExtractor(allow=r'showthread\.php\?(.*)\bt=',deny='(page=)|(#)|(\?p=)|(#post)|(goto=lastpost)'), callback='movie_page', follow=False),
	]

	def movie_page(self, response):

		hxs = Selector(response)
		item = ThreedmmcomItem()
		item['thread_url'] = response.url
		item['thread_id'] = url_query_parameter(response.url, 't')
		item['name'] = firstOrNone(hxs.select('//div[@class="bigusername"]/text()'))
		files = item['files'] = hxs.select('//a[@data-location]/@data-location').extract()
		if not files:
			return

		meta=item['meta']={}

		metadivs=response.xpath('//table[starts-with(@id,"post")]//td[@class="alt1" and @width="125"]/div')
		for i,entry in enumerate(metadivs):
			name=firstOrNone(entry.css('div.smallfont').xpath('text()'))
			if name and i<len(metadivs)-2:
				meta[name]=firstOrNone(metadivs[i+1].xpath('./descendant-or-self::*[name() != "script" and name() != "style"]/text()[normalize-space()]'))
		version=response.xpath('//table[starts-with(@id,"post")]//td[@class="alt1" and @width="125"]/table/tr[1]//strong/text()').extract()
		if version:
			item['meta']['version']=version[0].strip()

		return item

class S3dmmcomAllPagesSpider(S3dmmcomSpider):
	name = 's3dmmcomAllPages'

	rules = S3dmmcomSpider.rules + [
		Rule(LxmlLinkExtractor(allow=r'forumdisplay\.php\?(.*)\bf=6\b(.*)\bpage='),),
	]
