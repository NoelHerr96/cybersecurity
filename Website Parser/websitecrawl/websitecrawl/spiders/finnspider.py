import scrapy
"""
Learned from: https://www.youtube.com/watch?v=s4jtkzHhLzY&t=72s    
"""

class FinnSpider(scrapy.Spider):
    name = "finn"
    
    #insert URL to scrape here
    start_urls = ["https://www.finn.no"]
    
    def parse(self, response):
        for products in response.css("div.aspect-w-1 aspect-h-1 overflow-hidden rounded-8 border border-bluegray-300"):
            yield {
                "name": products.css("a"), 

            }