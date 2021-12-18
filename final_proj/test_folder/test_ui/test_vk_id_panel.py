from test_ui.base import BaseCase
import pytest
from config import *
import string
import random
from config import *
import allure

@allure.epic("UI")
@allure.feature("VK id")
@pytest.mark.UI
class TestVkIdPanel(BaseCase):

    def test_existing_id(self):
        '''
        1 - Login (fixture)
        2 - Go to ragister page & register valid random user
        3 - Mock user id
        4 - Go to main page
        5 - Check that id is displayed
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.email,
            self.fake_person.password,
            self.fake_person.password, True)
        id = self.fake_person.username[0:3] + '.' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.mock_cli.set_id(self.fake_person.username, id)
        self.main_page.go_to_this_page()
        panel = self.main_page.find(self.main_page.locators.VK_ID)
        assert panel.text.count(id) > 0

    def test_no_id(self):
        '''
        1 - Login (fixture)
        2 - Go to ragister page & register valid random user
        3 - delete user id on mock server
        4 - Go to main page
        5 - Check that id is not displayed
        '''
        self.register_page.go_to_this_page()
        # time.sleep(5)
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.email,
            self.fake_person.password,
            self.fake_person.password, True)
        self.mock_cli.delete_id(self.fake_person.username)
        self.main_page.go_to_this_page()
        assert not self.main_page.exist(self.main_page.locators.VK_ID)
