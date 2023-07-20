from django.urls import path
from django.urls import path

from .views import (
    # ShopIndexView,
    # CategoriesWithProductsTree,
    # ProductsView,
    # OrdersListView,
    # get_task_info,
    # CategoriesListView,
    ProductCreateView,
    # CategoryDetailView,
    # CategoryUpdateView,
    # CategoryDeleteView,
)
from .views import showcase_index


app_name = "showcase_app"

urlpatterns = [
    path("", showcase_index, name="index"),
    path("product/create/", ProductCreateView.as_view(), name="create-category"),
]
