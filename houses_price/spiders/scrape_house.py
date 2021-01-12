import scrapy as scrapy

years=range(2012,2021)
class HouseScraper(scrapy.Spider):
    name="house_spider"
    #start_urls=[ "https://mobile.anjuke.com/fangjia/chengdu{}/dayuanj/".format(x) for x in years ]
    def start_requests(self):
        years=range(2012,2021)
        urls=[ "https://mobile.anjuke.com/fangjia/chengdu{}/dayuanj/".format(x) for x in years ]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        prices=response.css("ul.listseo-item a")
        for house in prices:
            yield {
            "date": house.css(".item-1::text").get(),
            "price":house.css(".item-2::text").get()
            }
