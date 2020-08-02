from selenium.webdriver.common.by import By
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.common.keys import Keys 

class YandexPageLocators():
    SEARCH_INPUT = (By.ID, "text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search2__button>.button")
