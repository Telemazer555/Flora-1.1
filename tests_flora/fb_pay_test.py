from pages.fb_pay_page import TestFBPay
import time


class TestPay:

    def test_pay(self, driver):
        # url = 'https://dp-aswt:24050/apex/f?p=107:LOGIN_DESKTOP::::::#no-back-button' ### DEV
        url = 'https://dp-aswt:24014/apex/f?p=107:LOGIN_DESKTOP::::::#no-back-button'  ### PRE-PROD
        # url = 'https://dp-aswt:24046/apex/f?p=107:LOGIN_DESKTOP::::::#no-back-button'  ### TEST

        test_fb = TestFBPay(driver, url)
        test_fb.open()
        test_fb.login_fb()
        test_fb.find_vin_and_oplata_pdkp()
        time.sleep(3)
