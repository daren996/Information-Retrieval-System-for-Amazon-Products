# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

# cate = 'Baby'
# cate = 'Mens'
# cate = 'Womens'
# cate = 'Girls'
cate = 'Boys'

class AmazonPipeline(object):
    def __init__(self):
        self.file = codecs.open('Amazon_data_' + cate + '.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'

        self.file.write(line)

        return item
