# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class AmazonPipeline(object):
    def process_item(self, item, spider):
        with open("./result/result.txt", 'a') as fp:
            obj = {}
            obj['name'] = item['name']
            obj['url'] = item['url']
            item_json = json.dumps(obj)
            fp.write(item_json + '\n')
