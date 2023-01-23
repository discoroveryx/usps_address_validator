from rest_framework import serializers


class AddressValidateRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    address = serializers.CharField(max_length=128)
    city = serializers.CharField(max_length=128)
    state = serializers.CharField(max_length=64)
    zipcode = serializers.CharField(max_length=8)
