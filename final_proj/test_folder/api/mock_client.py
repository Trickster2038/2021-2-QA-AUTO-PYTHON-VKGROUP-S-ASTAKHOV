import requests
import allure

class MockClient:
    def __init__(self, mock_host, mock_port, username, password):
        self.session = requests.Session()
        self.base_url = f"http://{mock_host}:{mock_port}/vk_id"
        self.username = username
        self.password = password

    @allure.step("Mock - set id")
    def set_id(self, username, id):
        url = self.base_url + "/utils/create/" + username
        return self.session.request('POST', url, json={'id': id})

    @allure.step("Mock - delete id")
    def delete_id(self, username):
        url = self.base_url + "/utils/delete/" + username
        return self.session.request('DELETE', url)