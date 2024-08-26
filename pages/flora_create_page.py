import time
import random
from pages.base_page import BasePage
from locators.FLORA_LOCATORS import LOCATORS


class TestFloraPay(BasePage):
    locators = LOCATORS

    def flora_login(self):
        self.element_is_visible(self.locators.EMAIL).click()
        self.element_is_visible(self.locators.EMAIL).send_keys('st_pk_asp_mitsu')
        self.element_is_visible(self.locators.PASSWORD).click()
        self.element_is_visible(self.locators.PASSWORD).send_keys('Ww12345!')
        self.element_is_visible(self.locators.LOGIN).click()

    def dc_mutsy(self):

        DC = self.element_is_visible(LOCATORS.DS_ALTYWKA)
        if DC.text == 'ДЦ Алтуфьево Митцубиши':
            print('всё окей мы на нужном дц)')

        else:
            self.element_is_visible(self.locators.DS_ALTYWKA_1).click()
            self.element_is_visible(self.locators.DS_ALTYWKA_2).click()
            self.element_is_visible(self.locators.DS_ALTYWKA_ELSE).click()
            DS_SCROLL = self.element_is_visible(self.locators.DS_ALTYWKA_3)
            self.go_to_element(DS_SCROLL)
            DS_SCROLL.click()
            MUTSY_SCROLL = self.element_is_visible(self.locators.DS_ALTYWKA_4)
            self.go_to_element(MUTSY_SCROLL)
            MUTSY_SCROLL.click()
            self.refresh()

    def asp_pay_client(self):
        self.element_is_visible(LOCATORS.ADD_PLUS).click()
        self.element_is_visible(LOCATORS.VIZIT).click()
        self.element_is_visible(LOCATORS.CONTINUE).click()
        self.element_is_visible(LOCATORS.FIO).click()
        # self.element_is_visible(LOCATORS.FIO_INPUT).send_keys('Агаев Павел Вячеславович')
        self.element_is_visible(LOCATORS.FIO_INPUT).send_keys('Вишнякова Полина Владимировна')
        self.elements_are_visible(LOCATORS.FIO_CONTINUE)[0].click()
        self.element_is_visible(LOCATORS.FIO_CONTINUE_2IS4).click()
        self.element_is_visible(LOCATORS.SALE_ASP).click()
        self.element_is_visible(LOCATORS.CONTINUE_ASP).click()
        self.element_is_visible(LOCATORS.CHOICE_DS).click()
        self.element_is_visible(LOCATORS.CHOICE_DS_1).click()
        self.element_is_visible(LOCATORS.INPYT_SOTR).click()
        self.element_is_visible(LOCATORS.NAZNACIT).click()
        self.element_is_visible(LOCATORS.BATTON).click()
        self.element_is_visible(LOCATORS.ASP).click()

    def add_automobile(self):
        ADDBUTTON = self.elements_are_visible(LOCATORS.ADD2)[random.randint(0, 10)]
        self.go_to_element(ADDBUTTON)
        ADDBUTTON.click()
        VIN_ASERT = self.element_is_visible_long(LOCATORS.VIN_ASERT)
        if VIN_ASERT.text == 'Добавлено':
            VIN = self.element_is_visible(LOCATORS.VIN)
            print(VIN.text)
            with open(file=r'C:\Users\forsw\PycharmProjects\Flora-1.1\locators\VIN.py', mode='w',
                      encoding='utf-8') as file_vin:
                file_vin.write(VIN.text)

        SDELKA_ASSERT = self.element_is_visible_long(LOCATORS.SDELKA)
        SDELKA_ASSERT_TEXT = SDELKA_ASSERT.text
        if SDELKA_ASSERT_TEXT > '0':
            SDELKA_ASSERT.click()
        else:
            print('Чёт хуйня какая то хз')

        url_deal = self.driver.current_url
        with open(file=r'C:\Users\forsw\PycharmProjects\Flora-1.1\locators\URLS.py', mode='w',
                  encoding='utf-8') as file_url:
            file_url.write(url_deal)
            print(url_deal)
        SDELKA_AM_KP = self.element_is_visible(LOCATORS.SDELKA_AM)
        self.go_to_element(SDELKA_AM_KP)
        SDELKA_AM_KP.click()

    def go_to_pdkp_pay_4(self):
        time.sleep(12)
        self.elements_are_visible(LOCATORS.PDKP)[1].click()
        time.sleep(12)
        self.element_is_visible(LOCATORS.PDKP_PODPISANT).click()
        # print('Вот тут надо смотреть крыче')
        # time.sleep(1200)
        PODPISANT = self.elements_are_visible(LOCATORS.PDKP_PODPISANT_CLICK)[0]
        self.go_to_element(PODPISANT)
        PODPISANT.click()
        self.element_is_visible(LOCATORS.PDKP_INPUT_1).click()
        self.element_is_visible(LOCATORS.PDKP_INPUT_1_1).send_keys('60000')
        self.element_is_visible(LOCATORS.PDKP_INPUT_2).click()
        self.element_is_visible(LOCATORS.PDKP_INPUT_2_2).send_keys('08.06.2030')
        self.element_is_visible(LOCATORS.PDKP_BUTTON).click()
        self.element_is_visible(LOCATORS.PDKP_BUTTON2).click() ### падает с таймаутом
        self.element_is_visible(LOCATORS.PDKP_BUTTON3).click()
        self.element_is_visible(LOCATORS.PDKP_BUTTON4).click()
        self.element_is_visible(LOCATORS.PAY_BUTTON).click()
        self.element_is_visible(LOCATORS.PAY_BUTTON_CASSA).click()
        self.element_is_visible(LOCATORS.PAY_BUTTON_FORM).click()
        self.element_is_visible(LOCATORS.PAY_BUTTON_FORM_CLIK).click()
        # self.element_is_clickable(LOCATORS.PAY_BUTTON_FORM_CLIK_OK).click()

    def oformlenie_kp_bez_dopov(self):
        self.element_is_visible_long(LOCATORS.SDELKA).click() #### Решить вопрос с этой строкой
        self.element_is_visible_long(LOCATORS.SDELKA_AM).click()
        self.elements_are_visible(LOCATORS.PDKP)[1].click()
        KP_BUTTON = self.element_is_visible_long(LOCATORS.KP_BUTTON)
        self.go_to_element(KP_BUTTON)
        KP_BUTTON.click()
        self.element_is_visible_long(LOCATORS.KP_BUTTON_YES).click()
        Task = self.elements_are_visible(LOCATORS.NUMBER_TASK)[1]
        with open(file=r'C:\Users\forsw\PycharmProjects\Flora-1.1\locators\TASK.py', mode='w',
                  encoding='utf-8') as file_vin:
            file_vin.write(Task.text)

    def find_task(self):
        self.element_is_visible(LOCATORS.WORK_TABLES).click()
        self.element_is_visible(LOCATORS.TASKS).click()
