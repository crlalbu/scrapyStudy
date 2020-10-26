import scrapy


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    allowed_domains = ['worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        pass
