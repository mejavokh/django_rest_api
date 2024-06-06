from rest_framework import serializers

from address_book.models import Contacts, DeliveryAddresses


class DeliveryAddressesListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    city = serializers.CharField()
    street = serializers.CharField()
    home_number = serializers.IntegerField()

    class Meta:
        model = DeliveryAddresses
        fields = ['id', 'city', 'street', 'home_number']


class ContactSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()

    class Meta:
        model = Contacts
        fields = ['id', 'phone_number']



