import requests
import urllib


class ApiClient:

    csrf_token = None
    session = requests.Session()
    cookie = ""

    def login(self, username, passw):
        params = "?lang=ru&nosavelogin=0"
        url = "https://auth-ac.my.com/auth" + params
        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/'
        }
        username = urllib.parse.quote(username.encode('utf-8'))
        passw = urllib.parse.quote(passw.encode('utf-8'))
        payload = f"email={username}&password={passw}&continue=https%3A%2F%2Ftarget.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526ignore_opener%253D1%23email&failure=https%3A%2F%2Faccount.my.com%2Flogin%2F"
        payload = payload.encode('utf-8')
        response = self.session.request(
            "POST", url, headers=headers, data=payload, allow_redirects=False)
        cookie = response.headers['Set-Cookie']
        self.cookie += "; " + cookie
        while 'Location' in response.headers:
            url = response.headers['Location']
            response = self.session.request(
                "GET", url, allow_redirects=False)
            if 'Set-Cookie' in response.headers:
                cookie = response.headers['Set-Cookie']
                self.cookie += "; " + cookie

        responseCSRF = self.session.request(
            "GET", "https://target.my.com/csrf")

        cookieCSRF = responseCSRF.headers['Set-Cookie']
        self.cookie += "; " + cookieCSRF
        self.csrf_token = cookieCSRF.split("=")[1].split(";")[0]
        return response
