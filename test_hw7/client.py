import requests

class ClientRequests:

    def __init__(self, url):
        self.url = url 

    def get_surname(self, name):
        return requests.get(f'{self.url}/get_surname/{name}')

    def post_add_user(self, name):
        return requests.post(f'{self.url}/add_user', json={'name': name})
