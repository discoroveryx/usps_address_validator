from django.conf import settings

from main.entities import AddressResultEntity
from main.exceptions import (
    AddressValidateAddressNotFoundException,
    AddressValidateServiceIsNotAvailableException,
)
from main.libraries.usps import USPSAddress, USPSApiWithProxy


def address_validate_handler(validated_data) -> AddressResultEntity:
    validate_response = USPSAddress(
        name=validated_data['name'],
        address_1=validated_data['address'],
        city=validated_data['city'],
        state=validated_data['state'],
        zipcode=validated_data['zipcode'],
    )

    usps = USPSApiWithProxy(settings.USPS_USER_ID, test=True)

    try:
        validation = usps.validate_address(validate_response)
    except:  # noqa:E722
        raise AddressValidateServiceIsNotAvailableException

    result = validation.result

    try:
        validate_response = result['AddressValidateResponse']['Address']
    except KeyError:
        raise AddressValidateServiceIsNotAvailableException

    if 'Error' in validate_response:
        raise AddressValidateAddressNotFoundException

    if 'Address1' in validate_response:
        return AddressResultEntity(
            address1=result['AddressValidateResponse']['Address']['Address1'],
            address2=result['AddressValidateResponse']['Address']['Address2'],
            city=result['AddressValidateResponse']['Address']['City'],
            state=result['AddressValidateResponse']['Address']['State'],
            zip5=result['AddressValidateResponse']['Address']['Zip5'],
            zip4=result['AddressValidateResponse']['Address']['Zip4'],
        )

    return result
