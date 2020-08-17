import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class selectHotel_page_elements:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def hotel_name(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"_xcsyj0")]')

    def show_amentities_button(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"_1tv4hg3")]')

    def amentities_text(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"_svr7sj")]')

    def get_all_amentities(self):
        return self.driver.find_elements_by_xpath('//div[contains(@class,"_vzrbjl")]')

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_current_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])


class customWaits(selectHotel_page_elements):
    def wait_till_element_displays(self, element):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, element)))

    def wait_till_element_visible(self, element):
        return self.wait.until(EC.invisibility_of_element((By.XPATH, element)))

    def wait_till_element_clickable(self, element):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))


class selectHotel_page_actions(selectHotel_page_elements):
    def amentities_to_scroll(self):
        self.switch_to_current_tab()
        customWaits(self.driver).wait_till_element_displays('//div[contains(@class,"_xcsyj0")]')
        customWaits(self.driver).wait_till_element_clickable('//div[contains(@class,"_5kaapu")]')
        self.scroll_to_element(self.amentities_text())

    def click_on_show_amentities_button(self):
        try:
            self.show_amentities_button().click()
        except NoSuchElementException:
            traceback.print_exc()

    def get_all_amentities_values(self):
        data = []
        new_data = []
        amentities = self.get_all_amentities()
        for i in amentities:
            data.append(i.text)
        for i in data:
            for res in i.split('\n'):
                new_data.append(res)
        return new_data
