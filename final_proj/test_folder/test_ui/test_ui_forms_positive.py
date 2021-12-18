from base import BaseCase
import pytest
import allure

@allure.epic("UI")
@allure.feature("Forms positive")
@pytest.mark.UI
class TestFormsPagesPositive(BaseCase):
    
    def test_register_positive(self):
        '''
        1 - Go to register page
        2 - Enter random UNIQUE valid userdata
        3 - Check redirection to main page
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.email,
            self.fake_person.password,
            self.fake_person.password, True)
        assert self.main_page.is_on_main_page()

    def test_login_positive(self):
        '''
        1 - Go to register page
        2 - Enter random UNIQUE valid userdata
        3 - Logout
        4 - Go to login page
        5 - Enter credentials of crated user
        6 - Check redirection to main page
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.email,
            self.fake_person.password,
            self.fake_person.password, True)
        self.main_page.logout()
        self.login_page.go_to_this_page()
        self.login_page.login(
            self.fake_person.username,
            self.fake_person.password)
        assert self.main_page.is_on_main_page()