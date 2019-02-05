# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class GithubtrendingrepoSpider(scrapy.Spider):
    name = 'GithubTrendingRepo'
    allowed_domains = ['github.com/trending/']
    start_urls = ['http://github.com/trending//']

    def parse(self, response):
    	# print("%s : %s : %s" % (response.status, response.url, response.text) )

        # print title text with css and xpath selectors
	    title_text = response.css('title::text')
	    print(title_text.get())
	    title_text = response.xpath('//title[1]/text()') 
	    print(title_text.get())

        # Get all anchor tags with css and xpath selectors
	    css_links = response.css('a::attr(href)').getall()
	    xpath_links = response.xpath('//a/@href').getall()
	    print(len(css_links))
	    print(len(xpath_links))
	    for (link, xlink) in zip(css_links, xpath_links):
        	print('{} {} '.format(link, xlink))

        # fetch url from github and avoid social media sites
	    trending_links = LxmlLinkExtractor(allow= r'^https://[a-z.]+/[a-z.]+$', deny_domains=['shop.github.com','youtube.com','twitter.com'], unique = True).extract_links(response)
	    for link in trending_links:
	    	print("%s : %s " % (link.url, link.text))