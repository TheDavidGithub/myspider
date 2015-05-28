# -*- coding: utf-8 -*-

# Scrapy settings for myspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
import sys
sys.path.append('/home/lsj/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

BOT_NAME = 'myspider'

SPIDER_MODULES = ['myspider.spiders']
NEWSPIDER_MODULE = 'myspider.spiders'

ITEM_PIPELINES = {
    'myspider.pipelines.MyspiderPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myspider (+http://www.yourdomain.com)'
