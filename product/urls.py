from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('menu/', views.menu, name='menu'),
    #path('<int:kind_id>/product/', views.productList, name='productList'),
]
