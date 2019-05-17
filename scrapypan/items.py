# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapypanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    more = scrapy.Field()
    unit = scrapy.Field()
class LianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pic = scrapy.Field()
