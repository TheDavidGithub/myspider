# -*- coding: utf-8 -*-
import scrapy
import urlparse
from myspider.items import MyspiderItem

class XinSpider(scrapy.spider.Spider):
    name = "xin"
    allowed_domains = ["www.xin.com"]
    start_urls = [
        "http://www.xin.com/quanguo/s/o2a10i8393v1/"
    ]

    def parse(self, response):
        car_list = response.xpath(
            "//div[@id=\"search_container\"]/div[@class=\"car-box clearfix\"]/div[@class=\"car-vtc vtc-border \"]"
        )
        for car in car_list:
            item = MyspiderItem()
            image_url = car.xpath("./div[@class=\"vtc-img\"]/a/img/@src").extract()
            if image_url:
                item["image_url"] = image_url[0]
            title_list = car.xpath("./div[@class=\"vtc-info\"]/p/a/@title").extract()
            if title_list:
                title = title_list[0].split()
                if len(title) > 0:
                    item["brand"] = title[0]
                if len(title) > 1:
                    item["types"] = title[1]
                if len(title) > 2:
                    item["model"] = ' '.join(title[2:])
            car_url = car.xpath("./div[@class=\"vtc-info\"]/p/a/@href").extract()
            if car_url:
                item["car_url"] = urlparse.urljoin(response.url, car_url[0])
            box = car.xpath("./div[@class=\"vtc-info\"]/div[@class=\"box\"]/ul/li/text()").extract()
            if len(box) == 4:
                item["car_time"] = box[0]
                item["mileage"] = box[1]
                item["transmission_mode"] = box[2]
                item["city"] = box[3]
            have_accident = car.xpath("./div[@class=\"vtc-info\"]/div[@class=\"back\"]").extract()
            if have_accident:
                item["have_accident"] = "False"
            else:
                item["have_accident"] = "True"
            car_price = car.xpath("./div[@class=\"vtc-money\"]/em/text()").extract()
            if car_price:
                item["car_price"] = car_price[0]
            yield item

        a_list = response.xpath("//div[@class=\"con-page search_page_link\"]/a")
        for a in a_list:
            if ''.join(a.xpath("./text()").extract()).strip() == u'下一页':
                next_page = ''.join(a.xpath("./@data-page").extract()).strip()
                if next_page:
                    next_page_url = 'http://www.xin.com/quanguo/s/' + 'o2a10i'+next_page+'v1/'
                    yield scrapy.Request(next_page_url,callback=self.parse)
