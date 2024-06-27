from pages.base_page import BasePage
from locators.FLORA_LOCATORS import LOCATORS_FB
import time


class TestFBPay(BasePage):
    locators = LOCATORS_FB

    def login_fb(self):
        self.element_is_visible(self.locators.EMAIL).click()
        self.element_is_visible(self.locators.EMAIL).send_keys('nfkohtyuk')
        self.element_is_visible(self.locators.PASSWORD).click()
        self.element_is_visible(self.locators.PASSWORD).send_keys('15399123123')
        self.element_is_visible(self.locators.LOGIN).click()

    def find_vin_and_oplata_pdkp(self):
        with open(file=r'C:\Users\forsw\PycharmProjects\Flora-1.1\locators\VIN.py', mode='r',
                  encoding='utf-8') as file_vin:
            VIN = file_vin.read()
        self.elements_are_visible(self.locators.CLOSE)[0].click()
        self.element_is_visible(self.locators.DOKYMENT).click()
        self.element_is_visible(self.locators.SOP).click()
        self.element_is_visible(self.locators.VIN).send_keys(VIN)
        self.element_is_visible(self.locators.BUTTON_GO).click()
        self.element_is_visible(self.locators.HREF).click()
        time.sleep(60)
        FB_PAY = self.element_is_visible_long(self.locators.PAY)
        self.go_to_element(FB_PAY)
        FB_PAY.click()
        self.element_is_visible(self.locators.PAY_BUTTON).click()
        self.element_is_visible(self.locators.PAY_BUTTON_SAVE).click()
