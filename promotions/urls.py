from django.urls import path
from promotions import views

app_name = 'promotions'
urlpatterns = [
    path('promotions/', views.promotionsList, name='promotionsList'),
]
