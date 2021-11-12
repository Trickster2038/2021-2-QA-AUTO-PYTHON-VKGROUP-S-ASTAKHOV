import requests
import urllib
from api.jsons import *
import json


class ApiClient:

    csrf_token = None

    def __init__(self):
        self.session = requests.Session()

    def post_login(self, username, passw):
        url = "https://auth-ac.my.com/auth"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }
        username = urllib.parse.quote(username.encode('utf-8'))
        passw = urllib.parse.quote(passw.encode('utf-8'))
        payload = f"email={username}&password={passw}&continue=https%3A%2F%2Ftarget.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526ignore_opener%253D1%23email&failure=https%3A%2F%2Faccount.my.com%2Flogin%2F"
        payload = payload.encode('utf-8')
        response = self.session.request(
            "POST", url, headers=headers, data=payload, allow_redirects=True)

        self.session.request("GET", "https://target.my.com/csrf")

        for cookie in self.session.cookies:
            if cookie.name == 'csrftoken':
                self.csrf_token = cookie.value

        return response

    def post_create_campaign(self, name):
        payload = CampaignJsons.DEFAULT
        payload['name'] = name
        payload = json.dumps(payload)
        url = "https://target.my.com/api/v2/campaigns.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json'
        }
        response = self.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    def post_remove_campaign(self, id):
        url = "https://target.my.com/api/v2/campaigns/mass_action.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json'
        }
        payload = [
            {
                "id": id,
                "status": "deleted"
            }
        ]
        payload = json.dumps(payload)
        response = self.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    def get_campaigns(self):
        params = "?fields=id%2Cname%2Cdelivery%2Cprice%2Cbudget_limit%2Cbudget_limit_day%2Cpads_ots_limits%2Ccreated%2Cissues%2Cprices%2Cstatus%2Cpackage_id%2Cinterface_read_only%2Cread_only%2Cobjective%2Cuser_id%2Ctargetings__split_audience%2Ctargetings__pads%2Cenable_utm%2Cutm%2Cage_restrictions%2Cpackage_priced_event_type%2Cautobidding_mode&sorting=-id&limit=10&offset=0&_status__in=active&_user_id__in=11727528&_=1635850432320"
        url = "https://target.my.com/api/v2/campaigns.json" + params
        response = self.session.request("GET", url)
        return response

    def post_create_segment(self, name):
        params = "?fields=relations__object_type,relations__object_id,relations__params,relations__params__score,relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags"
        url = "https://target.my.com/api/v2/remarketing/segments.json" + params
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json'
        }
        payload = SegmentJsons.DEFAULT
        payload['name'] = name
        payload = json.dumps(payload)
        response = self.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    def get_segments(self):
        params = "?fields=relations__object_type,relations__object_id,relations__params,relations__params__score,relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags&limit=500&_=1635848016171"
        url = "https://target.my.com/api/v2/remarketing/segments.json" + params
        response = self.session.request("GET", url)
        return response

    def delete_segment(self, id):
        url = "https://target.my.com/api/v2/remarketing/segments/" + \
            str(id) + ".json"
        headers = {
            'X-CSRFToken': self.csrf_token,
        }
        response = self.session.request(
            "DELETE", url, headers=headers)
        return response
