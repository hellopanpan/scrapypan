# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

from scrapypan.items import ScrapypanItem
from scrapypan.items import LianItem

class DoubanPipeline(object):
    # 初始化
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        self.mydb = client[dbname]
        # 存放数据的数据库表名
        # self.post = mydb[sheetname]

    def process_item(self, item, spider):
        if(isinstance(item, ScrapypanItem)):
            # item (Item 对象) – 被爬取的item
            # spider (Spider 对象) – 爬取该item的spider
            # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
            # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
            data = dict(item)
            self.mydb['movies'].insert(data)
            return item
        elif(isinstance(item, LianItem)):
            # item (Item 对象) – 被爬取的item
            # spider (Spider 对象) – 爬取该item的spider
            # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
            # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
            data = dict(item)
            self.mydb['more'].insert(data)
            return item