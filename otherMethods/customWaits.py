from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class custom_waits:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_till_element_clickable(self, element):
        return self.wait.until(EC.element_to_be_clickable((By.ID, element)))
