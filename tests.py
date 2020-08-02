from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.locators import YandexPageLocators
from pages.yandexPage import YandexPage

class TestYandex():
  # def test_search_yandex(self, browser):
  #   try:
  #     link = "https://yandex.ru"
  #     pages = YandexPage(browser, link)
  #     pages.open()
  #     pages.check_equal_url_and_input_date()
  #   finally:
  #     browser.quit()
  
  def test_successful_login_in_yandex_mail(self, browser):
    try:
      test_login = input("Введите, пожалуйста, логин:  ")
      test_passwd = input("Введите, пожалуйста, пароль: ")
      link = "https://yandex.ru"
      pages = YandexPage(browser, link)
      pages.open()
      pages.successful_login_in_yandex_mail(test_login, test_passwd)
    finally:
      browser.quit()