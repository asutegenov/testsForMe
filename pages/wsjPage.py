from pages.base_page import BasePage
from pages.locators import WSJPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
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

  def check_link_africa(self, browser):
    search_button_world = self.browser.find_element(*WSJPageLocators.SEARCH_BUTTON_WORLD)
    button_world = AC(browser).move_to_element(search_button_world).perform()

    search_button_africa = self.browser.find_element(*WSJPageLocators.SEARCH_BUTTON_AFRICA)
    search_button_africa.click()

    assert "africa-news" in self.browser.current_url
  
  def check_button_search(self):
    search_button_search = self.browser.find_element(*WSJPageLocators.SEARCH_BUTTON_SEARCH)
    search_button_search.click()

    value_for_search = "apple"

    search_input_search = self.browser.find_element(*WSJPageLocators.SEARCH_INPUT_SEARCH)
    search_input_search.send_keys(value_for_search)
    search_button_submit = self.browser.find_element(*WSJPageLocators.SEARCH_BUTTON_SUBMIT)
    search_button_submit.click()

    assert value_for_search in self.browser.current_url
