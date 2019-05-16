# -*- coding: utf-8 -*-
import scrapy
from scrapypan.items import ScrapypanItem
from scrapypan.items import LianItem
#所有爬虫的基类，用户定义的爬虫必须从这个类继承
class DmozSpider(scrapy.Spider):
  #name是spider最重要的属性，而且是必须的。
  name = "panpan"
  allowed_domains = ["cd.lianjia.com"]
  
  # 开始循环
  def start_requests(self):
    for pageIdx in range(1, 2):
      yield scrapy.Request(
        url=f'https://cd.lianjia.com/ershoufang/pg{pageIdx}tt2/',
        callback=self.parse,
        errback=self.error
      )
  # 处理返回
  def parse(self, response):
    for sel in response.xpath('//ul[contains(@class, "sellListContent")]/li'):
      item = ScrapypanItem()
      item['title'] = sel.xpath('div/div[contains(@class, "title")]/a/text()').extract()[0]
      item['link'] = sel.xpath('div/div[contains(@class, "title")]/a/@href').extract()[0]
      item['desc'] = sel.xpath('div//div[contains(@class, "houseInfo")]/text()').extract()[0]
      # yield item
      url = item['link']
      print(url)
      yield item
      yield scrapy.Request(url, callback=self.parse_item)
      
  
  def error(self, response):
    print(response)
    pass

  def parse_item(self, response):
    for res in response.xpath("//div[contains(@class, 'content')]"):
      print(res)
      item2 = LianItem()
      item2['pic'] = res.xpath("//h1/text()").extract()[0]
      yield item2