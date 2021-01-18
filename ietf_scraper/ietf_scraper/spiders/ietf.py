import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # title = response.css('spam.title::text').get()
        title = response.xpath('//spam[@class="title"]/text()').get()
        return {"title": title}
        pass
