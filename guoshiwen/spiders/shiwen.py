# -*- coding: utf-8 -*-
import scrapy
from guoshiwen.items import GuoshiwenItem, DetailItem


class ShiwenSpider(scrapy.Spider):
    name = 'shiwen'
    allowed_domains = ['gushiwen.org',]
    start_urls = ['https://www.gushiwen.org/default_1.aspx']
    # start_urls = ['https://www.gushiwen.org/default_%s.aspx'% str(page) for page in range(1, 101)]

    def parse(self, response):
        list_data = response.xpath("//div[@class='left']/div/div[@class='cont']")
        for data in list_data:

            item = GuoshiwenItem()
            poetry = data.xpath("./p/a/b/text()").extract_first()
            if poetry:
                item['poetry'] = poetry
            poetry_url = data.xpath("./p[1]/a/@href").extract_first()

            if poetry:
                item['poetry_url'] = poetry_url
            dynasty = data.xpath("./p/a[1]/text()").extract_first()
            if dynasty:
                item['dynasty'] = dynasty
            poet = data.xpath("./p/a[2]/text()").extract_first()
            if poet:
                item['poet'] = poet
            title = data.xpath("./div[@class='contson']/text() | ./div[@class='contson']/p/text()").extract()
            if title:
                strs = ','.join(title)
                item['title'] = strs.replace('，',',').replace('。','.').replace('\n,','').replace('.,','.').strip()
                # print(item['poetry_url'])
            # num += 1
            # item['num'] = "gushi>>>>>>%d"%num
            # global num
            # 访问详情类，调用detail函数
            yield item
            yield scrapy.Request(url=item['poetry_url'], callback=self.detail)

            # yield scrapy.Request(item['poetry_url'], meta={'shi_item' : item}, callback=self.detail)


    def detail(self, response):
        item = DetailItem()
        # item = response.meta['shi_item']
        # 译文
        translation = response.xpath("//div[@class='left']/div[3]/div[@class='contyishang']/p[1]/text()").extract()
        print(translation)
        if translation:
            item['translation'] = translation
        else:
            item['translation'] = None
        # 注释
        annotation = response.xpath("//div[@class='left']/div[3]/div[@class='contyishang']/p[2]/text()").extract()
        if annotation:
            item['annotation'] = annotation
        else:
            item['annotation'] = response.xpath("//div[@class='left']/div[3]/div[1]/text()").extract()
        # 赏析
        appreciation = response.xpath("//div[@class='left']/div[5]/div/p/text()").extract()
        if appreciation:
            item['appreciation'] = appreciation
        else:
            item['appreciation'] = response.xpath("//div[@class='left']/div[4]/div[1]/p/text()")
        # 创作背景
        creation_background = response.xpath("//div[@class='left']/div[7]/div[@class='contyishang']/p/text()").extract()
        if creation_background:
            item['creation_background'] = creation_background
        else:
            item['creation_background'] = None
        translation_str = ''.join(translation)
        annotation_str = ''.join(annotation)
        appreciation_str = ''.join(appreciation)
        creation_background_str = ''.join(creation_background)
        item['translation'] = translation_str.replace('，',',').replace('。','.').replace('\n,','').replace('.,','.').strip()
        item['annotation'] = annotation_str.replace('，',',').replace('。','.').replace('\n,','').replace('.,','.').strip()
        item['appreciation'] = appreciation_str.replace('，',',').replace('。','.').replace('\n,','').replace('.,','.').strip()
        item['creation_background'] = creation_background_str.replace('，',',').replace('。','.').replace('\n,','').replace('.,','.').strip()

        yield item