from django.urls import path

from .views import *

urlpatterns = [
    path('contacts/', ContactsAPIView.as_view(), name='contacts'),
    path('delivery_address/', DeliveryAddressesAPIView.as_view(), name='delivery-address')
]


