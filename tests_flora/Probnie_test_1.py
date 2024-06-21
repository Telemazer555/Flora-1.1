from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from locators.FLORA_LOCATORS import LOCATORS
from locators.FLORA_LOCATORS import Scrolls
from selenium.webdriver import Keys

url = 'https://flora-host-preprod.com-dev.int.rolfcorp.ru/asp_sell/iu40ftn8xpad/vehicle-need/fe50a918-d1f1-4c5d-8c5b-30386c4ef510/selection'

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get(url)
action = ActionChains(driver)
scrolls = Scrolls(driver, action)
wait = WebDriverWait(driver, 15, poll_frequency=1)
long_wait = WebDriverWait(driver, 150, poll_frequency=1)
sleep(3)
### Вводим логин ###
wait.until(EC.visibility_of_element_located(LOCATORS.EMAIL)).click()
wait.until(EC.visibility_of_element_located(LOCATORS.EMAIL)).send_keys('st_pk_asp_mitsu')
### Вводим пароль ###
wait.until(EC.visibility_of_element_located(LOCATORS.PASSWORD)).click()
wait.until(EC.visibility_of_element_located(LOCATORS.PASSWORD)).send_keys('Ww12345!')
### жмём войти  ###
wait.until(EC.visibility_of_element_located(LOCATORS.LOGIN)).click()
### Дожидаемся пока в сделку добавится а\м больше 1   ###
SDELKA_ASSERT = long_wait.until(EC.visibility_of_element_located(LOCATORS.SDELKA))
SDELKA_ASSERT_TEXT = SDELKA_ASSERT.text
if SDELKA_ASSERT_TEXT > '0':
    SDELKA_ASSERT.click()
else:
    print('Чёт хуйня какая то хз')
### Нажимаем на А\М   ###
SDELKA_AM_KP = wait.until(EC.visibility_of_element_located(LOCATORS.SDELKA_AM))
scrolls.scroll_to_element(SDELKA_AM_KP)
SDELKA_AM_KP.click()
### Кликаем на 4 пункт дкп   ###
sleep(12)
PDKP = wait.until(EC.visibility_of_all_elements_located(LOCATORS.PDKP))[1]
PDKP.click()
###Прописать if вместо слипа на пустое поле с подписантом ###
sleep(10)
### Кликаем на выбор подписанта    ###
wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_PODPISANT)).click()
PODPISANT = wait.until(EC.visibility_of_all_elements_located(LOCATORS.PDKP_PODPISANT_CLICK))[0]
scrolls.scroll_to_element(PODPISANT)
PODPISANT.click()
### Кликаем и вписываем цену пдкп   ###
INPUT_1 = wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_INPUT_1))
INPUT_1.click()
INPUT_1_1 = wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_INPUT_1_1))
INPUT_1_1.send_keys('60000')
### Кликаем выбираем дату действия пдкп    ###
INPUT_2 = wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_INPUT_2))
INPUT_2.click()
INPUT_2_2 = wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_INPUT_2_2))
INPUT_2_2.send_keys('08.06.2030')
### Кликаем продписать пдкп    ###
wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_BUTTON)).click()

long_wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_BUTTON2)).click()

wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_BUTTON3)).click()

wait.until(EC.visibility_of_element_located(LOCATORS.PDKP_BUTTON4)).click()

class ="payment-need__item-main-title t1"]
