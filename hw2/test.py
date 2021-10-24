from ui.pages.mainpage import MainPage
import time

def test_one(browser):
    page = MainPage(browser)
    page.go_to_page()
    time.sleep(3)
    assert 1 == 1