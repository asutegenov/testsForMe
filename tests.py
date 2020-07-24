from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.locators import YandexPageLocators
from pages.search import Search

class TestYandex():
  def test_search_yandex(self, browser):
    try:
      link = "https://yandex.ru"
      pages = Search(browser, link)
      pages.open()
      pages.check_equal_url_and_input_date()
    finally:
      browser.quit()
      