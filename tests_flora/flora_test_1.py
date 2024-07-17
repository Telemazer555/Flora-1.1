from pages.flora_create_page import TestFloraPay
import time


class TestFlora:
    def test_full_sdelka(self, driver):
        # url = 'https://flora-host-asporders.com-dev.int.rolfcorp.ru/'
        # url = 'https://flora-host-dev.com-dev.int.rolfcorp.ru'  ### DEV
        url = 'https://flora-host-preprod.com-dev.int.rolfcorp.ru/'  ### PRE-PROD
        # url = 'https://flora-host-test.com-dev.int.rolfcorp.ru/'    ### TEST

        test_flora = TestFloraPay(driver, url)
        test_flora.open()
        test_flora.flora_login()
        # test_flora.dc_mutsy()
        test_flora.asp_pay_client()
        test_flora.add_automobile()
        # time.sleep(500)
        test_flora.go_to_pdkp_pay_4()
        time.sleep(5)
        test_flora.oformlenie_kp_bez_dopov()
        time.sleep(5)
        test_flora.find_task()

    def test_kp_bez_dopov(self, driver):
        with open(file=r'C:\Users\forsw\PycharmProjects\Flora-1.1\locators\URLS.py', mode='r',
                  encoding='utf-8') as file_vin:
            url = file_vin.read()
        test_testa = TestFloraPay(driver, url)
        test_testa.open()
        test_testa.flora_login()
        test_testa.oformlenie_kp_bez_dopov()

    # def test_task_pred_raswot(self, driver):
    #     task_pred_raswot = TestFloraPay(driver, url)
    #     task_pred_raswot.find_task()
