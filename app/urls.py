from django.contrib import admin
from django.urls import path
from .views import home, detail, filter_by,place_order
from .filter import search

app_name = 'app'

urlpatterns = [
    path('', home, name = 'home' ),
    path('category/<int:category_id>', home, name = 'category_filter'),
    path('detail/<product_id>', detail, name = 'detail'),
    path('filter/<filter_type>', filter_by, name = 'filter'),
    path('search/q=', search, name = 'search'),
    path('order/', place_order, name = 'order')
]