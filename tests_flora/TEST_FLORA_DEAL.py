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
import json


class FLORA:
    # url = 'https://flora-host-preprod.com-dev.int.rolfcorp.ru/'
    # url = 'https://flora-host-dev.com-dev.int.rolfcorp.ru'
    url = 'https://flora-host-test.com-dev.int.rolfcorp.ru/'

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
    wait = WebDriverWait(driver, 20, poll_frequency=1)
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

    DC = wait.until(EC.visibility_of_element_located(LOCATORS.DS_ALTYWKA))
    if DC.text == 'ДЦ Алтуфьево Митцубиши':
        print('всё окей мы на нужном дц)')
    else:
        selection_ds = wait.until(EC.visibility_of_element_located(LOCATORS.DS_ALTYWKA_1)).click()
        selection_ds_close = wait.until(EC.visibility_of_element_located(LOCATORS.DS_ALTYWKA_2)).click()
        selection_ds_else = wait.until(EC.visibility_of_element_located(LOCATORS.DS_ALTYWKA_ELSE)).click()
        selection_ds_mitsu = wait.until(EC.visibility_of_element_located(LOCATORS.DS_ALTYWKA_3))
        scrolls.scroll_to_element(selection_ds_mitsu)
        selection_ds_mitsu.click()
        selection_ds_mitsu_button = wait.until(EC.visibility_of_element_located(LOCATORS.DS_ALTYWKA_4))
        scrolls.scroll_to_element(selection_ds_mitsu_button)
        selection_ds_mitsu_button.click()
        driver.refresh()
        print('кто-то накликал другой дц)')

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
    # wait.until(EC.visibility_of_element_located(LOCATORS.FIO_INPUT)).send_keys('Уткин Евгений Игоревич')
    wait.until(EC.visibility_of_element_located(LOCATORS.FIO_INPUT)).send_keys('Агаев Павел Вячеславович')
    ### Нажимаем Продолжить ###
    DROPDOWN = (wait.until(EC.visibility_of_all_elements_located(LOCATORS.FIO_CONTINUE)))[0]
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
    ADDBUTTON = (long_wait.until(EC.visibility_of_all_elements_located(LOCATORS.ADD2)))[2]
    scrolls.scroll_to_element(ADDBUTTON)
    ADDBUTTON.click()
    ### Дожидаемся пока в сделку добавится а\м больше 1   ###
    SDELKA_ASSERT = long_wait.until(EC.visibility_of_element_located(LOCATORS.SDELKA))
    SDELKA_ASSERT_TEXT = SDELKA_ASSERT.text
    if SDELKA_ASSERT_TEXT > '0':
        SDELKA_ASSERT.click()
    else:
        print('Чёт хуйня какая то хз')

    ### Получаем url пройденной сдеки + записываем его в другой файл   ###
    url_deal = driver.current_url
    with open(file=r'C:\Users\forsw\PycharmProjects\Flora-1.1\locators\555_test-555.py', mode='w',
              encoding='utf-8') as file:
        file.write(url_deal)
        print(url_deal)
    ### Нажимаем на А\М   ###
    SDELKA_AM_KP = wait.until(EC.visibility_of_element_located(LOCATORS.SDELKA_AM))
    scrolls.scroll_to_element(SDELKA_AM_KP)
    SDELKA_AM_KP.click()
    # sleep(12)
    ### Кликаем на 4 пункт дкп   ###
    sleep(12)  ### убрать слипы добавить проверку на появление элемента ну и найти элемент ###
    PDKP = wait.until(EC.visibility_of_all_elements_located(LOCATORS.PDKP))[1]
    PDKP.click()
    ### Кликаем на выбор подписанта    ###
    sleep(12)  ### убрать слипы добавить проверку на появление элемента ну и найти элемент ###
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
    sleep(250000)
