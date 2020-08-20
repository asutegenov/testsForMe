from pages.base_page import BasePage
from pages.locators import WSJPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WSJPage(BasePage):
  def check_link_sign_in(self):
    search_button = self.browser.find_element(*WSJPageLocators.SEARCH_BUTTON_SIGNIN)
    search_button.click()

    assert "signin" in self.browser.current_url

  def check_link_subscribe(self):
    search_button = self.browser.find_element(*WSJPageLocators.SEARCH_BUTTON_SUBSCRIBE)
    search_button.click()

    assert "store" in self.browser.current_url

