from django.urls import path
from contacts import views

app_name = 'contacts'
urlpatterns = [
    path('delivery/', views.contactList, name='contactList'),
]
