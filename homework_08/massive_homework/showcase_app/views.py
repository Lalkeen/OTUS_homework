from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Product
from .forms import ProductForm

# Create your views here.


def showcase_index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("<h1>Showcase index</h1>")
    products = Product.objects.order_by("id").all()
    return render(
        request=request,
        template_name="showcase_app/index.html",
        context={"showcase": products},
    )


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = "name", "description"
    # success_url = reverse
    success_url = reverse_lazy("showcase_app:index")
