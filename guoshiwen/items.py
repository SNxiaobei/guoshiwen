# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuoshiwenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 诗的标题
    poetry = scrapy.Field()
    # 诗题的url
    poetry_url = scrapy.Field()
    # 朝代
    dynasty = scrapy.Field()
    # 诗人
    poet = scrapy.Field()
    # 诗文
    title = scrapy.Field()
    # 爬取的数量
    # num = scrapy.Field()


class DetailItem(scrapy.Item):
    # 译文
    translation = scrapy.Field()
    # 注释
    annotation = scrapy.Field()
    # 赏析
    appreciation = scrapy.Field()
    # 创作背景
    creation_background = scrapy.Field()
