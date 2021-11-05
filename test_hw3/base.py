import pytest
from jsons import *
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

    def create_campaign(self, name):
        payload = CampaignJsons.DEFAULT
        payload['name'] = name
        payload = json.dumps(payload)
        url = "https://target.my.com/api/v2/campaigns.json"
        headers = {
            'X-CSRFToken': self.api_client.csrf_token,
            'Cookie': self.api_client.cookie,
            'Content-Type': 'application/json'
        }
        response = self.api_client.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    def delete_campaign(self, id):
        url = "https://target.my.com/api/v2/campaigns/mass_action.json"
        headers = {
            'X-CSRFToken': self.api_client.csrf_token,
            'Cookie': self.api_client.cookie,
            'Content-Type': 'application/json'
        }
        payload = [
            {
                "id": id,
                "status": "deleted"
            }
        ]
        payload = json.dumps(payload)
        response = self.api_client.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    def get_campaigns(self):
        params = "?fields=id%2Cname%2Cdelivery%2Cprice%2Cbudget_limit%2Cbudget_limit_day%2Cpads_ots_limits%2Ccreated%2Cissues%2Cprices%2Cstatus%2Cpackage_id%2Cinterface_read_only%2Cread_only%2Cobjective%2Cuser_id%2Ctargetings__split_audience%2Ctargetings__pads%2Cenable_utm%2Cutm%2Cage_restrictions%2Cpackage_priced_event_type%2Cautobidding_mode&sorting=-id&limit=10&offset=0&_status__in=active&_user_id__in=11727528&_=1635850432320"
        url = "https://target.my.com/api/v2/campaigns.json" + params
        headers = {
            'Cookie': self.api_client.cookie
        }
        response = self.api_client.session.request("GET", url, headers=headers)
        return response

    def check_campaign_presence(self, name):
        campaigns = self.get_campaigns().json()
        for x in campaigns['items']:
            if x['name'] == name:
                return True
        return False

    def create_segment(self, name):
        params = "?fields=relations__object_type,relations__object_id,relations__params,relations__params__score,relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags"
        url = "https://target.my.com/api/v2/remarketing/segments.json" + params
        headers = {
            'X-CSRFToken': self.api_client.csrf_token,
            'Cookie': self.api_client.cookie,
            'Content-Type': 'application/json'
        }
        payload = SegmentJsons.DEFAULT
        payload['name'] = name
        payload = json.dumps(payload)
        response = self.api_client.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    def get_segments(self):
        params = "?fields=relations__object_type,relations__object_id,relations__params,relations__params__score,relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags&limit=500&_=1635848016171"
        url = "https://target.my.com/api/v2/remarketing/segments.json" + params
        headers = {
            'Cookie': self.api_client.cookie
        }
        response = self.api_client.session.request("GET", url, headers=headers)
        return response

    def check_segment_presence(self, name):
        segments = self.get_segments().json()
        for x in segments['items']:
            if x['name'] == name:
                return True
        return False

    def delete_segment(self, id):
        url = "https://target.my.com/api/v2/remarketing/segments/" + \
            str(id) + ".json"
        headers = {
            'X-CSRFToken': self.api_client.csrf_token,
            'Cookie': self.api_client.cookie
        }
        response = self.api_client.session.request("DELETE", url, headers=headers)
        return response
