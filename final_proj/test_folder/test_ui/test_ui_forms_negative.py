from base import BaseCase
import time
import pytest
import allure

@allure.epic("UI")
@allure.feature("Login negative")
@pytest.mark.UI
class TestLoginPageNegative(BaseCase):

    def test_fake_user(self):
        '''
        1 - Go to login page
        2 - Enter random UNIQUE user credentials
        3 - Check notification about invalid credentials
        '''
        self.login_page.go_to_this_page()
        self.login_page.login(self.fake_person.username,
                              self.fake_person.password)
        assert self.login_page.notification_include(
            'Invalid username or password')
        assert self.login_page.notification_text_clear()

    def test_invalid_login(self):
        '''
        1 - Go to login page
        2 - Enter random UNIQUE user credentials with TOO SHORT username
        3 - Check notification about too short username
        '''
        self.login_page.go_to_this_page()
        self.fake_person.username = self.fake_person.username[0:3]
        self.login_page.login(self.fake_person.username,
                              self.fake_person.password)
        assert self.login_page.notification_include(
            'Incorrect username length')
        assert self.login_page.notification_text_clear()

    def test_empty_username(self):
        '''
        1 - Go to login page
        2 - Enter username and empty password
        3 - Check that url dont change after pressing button
        '''
        self.login_page.go_to_this_page()
        self.login_page.login('', self.fake_person.password)
        assert self.login_page.blocked_on_page()

@allure.epic("UI")
@allure.feature("Register negative")
@pytest.mark.UI
class TestRegisterPageNegative(BaseCase):

    def test_short_username(self):
        '''
        1 - Go to registration page
        2 - Enter random user's data with too short username
        3 - Check notification about too short username
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username[0:3],
            self.fake_person.email,
            self.fake_person.password,
            self.fake_person.password,
            True)
        assert self.register_page.notification_include(
            'Incorrect username length')
        assert self.register_page.notification_text_clear()

    def test_empty_password(self):
        '''
        1 - Go to registration page
        2 - Enter random user's data with empty password
        3 - Check notification about password mismatch
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.email,
            self.fake_person.password, '', True)
        assert self.register_page.notification_include('Passwords must match')
        assert self.register_page.notification_text_clear()

    def test_empty_email(self):
        '''
        1 - Go to registration page
        2 - Enter random user's data with empty email
        3 - Check notification about email legnth
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username, '',
            self.fake_person.password,
            self.fake_person.password, True)
        assert self.register_page.notification_include(
            'Incorrect email length')
        assert self.register_page.notification_text_clear()

    def test_invalid_email(self):
        '''
        1 - Go to registration page
        2 - Enter random user's data with invalid email fromat
        3 - Check notification about invalid email
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.username + 'gmail.com',
            self.fake_person.password,
            self.fake_person.password, True)
        assert self.register_page.notification_include('Invalid email address')
        assert self.register_page.notification_text_clear()

    def test_empty_terms_checkbox(self):
        '''
        1 - Go to registration page
        2 - Enter random user's data without terms acceptence
        3 - Check that url dont change after pressing button
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.email,
            self.fake_person.password,
            self.fake_person.password, False)
        assert self.register_page.blocked_on_page()

    @pytest.mark.xfail(reason="notification dont render json")
    def test_invalid_multiple(self):
        '''
        1 - Go to registration page
        2 - Enter random user's data with invalid name and email
        3 - Check notifications text
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username[0:3],
            self.fake_person.username + 'gmail.com',
            self.fake_person.password,
            self.fake_person.password, True)
        assert self.register_page.notification_include('Invalid email address')
        assert self.register_page.notification_include(
            'Incorrect username length')
        assert self.register_page.notification_text_clear()

    def test_double_username(self):
        '''
        1 - Go to registration page
        2 - Register user
        3 - Return to registration page
        4 - Try to register with same username
        3 - Check notifications about existance of such user
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.email,
            self.fake_person.password,
            self.fake_person.password, True)
        self.main_page.logout()
        self.register_page.go_to_this_page()
        self.register_page.register(
        self.fake_person.username,
        self.fake_person.username + '@gmail.com',
        self.fake_person.password,
        self.fake_person.password, True)
        assert self.register_page.blocked_on_page()
        assert self.register_page.notification_include('User already exist')
        assert self.register_page.notification_text_clear()

    @pytest.mark.xfail(reason="no checking double email usage")
    def test_double_email(self):
        '''
        1 - Go to registration page
        2 - Register user
        3 - Return to registration page
        4 - Try to register with same email
        3 - Check notifications about existance of such user
        '''
        self.register_page.go_to_this_page()
        self.register_page.register(
            self.fake_person.username,
            self.fake_person.email,
            self.fake_person.password,
            self.fake_person.password, True)
        self.main_page.logout()
        self.register_page.go_to_this_page()
        self.register_page.register(
        self.fake_person.username + '2',
        self.fake_person.email,
        self.fake_person.password,
        self.fake_person.password, True)
        assert self.register_page.blocked_on_page()
        assert self.register_page.notification_include('User already exist')
        assert self.register_page.notification_text_clear()
