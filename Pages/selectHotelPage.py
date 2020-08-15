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

    def hotel_name(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"_xcsyj0")]')

    def amenities_text(self):
        return self.driver.find_element_by_xpath('//*[@id="site-content"]//div[5]/div[2]//div/section/h2')

    def show_amentities_button(self):
        return self.driver.find_element_by_xpath('//*[@id="site-content"]//div[5]/div[2]/div[3]/a')

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
        self.scroll_to_element(self.amenities_text())

    def click_on_show_amentities_button(self):
        self.show_amentities_button().click()

    def get_all_amentities_values(self):
        data = []
        new_data = []
        amentities = self.get_all_amentities()
        for i in amentities:
            data.append(i.text)
        for i in data:
            for ali in i.split('\n'):
                new_data.append(ali)
        return new_data
