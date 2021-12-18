from faker import Faker
import allure
import threading
import allure

class FakeUser():

    fake = Faker()
    lock = threading.Lock()
    username = None
    password = None
    email = None

    @allure.step('Init user')
    def __init__(self):
        name = FakeUser.fake.unique.first_name()
        while len(name) < 7:
            name = FakeUser.fake.unique.first_name()
        self.username = name
        self.password = ''.join(FakeUser.fake.words(3))
        self.email = FakeUser.fake.unique.last_name() + '@gmail.com'
        self.allure_display()

    def allure_display(self):
        record = f"Name: {self.username} \
        \nEmail: {self.email} \
        \nPassword: {self.password}"
        allure.attach(record, 'User', allure.attachment_type.TEXT)
