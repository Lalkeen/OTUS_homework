
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Product
from .forms import ProductForm

# Create your views here.


class ProductListView(ListView):
    queryset = (
        Product
        .objects
        .all()
    )


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("showcase_app:index")


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("showcase_app:product", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    success_url = reverse_lazy("showcase_app:index")
    queryset = (
        Product
        .objects
        .filter(~Q(archived=True))
        .all()
    )
