import scrapy
from getexampledata.items import WebExampleItem


class ExampleWebSpider(scrapy.Spider):
    name = 'examplewebdata'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            # Extract the raw price text, e.g. '£51.77'
            price_raw = book.css('p.price_color::text').get()
            
            # Separate the currency and price
            currency = price_raw[0]  # The first character is the currency symbol
            price = price_raw[1:]    # The rest is the price amount

            book_item = WebExampleItem()
            book_item['book_name'] = book.css('h3 a::attr(title)').get()
            book_item['book_currency'] = currency
            book_item['book_price'] = price
            book_item['book_rating'] = book.css('p.star-rating::attr(class)').get().replace('star-rating ', '')

            yield book_item

        # Go to the next page if available
        #next_page = response.css('li.next a::attr(href)').get()
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)
