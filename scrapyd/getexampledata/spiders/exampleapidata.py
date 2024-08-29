import scrapy
from getexampledata.items import ApiExampleItem
from getexampledata.database import insert_if_not_exists
from urllib.parse import urlencode

class ExampleApiSpider(scrapy.Spider):
    name = 'exampleapidata'
    
    # Add the token for authentication
    # custom_settings = {
    #    'DEFAULT_REQUEST_HEADERS': {
    #        'X-Api-Key': '',
    #        'Content-Type': 'application/json'
    #    }
    #}

    def start_requests(self):
        base_url = 'https://api.chucknorris.io/jokes/random'
        
        category = getattr(self, 'category', None)

        if category:
            params = {
                'category': category
            }
            url = f"{base_url}?{urlencode(params)}"
        else:
            url = base_url

        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # Parse the JSON response
        data = response.json()
        categories = data.get('categories', [])

        # Insert into categories table if the category doesnt exist
        for category in categories:
            table = 'categories'
            columns = ['category']
            columnvalues = [category]
            unique_columns = ['category']  # Specify the unique columns to check for existence
            insert_if_not_exists(table, columns, columnvalues, unique_columns)
        
        item = ApiExampleItem()
        item['id'] = data.get('id')
        item['joke'] = data.get('value')
        item['updated_at'] = data.get('updated_at')

        yield item