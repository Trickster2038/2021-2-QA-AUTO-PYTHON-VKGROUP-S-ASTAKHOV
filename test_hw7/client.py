import requests
from utils.responses_handler import ResponsesHandler


class ClientRequests:

    def __init__(self, url, log_level):
        self.url = url
        self.logger = ResponsesHandler(log_level)

    def handle_response(self, response):
        self.logger.log(response)
        return response

    def get_surname(self, name):
        return self.handle_response(requests.get(f'{self.url}/get_surname/{name}'))

    def post_add_user(self, name):
        return self.handle_response(requests.post(f'{self.url}/add_user', json={'name': name}))

    def put_update_user(self, name, surname):
        return self.handle_response(requests.put(f'{self.url}/update_user/{name}', json={'surname': surname}))

    def delete_user(self, name):
        return self.handle_response(requests.delete(f'{self.url}/delete_user/{name}'))
