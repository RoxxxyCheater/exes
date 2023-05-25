import scrapy
import json
import requests
# from market.models import Product 
import psycopg2
class RealitySpiderSpider(scrapy.Spider):
    name = "reality_spider"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://sreality.cz/"]
    pages_count = 25

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=2&category_type_cb=1&noredirect=1&page={page}&per_page=20&tms=1684963515218'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        api_response = requests.get(response.url)
        if api_response.status_code == 200: 
            data = api_response.json()
            for item in data["_embedded"]["estates"]:
                link = item['_links']["images"][0]['href'] if "_links" in item and item['_links']["images"][0] else "N/A"
                title = item["name"]
                img_url = link.split('?')[0]
                
                #To Django

                # product = Product(title=item["name"], img_url=link.split('?')[0])
                # product.save()    

                #To PostgreSQL

                 # Connection to PostgreSQL
                connection = psycopg2.connect(
                    dbname='postgres',
                    user='postgres',
                    password='qwerty',
                    host='db',
                    port='5432'
                )

                # Create cursor to SQL-request
                cursor = connection.cursor()
                
                # Create table if not exists
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS market_Product (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    img_url TEXT
                )
                '''
                cursor.execute(create_table_query)
                # Insert data to database
                insert_query = f"INSERT INTO market_Product (title, img_url) VALUES ('{title}', '{img_url}')"
                cursor.execute(insert_query)
                
                # Closing cursor and save changes to db
                cursor.close()
                connection.commit()
                connection.close()







