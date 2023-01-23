from rest_framework import serializers

from main.models import Address


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['pk', 'address', 'city', 'state', 'zipcode']
