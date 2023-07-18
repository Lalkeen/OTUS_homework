from django.urls import path
from .views import showcase_index
app_name = "showcase_app"

urlpatterns = [
    path("", showcase_index, name="index"),
]
