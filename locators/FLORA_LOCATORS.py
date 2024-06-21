class Scrolls:

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, element):
        self.action.scroll_to_element(element).perform()
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 900,
        });
        """)


class LOCATORS_FB:
    EMAIL = ("xpath", '//input[@class="text_field apex-item-text"]')
    PASSWORD = ("xpath", '//input[@class="password apex-item-text"]')
    LOGIN = ("xpath", '//button[@class="button-default "]')
    CLOSE = ("xpath", '//button[@class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"]')
    DOKYMENT = ("xpath", '//ul[@id="tabs"]//li[@class="first-current"]')
    SOP = ("xpath", '//a[text()="СОП на подержанные а/м"]')
    VIN = ("xpath", '//input[@name="P264_VIN"]')
    BUTTON_GO = ("xpath", '//button[@value="Применить"]')
    HREF = ("xpath", '//td[@class=" u-tL"]/a/img')
    PAY = ("xpath", '//a[@class="link_payment"]')
    PAY_BUTTON = ("xpath", '//fieldset[@class="checkbox_group apex-item-checkbox"]/input[@id="P262_PAID_UP_0"]')
    PAY_BUTTON_SAVE = ("xpath", '//button[@class="button-default"]/span[text()="Сохранить платеж"]')


class LOCATORS:
    EMAIL = ("id", "username")
    PASSWORD = ("id", "password")
    LOGIN = ("id", "kc-login")
    DS_ALTYWKA = ('xpath', '//div[@class="time-tracker__dc t4"]')
    VIN = ('xpath',
           '//span[text()="Добавлено"]//ancestor::*[@class="asp-sell-selection__car-block"]//span[@class="asp-sell-selection__car-vin"]')
    VIN_ASERT = ('xpath', '//div[@class="asp-sell-selection__car"]//span[text()="Добавлено"]')
    DS_ALTYWKA_1 = ('xpath', '//div[@class="timer-button t1 timer-button_started timer-button_with-events"]')
    DS_ALTYWKA_2 = (
        'xpath',
        '//button[@class="or-button or-button_color-pink or-button_md-fluid or-button_wide or-button_primary"]')
    DS_ALTYWKA_ELSE = ('xpath', '//*[text()="Начать рабочий день"]')
    DS_ALTYWKA_3 = ('xpath', '//*[text()="ДЦ Алтуфьево Митцубиши" ]')
    DS_ALTYWKA_4 = (
        'xpath',
        '//button[@class="or-button or-button_color-pink or-button_md-fluid or-button_wide or-button_primary"]')

    ADD_PLUS = ('xpath', '/html/body/div/div[1]/div/header/div[1]/button/span[1]')
    VIZIT = (
        'xpath', '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div[2]/div/div/button[1]')
    CONTINUE = (
        'xpath',
        '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/button/span')
    FIO = ('xpath',
           '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div')
    FIO_INPUT = ('xpath',
                 '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/input')
    FIO_CONTINUE = ('xpath',
                    '//div[@class="or-select-item search-client-widget__item"]')

    FIO_CONTINUE_2IS4 = ('xpath',
                         '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div')
    SALE_ASP = ('xpath',
                '//*[@id="app"]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div[1]/div[2]')
    CONTINUE_ASP = ('xpath',
                    '//*[@id="app"]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div[1]/div[2]/div/button[2]')
    INPYT_SOTR = ('xpath',
                  '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[4]/div[2]/div/div[3]/div/div/div/div/div[2]/input')
    NAZNACIT = ('xpath',
                '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[4]/div[2]/div/div[3]/div/div/div[2]/button')
    BATTON = ('xpath',
              '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[4]/div[1]/div[2]/div/button[2]')
    ASP = ('xpath',
           '/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div/div/main/div/section/div/div/div[1]/div[1]/p')
    ADD2 = 'xpath', '//button[@class="or-button or-button_color-lightpink or-button_th or-button_wide asp-sell-selection__car-buttons-item"]'
    SDELKA = 'xpath', '//span[@class="or-tab-notification t5 or-tab-notification_active"]'
    SDELKA_AM = 'xpath', '//div[@class="asp-deal__panel-car-content"]'
    SDELKA_BUTTON = 'xpath', '//button[@class = "or-button or-button_color-pink or-button_md or-button_wide or-button_primary asp-deal-sell-offer-generation__submit-button"]'
    SDELKA_BUTTON_YES = 'xpath', '//button[@class="or-button or-button_color-pink or-button_md-fluid or-button_wide or-button_primary confirm-option-modal__footer-button"]'
    PDKP = 'xpath', '//li[@class="asp-deal__content-panel-list-item"]'
    PDKP_PODPISANT = 'xpath', '//div[@class="or-autocomplete__inner-search"]'
    PDKP_PODPISANT_CLICK = 'xpath', '//ul[@class="or-autocomplete__options-list"]//li'
    PDKP_INPUT_1 = 'xpath', '//div[@class="or-base-input__wrapper or-base-input__wrapper_filled or-base-input__wrapper_label-as-placeholder or-base-input__wrapper_append"]'
    PDKP_INPUT_1_1 = 'xpath', '/html/body/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/input'
    PDKP_INPUT_2 = 'xpath', '//div[@class="or-base-input__wrapper or-base-input__wrapper_label-as-placeholder"]'
    PDKP_INPUT_2_2 = 'xpath', '/html/body/div[1]/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[4]/div/div/div[2]/div/div/div/div[1]/div/div[2]/input'
    PDKP_BUTTON = 'xpath', '//button[@class="or-button or-button_color-lightpink or-button_md or-button_wide asp-deal-sign-pdkp__actions-submit"]'
    PDKP_BUTTON2 = 'xpath', '//button[@class="or-button or-button_color-lightpink or-button_th or-button_wide legal-document-card__control-button"]'
    PDKP_BUTTON3 = 'xpath', '//div[@class="or-checkbox__button or-checkbox__button_md or-checkbox__button_usual"]'
    PDKP_BUTTON4 = 'xpath', '//button[@class="or-button or-button_color-lightpink or-button_md-fluid or-button_wide legal-document-modal__footer-buttons-item"]'
    PAY_BUTTON = 'xpath', '//span[text()="не выбран"]'
    PAY_BUTTON_CASSA = 'xpath', '//li[@class="or-select__options-list-item"]//span[text()="Через операционную кассу"]'
    PAY_BUTTON_FORM = 'xpath', '//button[@class="or-button or-button_color-pink or-button_m or-button_wide or-button_primary t2"]'
    PAY_BUTTON_FORM_CLIK = 'xpath', '//button[@class="or-button or-button_color-pink or-button_xl or-button_wide or-button_primary payment-params__content-footer-button"]'
