import os
import MySQLdb
import logging



class AdvancedspiderPipeline(object):
    def __init__(self):
        print('This is the init method ==================')
        self.connection=MySQLdb.connect("localhost","root","gowthaman","scrapy")
        print("connection status:",self.connection)
        self.conn=self.connection.cursor()
        print('Database connection Established')

    def process_item(self, item, spider):
        print("===============================process_item==========================================")
        print("================",item['urls'])
        try:
            self.conn.execute("insert into wmberg (urls) values('%s')"%(item['urls']))
            self.connection.commit()

        except Exception as Error:
            logging.log(Error)

        return item
    def close_spider(self, spider):
        self.conn.close()
        self.connection.close()


class UrlStoragePipeline(object):
    def __init__(self):
        print('======This is the FileStoragePipeLine======')

    def process_item(self,item,spider):

        self.inserting_urls(item,spider)



    def inserting_urls(self,item,spider):
        path = os.getcwd()
        print('The item is :',item['urls'])
        for i, j in spider.data.items():
            if i in item['urls']:
                os.chdir(path + '/' + j)
                with open(i, 'a+') as file:
                    file.write('%s \r\n' % item['urls'])
                os.chdir(path)
            else:
                pass


    def close_spider(self,spider):
        pass