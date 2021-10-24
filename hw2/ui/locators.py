from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_BTN = (By.XPATH, "//div[starts-with(@class, 'responseHead-module-button')]")
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_SUBMIT = (By.XPATH, "//div[starts-with(@class, 'authForm-module-button')]")
    UNSUPPORTED_LOGIN_NOTICE = (By.XPATH, "//div[starts-with(@class,'notify')]")

    TAB_CAMPAIGN = (By.XPATH, "//a[contains(@class,'center-module-campaigns')]")

class CampaignPageLocators(BasePageLocators):
    FIRST_CAMPAIGN_BTN = (By.CSS_SELECTOR, 'a[href="/campaign/new"')
    NEW_CAMPAIGN_BTN = (By.XPATH, "//div[contains(@class,'dashboard-module-createButtonWrap')]")

    COVERAGE_ADVERTISE = (By.XPATH, "//div[contains(@class,'column-list-item _reach')]")
    CAMPAIGN_URL = (By.XPATH, "//input[contains(@class,'mainUrl')]")
    CAMPAIGN_NAME_INPUT = (By.CSS_SELECTOR, "input.input__inp.js-form-element")

    ADDRESS_SEARCH_INPUT = (By.XPATH, "//input[contains(@class,'multi')]")
    ADDRESS_LIST_ELEM = (By.XPATH, "//span[contains(@class,'billboard')]")
    ADDRESS_SUBMIT = (By.XPATH, "//div[contains(@class,'bubbleComponent-module-submit')]")

    BANNER_FORMAT_IMAGE = (By.XPATH, "//div[contains(@id,'patterns_teaser')]")

    IMAGE_INPUT = (By.CSS_SELECTOR, 'input[data-test="image_90x75"]')
    IMAGE_SAVE = (By.CLASS_NAME, "image-cropper__save")

    BANNER_TITLE = (By.XPATH, "//input[contains(@data-name,'title')]")
    BANNER_TEXT = (By.XPATH, "//textarea[contains(@data-name,'text')]")

    SUBMIT_BANNER = (By.CSS_SELECTOR, 'div[data-test="submit_banner_button"]')

    CAMPAIGN_DATES = (By.CLASS_NAME, "date-setting__date-input")

    CAMPAIGN_BUDGET_PER_DAY = (By.CSS_SELECTOR, 'input[data-test="budget-per_day"]')

    SUBMIT_CAMPAIGN = (By.CLASS_NAME, 'js-save-button-wrap')