from pages.base_page import BasePage
from pages.locators import TechCrunchPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TechCrunchPage(BasePage):
  def check_link_login_on_start_page(self, browser):
    search_button_login = self.browser.find_element(*TechCrunchPageLocators.SEARCH_LINK_LOGIN)
    search_button_login.click()
    search_login_title = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((*TechCrunchPageLocators.SEARCH_LOGIN_TITLE,)))

    assert "Sign in" == search_login_title.text

  def check_startup_battlefield_in_right_list(self, browser):
    search_button_more = self.browser.find_element(*TechCrunchPageLocators.SEARCH_BUTTON_MORE)
    search_button_more.click()
    search_button_startup_battlefield = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((*TechCrunchPageLocators.SEARCH_BUTTON_STARTUP_BATTLEFIELD,)))
    search_button_startup_battlefield.click()

    assert "startup-battlefield" in self.browser.current_url

  def check_link_translate_to_japan(self):
    search_button_jpan = self.browser.find_element(*TechCrunchPageLocators.SEARCH_BUTTON_JAPAN)
    search_button_jpan.click()

    assert "jp" in self.browser.current_url

  def check_link_search(self):
    search_button_search = self.browser.find_element(*TechCrunchPageLocators.SEARCH_BUTTON_SEARCH)
    search_button_search.click()
    search_input_search = self.browser.find_element(*TechCrunchPageLocators.SEARCH_INPUT_SEARCH)
    value_for_input = "apple"
    search_input_search.send_keys(value_for_input + "\ue007")

    assert value_for_input in self.browser.current_url
