from django.shortcuts import render
from .models import Product

def products(request):
    # Загрузка данных из базы данных
    products = Product.objects.all()
    context = {}
    context['products'] = products

    return render(request, 'index.html', context)