import json

import requests
import xmltodict
from lxml import etree
from usps import Address, USPSApi, USPSApiError

from django.conf import settings


class USPSAddress(Address):
    ...


class USPSApiWithProxy(USPSApi):
    BASE_URL = 'http://production.shippingapis.com/ShippingAPI.dll?API='

    proxy_servers = {
        'http': settings.USPS_PROXY_SERVER,
    }

    def send_request(self, action, xml):
        session = requests.Session()
        session.proxies.update(self.proxy_servers)

        xml = etree.tostring(xml, encoding='iso-8859-1', pretty_print=self.test).decode()
        url = self.get_url(action, xml)
        xml_response = session.get(url).content
        response = json.loads(json.dumps(xmltodict.parse(xml_response)))
        if 'Error' in response:
            raise USPSApiError(response['Error']['Description'])
        return response
