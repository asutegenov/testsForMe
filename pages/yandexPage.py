from pages.base_page import BasePage
from pages.locators import YandexPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YandexPage(BasePage):
  def check_equal_url_and_input_date(self):
    search_input = self.browser.find_element(*YandexPageLocators.SEARCH_INPUT)
    search_input.send_keys("leinster")
    search_button = self.browser.find_element(*YandexPageLocators.SEARCH_BUTTON)
    search_button.click()
    
    assert "leinster" in self.browser.current_url, "leinster don't in URL"
  
  def successful_login_in_yandex_mail(self, test_login, test_passwd):
    #Поиск ссылки на почту
    find_link_to_mail = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((YandexPageLocators.LINK_MAIL)))
    find_link_to_mail.click()

    #Переход на нужную страницу
    new_window = self.browser.window_handles[1]
    self.browser.switch_to.window(new_window)

    #Заполнение формы ввода пароля
    input_login_form = WebDriverWait(self.browser,100).until(EC.visibility_of_element_located((YandexPageLocators.MAIL_INPUT_LOGIN)))
    input_login_form.send_keys(test_login)

    submit = WebDriverWait(self.browser, 100).until(EC.element_to_be_clickable((YandexPageLocators.MAIL_INPUT_SUBMIT)))
    submit.click()

    #Заполнение формы ввода пароля
    input_password_form = WebDriverWait(self.browser,100).until(EC.visibility_of_element_located((YandexPageLocators.MAIL_INPUT_PASSWORD)))
    input_password_form.send_keys(test_passwd)

    submit = WebDriverWait(self.browser, 100).until(EC.element_to_be_clickable((YandexPageLocators.MAIL_INPUT_SUBMIT)))
    submit.click()

    time.sleep(3)

    assert "https://mail.yandex.ru/" in self.browser.current_url, "Не вошел в Яндекс.Почта! Неправильный логин или пароль."

    