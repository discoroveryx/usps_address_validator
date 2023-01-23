from rest_framework.test import APITestCase

from main.models import Address


class AddressCreateRequestTestcase(APITestCase):
    url = '/address/create/'

    def test_create_ok(self):
        payload = {
            'address': '8 Wildwood',
            'city': 'Old lyme',
            'state': 'CT',
            'zipcode': '06371',
        }

        response = self.client.post(self.url, payload)

        self.assertEqual(response.status_code, 201)

        address = Address.objects.filter(
            address=payload['address'],
            city=payload['city'],
            state=payload['state'],
            zipcode=payload['zipcode'],
        )

        self.assertTrue(address.exists())
