import scrapy
from scrapy import item
from ..items import FirstprojectscrapyItem

class firstspyder(scrapy.Spider):
    name = 'Demo'
    start_urls =  [
        'https://pythonscraping.com/'
    ]

    # def parse(self , response):
    #     Header = response.css("h2,h3,h4,h5,h6::text").extract_first()
    #     yield{'Header' : Header}

    def parse(self, response):

        items = FirstprojectscrapyItem()

        all_header = response.css('h1,h2,h3,h4,h5,h6')
        
        for header in all_header:
            h2 = header.css('h2::text').extract()
            h3 = header.css('h3::text').extract()
            h4 = header.css('h4::text').extract()
            h5 = header.css('h5::text').extract()
            h6 = header.css('h6::text').extract()

            items['h2'] = h2
            items['h3'] = h3
            items['h4'] = h4
            items['h5'] = h5
            items['h6'] = h6

            yield items







