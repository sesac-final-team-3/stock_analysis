# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BoardcommentItem(scrapy.Item):

    title = scrapy.Field()
    view = scrapy.Field() 
    recommend = scrapy.Field() 
    decommend = scrapy.Field() 
    date = scrapy.Field() 
    comment = scrapy.Field() 
    com_code = scrapy.Field()
    pass
