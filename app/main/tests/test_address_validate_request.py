from urllib.parse import urlencode

from rest_framework.test import APITestCase

from main.constants import ADDRESS_VALIDATE_RESPONSE_NOT_FOUND_ERROR


class AddressValidateRequestTestcase(APITestCase):
    url = '/address/validate/'

    def test_validate_ok(self):
        payload = {
            'name': 'Tobin Brown',
            'address': '8 Wildwood',
            'city': 'Old lyme',
            'state': 'CT',
            'zipcode': '06371',
        }

        query = urlencode(payload)
        response = self.client.get(f'{self.url}?{query}')
        self.assertEqual(response.status_code, 200)

        expected_data = {
            'address1': '-',
            'address2': '8 WILDWOOD DR',
            'city': 'OLD LYME',
            'state': 'CT',
            'zip5': '06371',
            'zip4': '1844',
        }
        self.assertEqual(response.data, expected_data)

    def test_validate_error(self):
        payload = {
            'name': '1',
            'address': '1',
            'city': '1',
            'state': 'CT',
            'zipcode': '06371',
        }

        query = urlencode(payload)
        response = self.client.get(f'{self.url}?{query}')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, ADDRESS_VALIDATE_RESPONSE_NOT_FOUND_ERROR)
