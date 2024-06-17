from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from locators.FLORA_LOCATORS import LOCATORS
from locators.FLORA_LOCATORS import Scrolls

url = 'https://flora-host-preprod.com-dev.int.rolfcorp.ru/'
# url = 'https://flora-host-dev.com-dev.int.rolfcorp.ru'
# url = 'https://flora-host-test.com-dev.int.rolfcorp.ru/'

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
wait = WebDriverWait(driver, 30, poll_frequency=1)
long_wait = WebDriverWait(driver, 120, poll_frequency=1)
action = ActionChains(driver)
scrolls = Scrolls(driver, action)
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
### жмём в поле ФИО  ###
wait.until(EC.visibility_of_element_located(LOCATORS.FIO)).click()
### Вводим ФИО  ###
# wait.until(EC.visibility_of_element_located(LOCATORS.FIO_INPUT)).send_keys('Ассылов Евгений Сергеевич')
wait.until(EC.visibility_of_element_located(LOCATORS.FIO_INPUT)).send_keys('Уткин Евгений Игоревич')
### Нажимаем Продолжить ###
DROPDOWN = (wait.until(EC.visibility_of_all_elements_located(LOCATORS.FIO_CONTINUE)))[2]
DROPDOWN.click()
### Выбор в выпадающем окне  ###
wait.until(EC.visibility_of_element_located(LOCATORS.FIO_CONTINUE_2IS4)).click()
# wait.until(EC.visibility_of_element_located(LOCATORS.FIO_CONTINUE_2IS4)).click()
### Нажатие продолжить  ###
wait.until(EC.visibility_of_element_located(LOCATORS.FIO_CONTINUE_2IS4)).click()
### Выбор продажи АСП ###
wait.until(EC.visibility_of_element_located(LOCATORS.SALE_ASP)).click()
### жмём кнопку продолжить ###
wait.until(EC.visibility_of_element_located(LOCATORS.CONTINUE_ASP)).click()
### нажимаем в поле выбор сотрудника  ###
wait.until(EC.visibility_of_element_located(LOCATORS.INPYT_SOTR)).click()
### Назначаем себя  ###
wait.until(EC.visibility_of_element_located(LOCATORS.NAZNACIT)).click()
### жмём создать потребность ###
wait.until(EC.visibility_of_element_located(LOCATORS.BATTON)).click()
### Заходим в потребность  ###
wait.until(EC.visibility_of_element_located(LOCATORS.ASP)).click()
### Добавляем а\м в сделку   ###
ADDBUTTON = (long_wait.until(EC.visibility_of_all_elements_located(LOCATORS.ADD2)))[3]
ADDBUTTON.click()
### Дожидаемся пока в сделку добавится а\м больше 1   ###
SDELKA_ASSERT = long_wait.until(EC.visibility_of_element_located(LOCATORS.SDELKA))
SDELKA_ASSERT_TEXT = SDELKA_ASSERT.text
if SDELKA_ASSERT_TEXT > '0':
    SDELKA_ASSERT.click()
else:
    print('Чёт хуйня какая то хз')
# sleep(250)
### Нажимаем на А\М   ###
wait.until(EC.visibility_of_element_located(LOCATORS.SDELKA_AM)).click()
### На шаге формирования кп нажимаем продолжить   ###
sleep(4000)
# BUTTON_AM = wait.until(EC.text_to_be_present_in_element_value(LOCATORS.SDELKA_BUTTON, 'Продолжить'))
# BUTTON_AM = wait.until(EC.invisibility_of_element(LOCATORS.SDELKA_BUTTON))
#
# BUTTON_AM = driver.find_element(LOCATORS.SDELKA_BUTTON)
# scrolls.scroll_to_element(LOCATORS.SDELKA_BUTTON)
# BUTTON_AM.click()

#
# wait.until(EC.visibility_of_element_located(LOCATORS.SDELKA_BUTTON_YES)).click()
# wait.until(EC.visibility_of_element_located(LOCATORS.SDELKA_BUTTON_YES)).click()
# sleep(250)
