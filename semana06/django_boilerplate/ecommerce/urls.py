from django.urls import path
from .views import (
    ProductView,
)


urlpatterns = [
    path('products/all', ProductView.as_view())
]