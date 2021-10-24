from ui.pages.basepage import BasePage
from ui.locators import CampaignPageLocators
from selenium.webdriver.common.by import By
import os


class CampaignPage(BasePage):

    locators = CampaignPageLocators

    def go_to_creating(self):
        if self.exist(self.locators.FIRST_CAMPAIGN_BTN):
            self.click(self.locators.FIRST_CAMPAIGN_BTN)
        else:
            self.click(self.locators.NEW_CAMPAIGN_BTN)

    def create_campaign_default(self, title="Cmpg caption", body_text="Lorem ipsum"):
        self.go_to_creating()

        self.click(self.locators.COVERAGE_ADVERTISE)
        self.send_keys(self.locators.CAMPAIGN_URL, "https://vk.com/e_mail_ru")

        name_input = self.find(self.locators.CAMPAIGN_NAME_INPUT)
        self.last_campaign_name = name_input.text

        self.click(self.locators.BANNER_FORMAT_IMAGE)

        photo_path = os.path.abspath(os.path.join("media", "default_campaign.jpg"))
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

    def last_campaign_added(self):
        selector = f"//a[contains(@title,'{self.last_campaign_name}')]"
        return self.exist((By.XPATH, selector))

    
