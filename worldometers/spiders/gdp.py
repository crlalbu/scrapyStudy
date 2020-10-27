import scrapy


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    allowed_domains = ['worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url = f"https://worldpopulationreview.com{link}"
            #absolute_url = response.urljoin(link)

            # yield scrapy.Request(url=absolute_url)
            yield response.follow(url=link)
