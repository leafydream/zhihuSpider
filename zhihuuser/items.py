# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    author = Field()
    comment_count = Field()
    comment_permission = Field()
    created = Field()
    excerpt = Field()
    excerpt_title = Field()
    image_url = Field()
    is_labeled = Field()
    state = Field()
    title = Field()
    title_image = Field()
    type = Field()
    updated = Field()
    url = Field()
    voteup_count = Field()
    voting = Field()

