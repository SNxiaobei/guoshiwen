# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from guoshiwen.items import GuoshiwenItem,DetailItem


class GuoshiwenPipeline(object):
    def open_spider(self, spider):
        self.f = open('shiwen.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, GuoshiwenItem):
            # # print(type(item),"I"*10)
            # dict_data = dict(item)
            # print(dict_data)
            # # print(type(dict_data), 'p'*30)
            # data = dict_data["title"]
            # print(data)
            # str_data = ''.join(data)
            # print(type(str_data),'1'*30)
            # self.f.write(str_data)
            json_item = json.dumps(dict(item)) + ',\n'
            self.f.write(json_item.encode().decode("unicode-escape"))
        return item


    def close_spider(self, spider):
        self.f.close()


class DetailPipeline(object):
    def open_spider(self, spider):
        self.f = open('wen.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, DetailItem):
            json_item = json.dumps(dict(item)) + ',\n'
            self.f.write(json_item.encode().decode("unicode-escape"))
        return item

    def close_spider(self, spider):
        self.f.close()
