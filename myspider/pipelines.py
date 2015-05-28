# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from car.models import *

class MyspiderPipeline(object):
    def process_item(self, item, xin):
        car = Car.objects.get_or_create(
            city = item['city'],
            brand = item['brand'],
            types = item['types'],
            car_time = item['car_time'],
            mileage = item['mileage'],
            car_price = item['car_price'],
            image_url = item['image_url'],
            car_url = item['car_url'],
            model = item['model'],
            transmission_mode = item['transmission_mode'],
            have_accident = item['have_accident']
        )
        return item
