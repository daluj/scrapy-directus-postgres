# pipelines.py

import psycopg2

class PostgresPipeline:
    def __init__(self, db_settings):
        self.db_settings = db_settings

    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.getdict("DB_SETTINGS")
        return cls(db_settings)
    
    def __init__(self, db_settings):
        self.db_settings = db_settings

    def open_spider(self, spider):
        self.connection = psycopg2.connect(**self.db_settings)
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        # Construct the INSERT query dynamically based on the item fields
        columns = ', '.join(item.keys())
        values_template = ', '.join(['%s'] * len(item))
        query = f"INSERT INTO {spider.name} ({columns}) VALUES ({values_template})"

        try:
            self.cursor.execute(query, tuple(item.values()))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            spider.logger.error(f"Error storing item in PostgreSQL: {e}")

        return item