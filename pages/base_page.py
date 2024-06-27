from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=30):
        return wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def element_is_visible_long(self, locator, timeout=120):
        return wait(self.driver, timeout, poll_frequency=3).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=30):
        return wait(self.driver, timeout, poll_frequency=1).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=30):
        return wait(self.driver, timeout, poll_frequency=1).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)

    def find(self, *args):
        return self.driver.find_elements(*args)

    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def refresh(self):
        self.driver.refresh()
