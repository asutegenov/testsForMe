from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.locators import YandexPageLocators
from pages.yandexPage import YandexPage
from pages.wsjPage import WSJPage
from pages.techcrunchPage import TechCrunchPage

# class TestYandex():
#   def test_search_yandex(self, browser):
#     try:
#       link = "https://yandex.ru"
#       pages = YandexPage(browser, link)
#       pages.open()
#       pages.check_equal_url_and_input_date()
#     finally:
#       browser.quit()

#   def test_successful_login_in_yandex_mail(self, browser):
#     try:
#       test_login = input("Введите, пожалуйста, логин:  ")
#       test_passwd = input("Введите, пожалуйста, пароль: ")
#       link = "https://yandex.ru"
#       pages = YandexPage(browser, link)
#       pages.open()
#       pages.successful_login_in_yandex_mail(test_login, test_passwd)
#     finally:
#       browser.quit()

class TestWSJ():
  def test_on_start_page_wsj_link_signin(self, browser):
    try:
      link = "https://www.wsj.com/"
      pages = WSJPage(browser, link)
      pages.open()
      pages.check_link_sign_in()
    finally:
      browser.quit()

  def test_on_start_page_wsj_link_subscribe(self, browser):
    try:
      link = "https://www.wsj.com/"
      pages = WSJPage(browser, link)
      pages.open()
      pages.check_link_subscribe()
    finally:
      browser.quit()
   
class TestTechCrunch():
  def test_on_start_page_link_login(self,browser):
    try:
      link = "https://techcrunch.com/"
      pages = TechCrunchPage(browser, link)
      pages.open()
      pages.check_link_login_on_start_page(browser)
    finally:
      browser.quit()
  def test_on_start_page_right_list_startup_battlefield(self, browser):
    try:
      link = "https://techcrunch.com/"
      pages = TechCrunchPage(browser, link)
      pages.open()
      pages.check_startup_battlefield_in_right_list(browser)
    finally:
      browser.quit()
      

      