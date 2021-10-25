from allure_commons.types import ALLURE_UNIQUE_LABELS
from ui.pages.basepage import BasePage
from ui.locators import SegmentPageLocators
from selenium.webdriver.common.by import By
import time
import allure
from allure_commons.types import AttachmentType


class SegmentPage(BasePage):

    locators = SegmentPageLocators

    @allure.step("Open segment creating page")
    def go_to_creating(self):
        if self.is_displayed(self.locators.NEW_SEGMENT_BTN):
            self.wait_visible(self.locators.TABLE_HEADERS)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Segments_page", attachment_type=AttachmentType.PNG)
            self.click(self.locators.NEW_SEGMENT_BTN)
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Segments_page", attachment_type=AttachmentType.PNG)
            self.click(self.locators.FIRST_SEGMENT_BTN)

    @allure.step("Create new segment")
    def create_segment_default(self):
        self.go_to_creating()

        self.click(self.locators.SEGMENT_SOURCE_PAYED_N_PLAYED)
        self.click(self.locators.SUBMIT_SOURCE_BTN)

        name_input = self.send_suffux(self.locators.SEGMENT_NAME_INPUT)
        name = name_input.get_attribute('value')

        self.click(self.locators.SUBMIT_SEGMENT)

        self.logger.info(f"Segment {name} created")

        return name

    def segment_exist(self, name):
        selector = f"//a[contains(@title,'{name}') and not(@hidden)]"
        return self.exist((By.XPATH, selector))

    @allure.step("Segment deleted")
    def delete_segment(self, name):
        self.logger.info(f"Deleting {name} segment")
        selector = f"//a[contains(@title, '{name}')]/../../following-sibling::div[4]/span"
        self.click((By.XPATH, selector))
        self.click(self.locators.CONFIRM_DELETE)
        return self.wait_expired((By.XPATH, f"//a[contains(@title,'{name}') and not(@hidden)]"))
