from selenium.webdriver.common.by import By
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.common.keys import Keys 

class YandexPageLocators():
    SEARCH_INPUT = (By.ID, "text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search2__button>.button")

    LINK_MAIL = (By.CLASS_NAME, "desk-notif-card__login-enter-expanded")

    MAIL_INPUT_LOGIN = (By.ID, "passp-field-login") 
    MAIL_INPUT_PASSWORD = (By.ID, "passp-field-passwd")
    
    MAIL_INPUT_SUBMIT = (By.CLASS_NAME, "Button2_type_submit")
    