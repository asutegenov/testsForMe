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

class WSJPageLocators():
    SEARCH_BUTTON_SIGNIN = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/div[1]/div/div[2]/div/a[2]')
    SEARCH_BUTTON_SUBSCRIBE = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/div[1]/div/div[2]/div/a[1]')

    # Проверка ссылки Africa в меню World
    SEARCH_BUTTON_WORLD = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/nav/ul/li[2]/a')
    SEARCH_BUTTON_AFRICA = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/nav/ul/li[2]/div/div/ul[1]/li[2]/a')

    # Проверка поиска
    SEARCH_BUTTON_SEARCH = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/div[2]/button')
    SEARCH_INPUT_SEARCH = (By.ID , 'searchInput')
    SEARCH_BUTTON_SUBMIT = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/header/div[2]/div/form/input[2]')

class TechCrunchPageLocators():
    SEARCH_LINK_LOGIN = (By.XPATH, '//*[@id="root"]/div/div/header/div/div[2]/div/div[1]/a')
    SEARCH_LOGIN_TITLE = (By.CLASS_NAME, 'challenge>strong')
    SEARCH_BUTTON_MORE = (By.CLASS_NAME, 'more-link>a')
    SEARCH_BUTTON_STARTUP_BATTLEFIELD = (By.XPATH, '//*[@id="root"]/div/div/header/div[2]/div/div[2]/div/ul/li[1]/a')
    