# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyRedisMongodbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()

class data_url_mongodb(scrapy.Item):
    md5url = scrapy.Field()
    url = scrapy.Field()
    titletags = scrapy.Field()
    badytags = scrapy.Field()
    # domain = scrapy.Field()
    # domaintags = scrapy.Field()
    # domaintype1 = scrapy.Field()    
    # domaintype2 = scrapy.Field()
    # domainarea = scrapy.Field()
    
class data_domain_mongodb(scrapy.Item):

    domain = scrapy.Field()
    domaintags = scrapy.Field()
    domaintype1 = scrapy.Field()    
    domaintype2 = scrapy.Field()
    domainarea = scrapy.Field()
    