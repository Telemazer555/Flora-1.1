from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from locators.FLORA_LOCATORS import LOCATORS

url = 'https://flora-host-preprod.com-dev.int.rolfcorp.ru/'

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--incognito")
# options.add_argument("--headless")
### включение юзер агента и обнужение автоматизации ###
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "--user-agent=-Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.3-")

driver = webdriver.Chrome(options=options)
driver.get(url)
wait = WebDriverWait(driver, 15, poll_frequency=1)
sleep(3)



### Вводим логин ###
wait.until(EC.visibility_of_element_located(LOCATORS.EMAIL)).click()
wait.until(EC.visibility_of_element_located(LOCATORS.EMAIL)).send_keys('st_pk_asp_mitsu')
### Вводим пароль ###
wait.until(EC.visibility_of_element_located(LOCATORS.PASSWORD)).click()
wait.until(EC.visibility_of_element_located(LOCATORS.PASSWORD)).send_keys('Ww12345!')
### жмём войти  ###
wait.until(EC.visibility_of_element_located(LOCATORS.LOGIN)).click()
### жмём добавить (+)  ###
wait.until(EC.visibility_of_element_located(LOCATORS.ADD_PLUS)).click()
### выбираем тип сделки визит (+)  ###
wait.until(EC.visibility_of_element_located(LOCATORS.VIZIT)).click()
### жмём продолжить  ###
wait.until(EC.visibility_of_element_located(LOCATORS.CONTINUE)).click()
### Вводим ФИО  ###
wait.until(EC.visibility_of_element_located(LOCATORS.FIO)).click()
wait.until(EC.visibility_of_element_located(LOCATORS.FIO_INPUT)).send_keys('Ассылов Евгений Сергеевич')

wait.until(EC.visibility_of_element_located(LOCATORS.FIO_CONTINUE)).click()

wait.until(EC.visibility_of_element_located(LOCATORS.FIO_CONTINUE_2IS4)).click()

wait.until(EC.visibility_of_element_located(LOCATORS.FIO_CONTINUE_2IS4)).click()

wait.until(EC.visibility_of_element_located(LOCATORS.SALE_ASP)).click()

wait.until(EC.visibility_of_element_located(LOCATORS.CONTINUE_ASP)).click()





driver.save_screenshot('sceen.png')
sleep(3000)
