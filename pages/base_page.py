from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser:RemoteWebDriver, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
