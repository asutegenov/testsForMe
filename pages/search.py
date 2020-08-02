from pages.base_page import BasePage
from pages.locators import YandexPageLocators
import time

class Search(BasePage):
  def check_equal_url_and_input_date(self):
    search_input = self.browser.find_element(*YandexPageLocators.SEARCH_INPUT)
    search_input.send_keys("leinster")
    search_button = self.browser.find_element(*YandexPageLocators.SEARCH_BUTTON)
    search_button.click()
    
    assert "leinster" in self.browser.current_url, "leinster don't in URL"
    time.sleep(1)
    