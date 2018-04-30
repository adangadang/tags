#encoding:utf-8
from scrapy_redis.spiders import RedisSpider
import scrapy
from ..items import data_url_mongodb

from goose import Goose  
from goose.text import StopWordsChinese  
import md5
import jieba  
import jieba.analyse 

class MySpider(RedisSpider):
    name = 'tags'
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_tags.pipelines.MgdbPipeline': 300
        }}
    redis_key = 'myspider:start_urls' #从redis里面读url https://blog.csdn.net/mighty13/article/details/51354406

    def extract_tagss(content,topk):  
        #content = content.strip()  
        tags=jieba.analyse.extract_tags(content,topk)  
        return ','.join(tags)        
        
    def parse(self, response):
        item = data_url_mongodb()
        m = md5.new()
        m.update(response.url)
        item['md5url'] = m.hexdigest()
        item['url'] = response.url
        article = Goose({'stopwords_class': StopWordsChinese}).extract(raw_html=response.body)

        title=article.title
        #bady=article.cleaned_text[:350];badytags=bady
        bady=article.cleaned_text
        #item['titletags'] = article.title
        #item['badytags'] = article.cleaned_text
        titletags=jieba.analyse.extract_tags(title,3)
        badytags=jieba.analyse.extract_tags(bady,5)
        
        item['titletags'] = ','.join(titletags)
        item['badytags'] = ','.join(badytags)
        
        yield item

