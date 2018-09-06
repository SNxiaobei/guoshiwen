# -*- coding: utf-8 -*-
import random
from guoshiwen.settings import USER_AGENT_LIST

class User_AgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        print(user_agent)
        request.headers["User-Agent"] = user_agent

        spider.logger.debug("--" * 50)
        spider.logger.warning("--" * 50)
        # 注意不要return request给引擎，不然引擎会认为是下载失败的请求，会重新加入调度器请求队列


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # 免费代理格式
        # proxy = "http//：115.28.141.184.16816"
        # 付费代理格式
        proxy = "http://maozhaojun:ntkn0npx@115.28.141.184:16816"
        # scrapy的request对象提供了meta字典的键proxy来储存代理信息
        request.meta['proxy'] = proxy