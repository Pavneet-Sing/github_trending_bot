# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field
from github_trending_bot.items import PageContentItem


# class PageContentItem(Item): # A data storage class(like directory) to store the extracted data
#     url = Field()
#     content = Field()

class Githubtrendingrepocrawler(CrawlSpider): # 1
    name = 'GithubTrendingRepoCrawler' # 2
    start_urls = ['http://github.com/trending/'] # 2

    # 3
    rules = (
        # Extract link from this path only
        Rule(
            LxmlLinkExtractor(restrict_xpaths=[
                "//ol[@id=repo-list]//h3/a/@href"], allow_domains=['https://github.com/trending']), 
            callback='parse'
        ),
        # link should match this pattern and create new requests
        Rule(
            LxmlLinkExtractor(allow='https://github.com/[\w-]+/[\w-]+$', allow_domains=['github.com']), 
            callback='parse_product_page'
        ),
        # # Recursive Rule
        # Rule(
        #     LxmlLinkExtractor(allow='https://github.com/[\w-]+/[\w-]+$', allow_domains=['github.com']), 
        #     callback='parse_product_page', follow=True
        # ),
    )

     # 4
    def parse_product_page(self, response):
        item = PageContentItem()
        item['url'] = response.url
        item['content'] = response.css('article').get()
        yield item