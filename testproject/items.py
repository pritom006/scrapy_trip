# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestprojectItem(scrapy.Item):
    # Fields for trip
    hotelName = scrapy.Field()
    rating = scrapy.Field()
    location = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    roomName = scrapy.Field()
    price = scrapy.Field()
    imageUrl = scrapy.Field()
    city_id = scrapy.Field()

    

