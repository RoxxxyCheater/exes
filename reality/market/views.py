import subprocess
from django.shortcuts import render
from .models import Product

# def run_scraper():
#     subprocess.run(['scrapy', 'crawl', 'market'])

def products(request):
    # run_scraper()
    # Загрузка данных из базы данных
    products = Product.objects.all()
    context = {}
    context['products'] = products

    return render(request, 'index.html', context)