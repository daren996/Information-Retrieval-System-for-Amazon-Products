# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    title =scrapy.Field()
    cat=scrapy.Field()
    price=scrapy.Field()
    star=scrapy.Field()
    reviewers=scrapy.Field()
    questions=scrapy.Field()
    description=scrapy.Field()
    Product_description=scrapy.Field()
    details=scrapy.Field()
    details1=scrapy.Field()
    picture=scrapy.Field()
    pass
