# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiubaiPipeline(object):
    def process_item(self, item, spider):
        with open('./data.txt', 'a+') as f:
            f.write('作者: %s\n %s\n 点赞: %s\t 评论数: %s\n\n' % (item['author'], item['body'], item['funNum'], item['comNum']))