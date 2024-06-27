from pages.flora_create_page import TestFloraPay
import time


class TestFlora:
    def test_input_flora(self, driver):
        # url = 'https://flora-host-asporders.com-dev.int.rolfcorp.ru/'
        # url = 'https://flora-host-dev.com-dev.int.rolfcorp.ru'  ### DEV
        url = 'https://flora-host-preprod.com-dev.int.rolfcorp.ru/'  ### PRE-PROD
        # url = 'https://flora-host-test.com-dev.int.rolfcorp.ru/'    ### TEST

        test_flora = TestFloraPay(driver, url)
        test_flora.open()
        test_flora.flora_login()
        test_flora.dc_mutsy()
        test_flora.asp_pay_client()
        test_flora.add_automobile()
        test_flora.go_to_pdkp_pay_4()
        time.sleep(10)
