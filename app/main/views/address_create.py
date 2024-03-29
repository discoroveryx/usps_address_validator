from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from main.models import Address
from main.serializers import AddressCreateSerializer


class AddressCreate(viewsets.ModelViewSet):
    serializer_class = AddressCreateSerializer
    queryset = Address.objects.all()
    permission_classes = [AllowAny]
