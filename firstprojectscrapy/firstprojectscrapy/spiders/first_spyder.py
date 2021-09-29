import scrapy
import bs4

class firstspyder(scrapy.Spider):
    name = 'Demo'
    start_urls =  [
        'https://pythonscraping.com/'
    ]

    def parse(self , response):
        Header = response.css("h2,h3,h4,h5,h6").extract()
        yield{'Header' : Header}


