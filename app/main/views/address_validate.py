from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.constants import (
    ADDRESS_VALIDATE_RESPONSE_NOT_AVAILABLE_ERROR,
    ADDRESS_VALIDATE_RESPONSE_NOT_FOUND_ERROR,
)
from main.exceptions import (
    AddressValidateAddressNotFoundException,
    AddressValidateServiceIsNotAvailableException,
)
from main.handlers.address_validate_handler import address_validate_handler
from main.serializers import AddressValidateRequestSerializer, AddressValidateResponseSerializer


class AddressValidate(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        serializer = AddressValidateRequestSerializer(data=request.query_params)

        serializer.is_valid(raise_exception=True)

        try:
            result = address_validate_handler(serializer.validated_data)
        except AddressValidateServiceIsNotAvailableException:
            return Response(
                ADDRESS_VALIDATE_RESPONSE_NOT_AVAILABLE_ERROR,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except AddressValidateAddressNotFoundException:
            return Response(
                ADDRESS_VALIDATE_RESPONSE_NOT_FOUND_ERROR,
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = AddressValidateResponseSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)
