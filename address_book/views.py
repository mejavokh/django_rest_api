from rest_framework.generics import ListAPIView

from .serializers import *
from .models import *


class DeliveryAddressesAPIView(ListAPIView):
    queryset = DeliveryAddresses.objects.all()
    serializer_class = DeliveryAddressesListSerializer


class ContactsAPIView(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer





