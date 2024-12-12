from scrapy_selenium import SeleniumRequest
from scrapy import Spider
from testproject.items import TestprojectItem


class TripSpider(Spider):
    name = "trip"
    allowed_domains = ["trip.com"]
    start_urls = [
        "https://uk.trip.com/hotels/?locale=en-GB&curr=GBP"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        for hotel in response.css("div.recommend_hotels"):
            item = TestprojectItem()
            #item["title"] = hotel.css("h3.hotel-name::text").get(default='N/A')
            item["title"] = hotel.css("h3.boundCities_title::text").get(default='N/A')
            item["rating"] = hotel.css("span.hotel-score span::text").get(default='N/A')
            item["location"] = hotel.css("div.hotel-location::text").get(default='N/A')
            item["latitude"] = hotel.css("::attr(data-lat)").get(default='N/A')
            item["longitude"] = hotel.css("::attr(data-lng)").get(default='N/A')
            item["room_type"] = hotel.css("div.room-type::text").get(default='N/A')
            item["price"] = hotel.css("div.price span.amount::text").get(default='N/A')
            item["images"] = hotel.css("img.hotel-image::attr(src)").getall()
            yield item
            print(item)
