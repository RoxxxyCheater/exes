import scrapy
import json
import requests

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
                print("API Title:", item["name"])
                print("Image URL:", link.split('?')[0])

