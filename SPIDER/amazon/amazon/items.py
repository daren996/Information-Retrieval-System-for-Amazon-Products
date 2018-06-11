# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    cat = scrapy.Field()
    price = scrapy.Field()
    star = scrapy.Field()
    reviewers = scrapy.Field()
    questions = scrapy.Field()
    pass