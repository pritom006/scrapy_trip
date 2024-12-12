# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestprojectItem(scrapy.Item):
    # Fields for trip
    title = scrapy.Field()
    rating = scrapy.Field()
    location = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    room_type = scrapy.Field()
    price = scrapy.Field()
    images = scrapy.Field()

    
    # Fields for quotes
    # text = scrapy.Field()
    # author = scrapy.Field()
    # tags = scrapy.Field()

    # Fields for books
    # title = scrapy.Field()
    # price = scrapy.Field()
    # availability = scrapy.Field()
