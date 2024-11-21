import scrapy


class MopDetailsSpiderSpider(scrapy.Spider):
    name = "mop_details_spider"
    allowed_domains = ["concesiones.mop.gob.cl"]
    start_urls = ["https://concesiones.mop.gob.cl"]

    def parse(self, response):
        pass
