import scrapy


class ListingscrawlerSpider(scrapy.Spider):
    name = 'ListingsCrawler'
    allowed_domains = ['https://www.ebay.co.uk/b/Mobile-Smart-Phones/9355?_fsrp=0&Brand=Apple&Network=Unlocked&_sacat=9355&LH_BIN=1&LH_ItemCondition=1000%7C1500%7C2000%7C2500%7C3000&rt=nc&Lock%2520Status=Factory%2520Unlocked%7CNetwork%2520Unlocked&Model=Apple%2520iPhone%2520XS']
    start_urls = ['http://https://www.ebay.co.uk/b/Mobile-Smart-Phones/9355?_fsrp=0&Brand=Apple&Network=Unlocked&_sacat=9355&LH_BIN=1&LH_ItemCondition=1000%7C1500%7C2000%7C2500%7C3000&rt=nc&Lock%2520Status=Factory%2520Unlocked%7CNetwork%2520Unlocked&Model=Apple%2520iPhone%2520XS/']

    def parse(self, response):
        pass
