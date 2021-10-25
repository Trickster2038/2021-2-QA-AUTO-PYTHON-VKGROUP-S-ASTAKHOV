from ui.pages.basepage import BasePage
from ui.locators import CampaignPageLocators
from selenium.webdriver.common.by import By
import os
import allure
from allure_commons.types import AttachmentType


class CampaignPage(BasePage):

    locators = CampaignPageLocators

    @allure.step("Go to campaign creating page")
    def go_to_creating(self):
        if self.is_displayed(self.locators.NEW_CAMPAIGN_BTN):
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Campaigns_page", attachment_type=AttachmentType.PNG)
            self.click(self.locators.NEW_CAMPAIGN_BTN)
        else:
            self.wait_clickable(self.locators.FIRST_CAMPAIGN_BTN)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Campaigns_page", attachment_type=AttachmentType.PNG)
            self.click(self.locators.FIRST_CAMPAIGN_BTN)

    @allure.step("Create new campaign")
    def create_campaign_default(self, title="Cmpg caption", body_text="Lorem ipsum"):
        self.go_to_creating()

        self.click(self.locators.COVERAGE_ADVERTISE)
        self.send_keys(self.locators.CAMPAIGN_URL, "https://vk.com/e_mail_ru")

        name_input = self.send_suffux(self.locators.CAMPAIGN_NAME_INPUT)
        name = name_input.get_attribute('value')

        self.click(self.locators.BANNER_FORMAT_IMAGE)

        photo_path = os.path.abspath(
            os.path.join("test_hw2", "media", "default_campaign.jpg"))
        self.send_file(self.locators.IMAGE_INPUT, photo_path)
        self.click(self.locators.IMAGE_SAVE)

        self.send_keys(self.locators.BANNER_TITLE, title)
        self.send_keys(self.locators.BANNER_TEXT, body_text)

        self.click(self.locators.SUBMIT_BANNER)

        date_fields = self.find_all(self.locators.CAMPAIGN_DATES)
        date_fields[0].clear()
        date_fields[0].send_keys("01.01.2022")
        date_fields[1].clear()
        date_fields[1].send_keys("07.01.2022")

        self.send_keys(self.locators.CAMPAIGN_BUDGET_PER_DAY, "100")

        self.click(self.locators.SUBMIT_CAMPAIGN)

        return name

    def campaign_exist(self, name):
        selector = f"//a[contains(@title,'{name}')]"
        return self.exist((By.XPATH, selector))
