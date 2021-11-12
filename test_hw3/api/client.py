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
        return self.session.request(
            "POST", url, headers=headers, data=payload)

    def post_remove_campaign(self, id):
        url = "https://target.my.com/api/v2/campaigns/mass_action.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json'
        }
        payload = json.dumps([{"id": id, "status": "deleted"}])
        return self.session.request("POST", url, headers=headers, data=payload)

    def get_campaigns(self):
        url = "https://target.my.com/api/v2/campaigns.json?fields=id%2Cname%2Cautobidding_mode&_status__in=active"
        return self.session.request("GET", url)

    def post_create_segment(self, name):
        url = "https://target.my.com/api/v2/remarketing/segments.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Content-Type': 'application/json'
        }
        payload = SegmentJsons.DEFAULT
        payload['name'] = name
        payload = json.dumps(payload)
        return self.session.request("POST", url, headers=headers, data=payload)

    def get_segments(self):
        url = "https://target.my.com/api/v2/remarketing/segments.json?fields=id,name&limit=500"
        return self.session.request("GET", url)

    def delete_segment(self, id):
        url = f"https://target.my.com/api/v2/remarketing/segments/{id}.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
        }
        return self.session.request("DELETE", url, headers=headers)
