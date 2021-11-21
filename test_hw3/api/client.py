import requests
import urllib
from api.data_templates import *
import json
import os


class ApiClient:

    csrf_token = None

    def __init__(self, media_root):
        self.session = requests.Session()
        self.media_root = media_root

    def post_login(self, username, passw):
        url = "https://auth-ac.my.com/auth"
        headers = {
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
        payload = CampaignDataTemplates.DEFAULT
        id = int(self.post_upload_image().json()['id'])
        payload["banners"][0]["content"]["image_90x75"]["id"] = id
        payload["banners"][0]["urls"]["primary"]["id"] = self.get_url_id()
        payload['name'] = name
        url = "https://target.my.com/api/v2/campaigns.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
        }
        return self.session.request(
            "POST", url, headers=headers, json=payload)

    def post_remove_campaign(self, id):
        url = "https://target.my.com/api/v2/campaigns/mass_action.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
        }
        payload = [{"id": id, "status": "deleted"}]
        return self.session.request("POST", url, headers=headers, json=payload)

    def get_campaigns(self):
        url = "https://target.my.com/api/v2/campaigns.json?fields=id%2Cname%2Cautobidding_mode&_status__in=active"
        return self.session.request("GET", url)

    def post_create_segment(self, name):
        url = "https://target.my.com/api/v2/remarketing/segments.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
        }
        payload = SegmentDataTemplates.DEFAULT
        payload['name'] = name
        return self.session.request("POST", url, headers=headers, json=payload)

    def get_segments(self):
        url = "https://target.my.com/api/v2/remarketing/segments.json?fields=id,name&limit=500"
        return self.session.request("GET", url)

    def delete_segment(self, id):
        url = f"https://target.my.com/api/v2/remarketing/segments/{id}.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
        }
        return self.session.request("DELETE", url, headers=headers)

    def post_upload_image(self):
        url = "https://target.my.com/api/v2/content/static.json"
        pic_path = os.path.join(self.media_root, 'banner.jpg')
        headers = {
            'X-CSRFToken': self.csrf_token,
        }
        file = {
            'file': (os.path.basename(pic_path), open(pic_path, 'rb'), 'image/jpeg'),
            'data': (None, json.dumps({"width": 0, "height": 0})),
        }
        return self.session.request(
            "POST", url, headers=headers, files=file)

    def get_url_id(self, target_url="https://vk.com/feed"):
        target_url = urllib.parse.quote(target_url.encode('utf-8'))
        url = f"https://target.my.com/api/v1/urls/?url={target_url}"
        return self.session.request("GET", url).json()["id"]
