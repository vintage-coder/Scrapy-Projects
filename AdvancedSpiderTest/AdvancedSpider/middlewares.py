from scrapy import signals
import time
from urllib.parse import urlparse
import os
from os import path


class AdvancedspiderSpiderMiddleware(object):

    def __init__(self):
        print('====================================middleware init method--------------------------')

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()

        crawler.signals.connect(pipeline.engine_started, signal=signals.engine_started)
        crawler.signals.connect(pipeline.engine_stopped, signal=signals.engine_stopped)
        # crawler.signals.connect(pipeline.item_scraped, signal=signals.item_scraped)
        # crawler.signals.connect(pipeline.item_dropped, signal=signals.item_dropped)
        crawler.signals.connect(pipeline.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signal=signals.spider_closed)
        # crawler.signals.connect(pipeline.spider_idle, signal=signals.spider_idle)
        # crawler.signals.connect(pipeline.spider_error, signal=signals.spider_error)
        # crawler.signals.connect(pipeline.request_scheduled, signal=signals.request_scheduled)
        # crawler.signals.connect(pipeline.request_dropped, signal=signals.request_dropped)
        # crawler.signals.connect(pipeline.response_received, signal=signals.response_received)
        # crawler.signals.connect(pipeline.response_downloaded, signal=signals.response_downloaded)
        return pipeline
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
        print('==============================')
        print('spider opened',spider.name)
        print('=============================')


    def spider_closed(self,spider):
        spider.logger.info('spider closed: %s' % spider.name)
        print('=============================================================================')
        print('spider closed',spider)
        print('There are ',len(spider.valid_url),'valid urls and There are ',len(spider.invalid_url),'invalid urls')
        print('The invalid urls are:')
        if len(spider.invalid_url)>0:
            print('The invalid urls are......')
            for url in spider.invalid_url:
                print(url)



        print(' ======================================================================= ')

    def process_spider_input(self, response, spider):
        # print('process spider input =======================================')
        # print("The response url is:",response.url)
        # print('the response is',response.status)
        # print("================================")
        return None

    def process_spider_output(self, response, result, spider):

        # print('process spider output ===================================================================')
        # print('The response url is:',response.url)
        # print('The response is :',response.status)
        #
        # print("===========================================")

        for i in result:

            yield i





    def engine_started(self):
        print('Engine started ===============================')
        print('The time is:',time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: engine_started')
        pass


    def engine_stopped(self):
        print('Engine stopped================================')

        print('The Time is:',time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: engine_stoped')
        pass

    def custom_method(self):
        print("==============")
        print("This is custom method=========================")


    # def item_scraped(self):
    #
    #     print(time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: item scrapped')
    #     pass

    # def item_dropped(self):
    #
    #     print(time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: item_dropped')
    #     pass


    # def spider_idle(self):
    #
    #     print(time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: spider_idle')
    #     pass


    # def spider_error(self):
    #
    #     print(time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: spider error')
    #     pass


    def request_scheduled(self):
        print('Request scheduled=========================')

        print('The time is:',time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: request scheduled')
        pass


    def request_dropped(self):
        print('Request dropped==========================')
        print('The Time is:',time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: request dropped')
        pass

    # def response_received(self):
    #     print(time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: response received')
    #     pass


    # def response_downloaded(self):
    #     print(time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: response downloaded')
    #     pass

    def process_spider_exception(self, response, exception, spider):

        print('process spider exception ==================================================================')
        pass

    def process_start_requests(self, start_requests, spider):
        self.creating_directory(spider)

        for r in start_requests:
            print("The start request is :",r)
            yield r

    def creating_directory(self,spider):
        path = os.getcwd()
        print("The data is ", spider.data)
        for j, i in spider.data.items():
            if os.path.isdir(i):
                os.chdir(path + '/' + i)
                with open(j, 'w+') as file:
                    pass
                os.chdir(path)
            else:
                os.mkdir(i)
                os.chdir(path + '/' + i)
                with open(j, 'w+') as file:
                    pass
                os.chdir(path)
                print('directory was created')





class AdvancedspiderDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):

        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        print("================Download middleware  process request")
        print("The request is :",request)

        print("==============")
        return None

    def process_response(self, request, response, spider):
        print("=============Download middleware process response")

        print("The request is :",request)
        print("The response status is:",response.url)
        print("==============================")
        return response

    def process_exception(self, request, exception, spider):

        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
