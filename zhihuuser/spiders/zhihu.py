# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import Spider, Request

from zhihuuser.items import ZhihuItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']


    url = 'https://www.zhihu.com/api/v4/columns/purerender/articles?include=data%5B*%5D.admin_closed_comment%2Ccomment_count%2Csuggest_edit%2Cis_title_image_full_screen%2Ccan_comment%2Cupvoted_followees%2Ccan_open_tipjar%2Ccan_tip%2Cvoteup_count%2Cvoting%2Ctopics%2Creview_info%2Cauthor.is_following%2Cis_labeled%2Clabel_info&limit={limit}&offset={offset}'

    def start_requests(self):

        yield Request(self.url.format(limit=10, offset=0), callback=self.parse_follows)


    def parse_follows(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                item = ZhihuItem()

                for field in item.fields:
                    if field in result.keys():
                        item[field] = result.get(field)
                yield item

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_follows)


