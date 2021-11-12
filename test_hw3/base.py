import pytest
from api.jsons import *
import json
import random
import string


class ApiBase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, client):
        self.api_client = client

    def random_string(self, length=10):
        strg = ''.join(random.choice(string.ascii_lowercase)
                       for _ in range(length))
        return strg

    def check_campaign_presence(self, name):
        campaigns = self.api_client.get_campaigns().json()
        for x in campaigns['items']:
            if x['name'] == name:
                return True
        return False

    def check_segment_presence(self, name):
        segments = self.api_client.get_segments().json()
        for x in segments['items']:
            if x['name'] == name:
                return True
        return False
