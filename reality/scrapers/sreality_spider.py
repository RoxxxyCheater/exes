import scrapy
from market.models import Product

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/hledani/prodej/domy']

    def parse(self, response):
        product_count = 0

        # Извлечение данных со страницы
        for item in response.css('.item'):
            title = item.css('.title a::text').get()
            img_url = item.css('.image img::attr(src)').get()
            prod_url = item.css('.title a::attr(href)').get()

            # Создание экземпляра модели Product и сохранение данных
            product = Product(title=title, img_url=img_url, prod_url=prod_url)
            product.save()
            product_count += 1
            if product_count >= 10:
                break

        # Переход на следующую страницу, если нужно
        next_page_url = response.css('.next a::attr(href)').get()
        if next_page_url and product_count < 500:
            yield response.follow(next_page_url, self.parse)