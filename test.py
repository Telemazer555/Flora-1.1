from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from locators.FLORA_LOCATORS import LOCATORS

url = 'https://flora-host-preprod.com-dev.int.rolfcorp.ru/asp_sell/ibw9ixjg2orz/vehicle-need/9ccfd8ac-9f4d-4500-8ec8-919eb8f53c7e/selection'

options = Options()
options.add_argument("--window-size=1920,1080")
# options.add_argument("--incognito")
# options.add_argument("--headless")
### включение юзер агента и обнужение автоматизации ###
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "--user-agent=-Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.3-")
# sleep(25)
# ADDBUTTON = (wait.until(EC.visibility_of_all_elements_located(ADD2)))
# print(len(ADDBUTTON))
# for i in ADDBUTTON:
#     print(i.text)

driver = webdriver.Chrome(options=options)
driver.get(url)
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
### Баттоны которые кликабильные тут к примеру 14\20
ADD2 = 'xpath', '//button[@class="or-button or-button_color-lightpink or-button_th or-button_wide asp-sell-selection__car-buttons-item"]'
ADD3 = 'class name', 'or-button or-button_color-lightpink or-button_th or-button_wide asp-sell-selection__car-buttons-item'
SDELKA = 'xpath', '//span[@class="or-tab-notification t5 or-tab-notification_active"]'

ADDBUTTON = (long_wait.until(EC.visibility_of_all_elements_located(ADD2)))[3]
ADDBUTTON.click()
SDELKA_ASSERT = wait.until(EC.visibility_of_element_located(SDELKA))
SDELKA_ASSERT_TEXT = SDELKA_ASSERT.text
if SDELKA_ASSERT_TEXT > '0':
    SDELKA_ASSERT.click()
else:
    print('Чёт хуйня какая то хз бля')
sleep(25)
print('Успешно пройдено!')