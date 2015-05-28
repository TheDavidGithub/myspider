# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
    city = scrapy.Field()
    brand = scrapy.Field()
    types = scrapy.Field()
    car_time = scrapy.Field()
    mileage = scrapy.Field()
    car_price = scrapy.Field()
    image_url = scrapy.Field()
    car_url = scrapy.Field()
    model = scrapy.Field()
    transmission_mode = scrapy.Field()
    have_accident = scrapy.Field()
