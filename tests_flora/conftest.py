from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
# from selenium.webdriver.common.action_chains import ActionChains
# from locators.FLORA_LOCATORS import Scrolls


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    # action = ActionChains(driver)
    # scrolls = Scrolls(driver, action)
    # yield driver
    # driver.quit()
    return driver
