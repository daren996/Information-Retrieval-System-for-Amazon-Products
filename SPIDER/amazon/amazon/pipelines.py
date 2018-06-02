# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class AmazonPipeline(object):
    def process_item(self, item, spider):
        with open("./result/result_info.txt", 'a') as fp:
            # obj = {'name': item['name'], 'url': item['url'], 'cat': item['cat']}
            obj = {
                'title': item['title'],
                'cat': item['cat'],
                'price': item['price'],
                'star': item['star'],
                'reviewers': item['reviewers'],
                'questions': item['questions'],
            }
            item_json = json.dumps(obj)
            fp.write(item_json + '\n')
        return item
