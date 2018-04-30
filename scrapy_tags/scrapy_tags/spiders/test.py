#encoding:utf-8
from goose import Goose  
from goose.text import StopWordsChinese  

import jieba  
import jieba.analyse  
def extract_tags(content,topk):  
        content = content.strip()  
        tags=jieba.analyse.extract_tags(content, topK=topk)  
        return ','.join(tags)        
def gooseExample():  
        g = Goose()  
        url = "http://www.chinadaily.com.cn/a/201712/22/WS5a3c7473a31008cf16da2d9e.html"  
        article = g.extract(url=url)  
        print(article.title)  
        print(article.cleaned_text[:150])  
          
def gooseChineseExample():  
        g = Goose({'stopwords_class': StopWordsChinese})  
        url = "https://item.btime.com/36a0f17i0489keqltn35q96p4lr?from=haozcxw"  
        article = g.extract(url=url)  
        print(article.title)  
        print(article.meta_description)  
        print(article.cleaned_text[:150])  
        print( extract_tags(article.cleaned_text[:150],5))  
      
if __name__ == '__main__':  
        #begin_insert_job("knowledge", "person", "../data/Person.json")  
        gooseExample()  
        gooseChineseExample()  

# from goose import Goose
# from goose.text import StopWordsChinese
# url  = 'https://item.btime.com/36a0f17i0489keqltn35q96p4lr?from=haozcxw'
# g = Goose({'stopwords_class': StopWordsChinese})
# article = g.extract(url=url)
# print article.cleaned_text[:150]

#https://hr.tencent.com/position_detail.php?id=39664&keywords=&tid=0&lid=0

# from goose import Goose
# from goose.text import StopWordsChinese
# url  = 'https://hr.tencent.com/position_detail.php?id=39664&keywords=&tid=0&lid=0'
# g = Goose({'stopwords_class': StopWordsChinese})
# article = g.extract(url=url)
# print article.cleaned_text[:150]

#两个爬从队列（1.domain队列 进入后 爬虫取出 分类 域名关键字 2.url队列  进入后  爬虫 取出 标题关键字 内容关键字  ）  if 存在不  不存在 写入队列
#https://blog.csdn.net/mighty13/article/details/51354406
#https://github.com/grangier/python-goose
#https://www.cnblogs.com/huwei934/p/6971266.html  scrapy基础知识之发送POST请求： 可以使用 yield scrapy.FormRequest(url, formdata, callback)方法发送POST请求。
