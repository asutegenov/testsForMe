from pages.base_page import BasePage
from pages.locators import WikipediaPageLocators
from selenium.webdriver.common.by import By
import time

class WikipediaPage(BasePage):
  def check_correct_born_place_isaak_azimov(self):
    search_input = self.browser.find_element(By.ID, "searchInput")
    search_input.send_keys("Isaac Asimov")
    search_button = self.browser.find_element(By.ID, "searchButton")
    search_button.click()
    search_born_place = self.browser.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[4]/td/a[1]')
    search_born_place.click()
    petrovichi = self.browser.current_url

    assert "https://en.wikipedia.org/wiki/Petrovichi,_Smolensk_Oblast" == petrovichi
