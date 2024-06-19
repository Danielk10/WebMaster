from django.urls import path

from ..views.views import ProductListView, ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('add/', ProductCreateView.as_view(), name='product-add'),
]
