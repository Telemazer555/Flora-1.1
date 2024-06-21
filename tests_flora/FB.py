from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from locators.FLORA_LOCATORS import LOCATORS_FB
from locators.FLORA_LOCATORS import Scrolls
import json


class FB:
    # url = 'https://dp-aswt:24050/apex/f?p=107:LOGIN_DESKTOP::::::#no-back-button' ### DEV
    url = 'https://dp-aswt:24014/apex/f?p=107:LOGIN_DESKTOP::::::#no-back-button'  ### PRE-PROD
    # url = 'https://dp-aswt:24046/apex/f?p=107:LOGIN_DESKTOP::::::#no-back-button' ### TEST

    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    ### включение юзер агента и обнужение автоматизации ###
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument(
    #     "--user-agent=-Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.3-")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 20, poll_frequency=1)
    long_wait = WebDriverWait(driver, 600, poll_frequency=1)
    action = ActionChains(driver)
    scrolls = Scrolls(driver, action)
    with open(file=r'C:\Users\forsw\PycharmProjects\Flora-1.1\locators\VIN.py', mode='r',
              encoding='utf-8') as file_vin:
        VIN = file_vin.read()

    ### Вводим логин ###
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.EMAIL)).click()
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.EMAIL)).send_keys('nfkohtyuk')
    ### Вводим пароль ###
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.PASSWORD)).click()
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.PASSWORD)).send_keys('15399123123')
    ### жмём войти  ###
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.LOGIN)).click()
    ### жмём закрыть
    wait.until(EC.visibility_of_all_elements_located(LOCATORS_FB.CLOSE))[0].click()
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.DOKYMENT)).click()
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.SOP)).click()
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.VIN)).send_keys(VIN)
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.BUTTON_GO)).click()
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.HREF)).click()
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.PAY)).click()
    wait.until(EC.visibility_of_element_located(LOCATORS_FB.PAY_BUTTON)).click()
    SAVE = wait.until(EC.visibility_of_element_located(LOCATORS_FB.PAY_BUTTON_SAVE))
    SAVE.click()
    print('Предоплата прошла !')
