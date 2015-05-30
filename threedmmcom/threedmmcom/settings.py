# -*- coding: utf-8 -*-

# Scrapy settings for threedmmcom project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'threedmmcom'

SPIDER_MODULES = ['threedmmcom.spiders']
NEWSPIDER_MODULE = 'threedmmcom.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'FooneBot (+http://3dmm.tv/)'

FEED_FORMAT = 'json'
FEED_URI = 'movies.json'