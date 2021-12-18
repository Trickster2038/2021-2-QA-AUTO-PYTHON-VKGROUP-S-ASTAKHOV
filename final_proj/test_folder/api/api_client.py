import requests
import urllib
import allure
import time

class ApiClient:
    def __init__(self, app_host, app_port, username, password):
        self.session = requests.Session()
        self.base_url = f"http://{app_host}:{app_port}/"
        self.username = username
        self.password = password

    @allure.step("get app status")
    def get_app_status(self):
        url = self.base_url + 'status'
        return self.session.request('GET', url)

    def wait_app_up(self):
        i = 0
        while i < 200:
            i += 1
            try:
                code = self.get_app_status().status_code
                if code == 200:
                    break
            except Exception:
                pass
            time.sleep(0.1)


    @allure.step("login user")
    def post_login(self):
        url = self.base_url + "login"
        headers = {
            'Referer': self.base_url,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        username = urllib.parse.quote(self.username.encode('utf-8'))
        password = urllib.parse.quote(self.password.encode('utf-8'))
        payload = f"username={username}&password={password}&submit=Login"

        payload = payload.encode('utf-8')
        response = self.session.request(
            "POST", url, headers=headers, data=payload, allow_redirects=False)
        return response

    @allure.step("create user")
    def post_create_user(self, user):
        user.allure_display()
        url = self.base_url + 'api/add_user'
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {"username": user.username,
                   "password": user.password, "email": user.email}
        return self.session.request('POST', url, headers=headers, json=payload)

    @allure.step("Delete user")
    def get_delete_user(self, user):
        user.allure_display()
        url = self.base_url + "/api/del_user/" + user.username
        return self.session.request('GET', url)
    
    @allure.step("Block user")
    def get_block_user(self, user):
        user.allure_display()
        url = self.base_url + "/api/block_user/" + user.username
        return self.session.request('GET', url)

    @allure.step("Accept user")
    def get_accept_user(self, user):
        user.allure_display()
        url = self.base_url + "/api/accept_user/" + user.username
        return self.session.request('GET', url)

