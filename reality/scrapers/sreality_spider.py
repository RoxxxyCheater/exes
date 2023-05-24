import scrapy
from scrapy.crawler import CrawlerProcess
from market.models import Product
from scrapy.utils.project import get_project_settings
class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/hledani/prodej/domy']

    def parse(self, response):
        product_count = 0

        for item in response.css('.item'):
            title = item.css('.title a::text').get()
            img_url = item.css('.image img::attr(src)').get()
            prod_url = item.css('.title a::attr(href)').get()

            product = Product(title=title, img_url=img_url, prod_url=prod_url)
            product.save()
            product_count += 1
            if product_count >= 500:
                break

        next_page_url = response.css('.next a::attr(href)').get()
        if next_page_url and product_count < 500:
            yield response.follow(next_page_url, self.parse),

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(SrealitySpider)
    process.start()
