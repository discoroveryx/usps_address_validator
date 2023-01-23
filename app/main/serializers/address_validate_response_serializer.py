from rest_framework import serializers


class AddressValidateResponseSerializer(serializers.Serializer):
    address1 = serializers.CharField(max_length=128)
    address2 = serializers.CharField(max_length=128)
    city = serializers.CharField(max_length=128)
    state = serializers.CharField(max_length=64)
    zip5 = serializers.CharField(max_length=8)
    zip4 = serializers.CharField(max_length=8)
