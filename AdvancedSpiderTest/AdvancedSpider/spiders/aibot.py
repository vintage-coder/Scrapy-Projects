import csv
import scrapy
try:
    from urllib2 import urlparse
except:
    from urllib.parse import urlparse
from scrapy.http import Request
from AdvancedSpider.items import AdvancedspiderItem



class AibotSpider(scrapy.Spider):
    name = 'aibot'
    allowed_domains =[ ]
    start_urls = [ ]
    domains=[]
    handle_httpstatus_list = [403, 404]
    urlsfile = open("base.csv", 'r')
    reader=csv.reader(urlsfile)
    data={}
    for row in reader:
        if len(row)==0:
            break

        print(row[0],'==============',row[1])
        urlsA=urlparse(row[0]).netloc
        if urlsA.startswith('www'):
            urls=urlsA.split('www.')[1]
            allowed_domains.append(urls)
            temp=urlsA.split('.')
            data[temp[1]]=row[1]
        else:
            allowed_domains.append(urlsA)
            temp=urlsA.split('.')
            data[temp[0]]=row[1]
        domains.append(row[1])
        start_urls.append("http://"+urlsA+"/")




    urlsfile.close()
    print("=================the start urls",start_urls)
    print("==================the allowed domains",allowed_domains)
    print("===================the domains",domains)

    valid_url = []
    invalid_url = []
    count=0
    maxdepth =7
    domain = ''


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse)
    

    def parse(self, response):

        from_url = ''
        from_text = ''
        depth = 0

        if 'from' in response.meta: from_url = response.meta['from']
        if 'text' in response.meta: from_text = response.meta['text']
        if 'depth' in response.meta: depth = response.meta['depth']



        if response.status in [404, 400, 301, 302, 500]:
            self.invalid_url.append({'url': response.url,
                                     'from': from_url,
                                     'text': from_text})
        else:

            self.valid_url.append({'url': response.url,
                                   'from': from_url,
                                   'text': from_text})


            gowtham=AdvancedspiderItem()
            gowtham['urls']=response.url
            yield  gowtham

            print(depth, response.url, '<-', from_url, from_text)

            with open('dir_test.txt', 'a+') as f:
                AibotSpider.count += 1
                if AibotSpider.count <= 500000:
                    print('count=%d depth=%d' % (AibotSpider.count, depth), response.url, '<-', from_url, from_text, sep=' ')
            
                    f.write('%s \r\n' % (response.url))
            

            if depth < self.maxdepth:

                a_selectors = response.xpath("//a")

                for selector in a_selectors:
                    text = selector.xpath('text()').extract_first()

                    link = selector.xpath('@href').extract_first()

                    request = response.follow(link, callback=self.parse)
                    request.meta['from'] = response.url
                    request.meta['text'] = text
                    request.meta['depth']=depth+1

                    yield request

