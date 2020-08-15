from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class selectHotel_page_elements:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)


class customWaits(selectHotel_page_elements):
    def wait_till_element_displays(self, element):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, element)))

    def wait_till_element_visible(self, element):
        return self.wait.until(EC.invisibility_of_element((By.XPATH, element)))

    def wait_till_element_clickable(self, element):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))