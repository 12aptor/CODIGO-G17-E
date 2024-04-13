from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductsModel
from django.template import loader

def home(request):
    products = ProductsModel.objects.all()
    # template = loader.get_template('ecommerce/index.html')

    # return HttpResponse(template.render({'products': products}))
    return render(request, 'ecommerce/index.html', {'products': products})