from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def product_form_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm

    context = { 'form':form}

    return render(request, "product/create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object':obj,
        'title':obj.title,
        'summary': obj.summary
    }
    return render(request, "product/detail.html", context)