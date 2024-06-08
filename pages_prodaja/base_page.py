class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver = url

    def open(self):
        self.driver.get(self.url)
