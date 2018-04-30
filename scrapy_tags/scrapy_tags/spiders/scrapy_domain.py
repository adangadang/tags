#encoding:utf-8
#from scrapy_redis.spiders import scrapy.Spider
import scrapy
from ..items import data_domain_mongodb
class domainSpider(scrapy.Spider):
    name = 'domain'
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_tags.pipelines.Mgdb2Pipeline': 300
        }}
    #redis_key = 'myspider:start_urls' #从redis里面读url
    #start_urls = ['http://search.top.chinaz.com/Search.aspx?url='+redis_key]
    start_urls = ['http://search.top.chinaz.com/Search.aspx?url='+'www.ppdai.com']
    def parse(self, response):
        try:
            url_www = response.xpath("//div[@class='leftImg']/a/@href").extract_first()
        except:
            return

        yield scrapy.Request(url_www, self.parse_detail)

    def parse_detail(self, response):
       
        item = data_domain_mongodb()
        #item['domain'] = response.url
        url_str = self.start_urls[0]
        item['domain'] = url_str.split('url=')[1]
        item['domaintags'] = response.xpath("//span[@class='Lnone']/text()").extract()
        item['domaintype1'] = response.xpath("//p[@class='fz14 SimSun ']/a[1]/text()").extract_first()
        item['domaintype2'] = response.xpath("//p[@class='fz14 SimSun ']/a[2]/text()").extract_first()
        item['domainarea'] = response.xpath("//p[@class='mb15 fz14 SimSun']/a/text()").extract_first()
        yield item