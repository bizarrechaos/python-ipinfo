import json
import requests


class ipinfo:
    info = None

    def __init__(self, ip):
        self.ip = ip

    def geolocate(self):
        url = 'http://ipinfo.io/{0}/json'.format(self.ip)
        try:
            return requests.get(url).json()
        except Exception:
            return {}
