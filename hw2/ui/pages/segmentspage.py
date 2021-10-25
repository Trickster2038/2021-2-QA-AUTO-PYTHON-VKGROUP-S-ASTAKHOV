from ui.pages.basepage import BasePage
from ui.locators import SegmentPageLocators
from selenium.webdriver.common.by import By
import time


class SegmentPage(BasePage):

    locators = SegmentPageLocators

    def go_to_creating(self):
        if self.is_displayed(self.locators.NEW_SEGMENT_BTN):
            self.click(self.locators.NEW_SEGMENT_BTN)
        else:
            self.click(self.locators.FIRST_SEGMENT_BTN)

    def create_segment_default(self):
        self.go_to_creating()

        self.click(self.locators.SEGMENT_SOURCE_PAYED_N_PLAYED)
        self.click(self.locators.SUBMIT_SOURCE_BTN)

        name_input = self.find(self.locators.SEGMENT_NAME_INPUT)
        name = name_input.get_attribute('value')

        self.click(self.locators.SUBMIT_SEGMENT)

        return name

    def segment_exist(self, name):
        selector = f"//a[contains(@title,'{name}') and not(@hidden)]"
        return self.exist((By.XPATH, selector))

    def delete_segment(self, name):
        selector = f"//a[contains(@title, '{name}')]/../../following-sibling::div[4]/span"
        self.click((By.XPATH, selector))
        self.click(self.locators.CONFIRM_DELETE)
        return self.wait_expired((By.XPATH, f"//a[contains(@title,'{name}') and not(@hidden)]"))
