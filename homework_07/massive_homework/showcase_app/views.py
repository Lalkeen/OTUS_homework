from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product

# Create your views here.

def showcase_index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("<h1>Showcase index</h1>")
    products = Product.objects.order_by("id").all()
    return render(request=request, template_name="showcase_app/index.html", context={"showcase": products})
