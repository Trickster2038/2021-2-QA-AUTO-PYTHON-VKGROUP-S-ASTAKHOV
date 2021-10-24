from ui.pages.basepage import BasePage

class MainPage(BasePage):

    url = "https://target.my.com"

    def go_to_page(self):
        return self.driver.get(self.url)