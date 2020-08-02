from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSearsh():
  def test_search(self):
    try:
      link = "https://yandex.ru"
      browser = webdriver.Chrome()
      browser.get(link)

      search_input = browser.find_element(By.ID, 'text')
      search_input.send_keys("leinster")
      search_button = browser.find_element(By.CSS_SELECTOR, '.search2__button>.button')
      search_button.click()
      
      print(browser.current_url)
      assert "leinster" in browser.current_url, "ERRORRRRRRRR!"
    finally:
      browser.quit()