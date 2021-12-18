from selenium.webdriver.common.by import By
from ui.locators.base_locators import BasePageLocators

class MainPageLocators(BasePageLocators):
    LOGOUT_BTN = (By.CSS_SELECTOR, 'a[href="/logout"]')

    ICON_API = (By.CSS_SELECTOR, 'img[src="/static/images/laptop.png"]')
    ICON_FUTURE = (By.CSS_SELECTOR, 'img[src="/static/images/loupe.png"]')
    ICON_SMTP = (By.CSS_SELECTOR, 'img[src="/static/images/analytics.png"]')

    TAB_PYTHON = (By.XPATH, '//a[contains(text(), "Python")]')
    LINK_PYHTON_HISTORY = (By.XPATH, '//a[contains(text(), "Python history")]')
    LINK_FLASK = (By.XPATH, '//a[contains(text(), "About Flask")]')

    TAB_NETWORK = (By.XPATH, '//a[contains(text(), "Network")]')
    LINK_WIRESHARK_NEWS = (By.XPATH, '//a[contains(text(), "News")]')
    LINK_WIRESHARK_DOWNLOAD = (By.CSS_SELECTOR, 'a[href="https://www.wireshark.org/#download"]')
    LINK_EXAMPLES = (By.XPATH, '//a[contains(text(), "Examples")]')

    TAB_LINUX = (By.XPATH, '//a[contains(text(), "Linux")]')
    LINK_CENTOS = (By.XPATH, '//a[contains(text(), "Download Centos7")]')

    ICON_HOME = (By.XPATH, '//a[contains(text(), "HOME")]')
    APP_ICON = (By.CSS_SELECTOR, 'a.uk-navbar-brand[href="/"]')

    VK_ID = (By.XPATH, '//li[contains(text(), "VK ID")]')