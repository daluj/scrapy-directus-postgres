# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ApiExampleItem(scrapy.Item):
    id = scrapy.Field()
    joke = scrapy.Field()
    updated_at = scrapy.Field()

class WebExampleItem(scrapy.Item):
    book_name = scrapy.Field()
    book_price = scrapy.Field()
    book_rating = scrapy.Field()
    book_currency = scrapy.Field()