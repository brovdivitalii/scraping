from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from module.items import *


class HotlineSpider(CrawlSpider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/musical_instruments/mikrofony/"]
    rules = [
        Rule(LinkExtractor(allow='^.*\/ua\/musical_instruments-mikrofony\/.*$'), callback='parse', follow=True),
        Rule(LinkExtractor(allow='^.*\/ua\/musical_instruments\/mikrofony\/((\?p=[0-9]*)|)$'), callback='pages', follow=True),
    ]

    def parse(self, response):
        name = response.xpath('//*[@id="__layout"]/div/div[1]/div[3]/div[1]/div/h1').xpath("string()").extract()
        title = response.xpath('//*[@id="__layout"]/div/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/p').xpath("string()").extract()
        shops = response.xpath('//*[@id="tabs"]/div[3]/div[3]/div[1]/div[1]/div/div[1]/div/a').xpath("string()").extract()
        print("item")
        print(response.url)
        yield Micro(
            name=name,
            title=title,
            shops=shops,
            url=response.url,
        )

    def pages(self, response):
        print("page")
        print(response.url)
