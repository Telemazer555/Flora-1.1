import time

from pages_prodaja.base_page import BasePage


def test(driver):
    page = BasePage (driver, 'https://keycloak.com-dev.int.rolfcorp.ru/realms/COREAPP-DEV/protocol/openid-connect/auth?client_id=CORE&redirect_uri=https%3A%2F%2Fflora-host-preprod.com-dev.int.rolfcorp.ru%2F&state=03538c64-3224-4077-83cb-74bdc92998b0&response_mode=fragment&response_type=code&scope=openid&nonce=3a50f362-5b52-4a03-b1a4-628f32153813')
    page.open()
    time.sleep(3)