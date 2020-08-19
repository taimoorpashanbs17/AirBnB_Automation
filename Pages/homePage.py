import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from otherMethods import getDates


class home_page_elements:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_page(self, url):
        self.driver.get(url)

    def search_field(self):
        field = self.driver.find_element_by_id('bigsearch-query-detached-query')
        return field

    def checkin_datepicker_calender(self):
        return self.driver.find_element_by_xpath('//div[contains(@class, "_wtz1co")]')

    def get_value_date(self, date):
        value = self.driver.find_element_by_xpath('//div[contains(@data-testid, "datepicker-day-{}")]'.
                                                  format(date))
        return value

    def guest_button(self):
        button = self.driver.find_element_by_xpath('//div[contains(@class, "_uh2dzp")]')
        return button

    def add_guest_button(self):
        button = self.driver.find_element_by_xpath('//*[@id="stepper-adults"]/button[2]/span')
        return button

    def add_child_button(self):
        button = self.driver.find_element_by_xpath('//*[@id="stepper-children"]/button[2]/span')
        return button

    def search_button(self):
        return self.driver.find_element_by_xpath("//button[contains(., 'Search')]")

    def get_checkIn_date(self):
        dates = []
        field = self.driver.find_elements_by_xpath('//div[contains(@class, "_vuaqekp")]')
        for d in field:
            dates.append(d.text)
        return dates

    def get_Location_name(self):
        field = self.driver.find_element_by_id('bigsearch-query-detached-query')
        return field.get_attribute('value')


class customWaits(home_page_elements):
    def wait_till_element_clickable(self, element):
        return self.wait.until(EC.element_to_be_clickable((By.ID, element)))

    def wait_till_element_clickable_xpath(self, element):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))


class home_page_actions(home_page_elements):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_method = None

    def enter_on_search_field(self, value):
        customWaits(self.driver).wait_till_element_clickable("bigsearch-query-detached-query")
        self.search_field().click()
        self.search_field().send_keys(value)

    def click_on_calender(self):
        customWaits(self.driver).wait_till_element_clickable_xpath(
                    '//div[contains(@class, "_wtz1co")]')
        self.checkin_datepicker_calender().click()

    def enter_date(self, date):
        customWaits(self.driver).wait_till_element_clickable_xpath('//div[contains(@data-testid, "datepicker-day-{}")]'.
                                                                   format(getDates.get_current_date()))
        self.get_value_date(date).click()

    def click_on_guest_button(self):
        self.guest_button().click()

    def add_number_of_guest(self, number_of_guests):
        for i in range(number_of_guests):
            self.add_guest_button().click()

    def add_number_of_child(self, number_of_children):
        for i in range(number_of_children):
            self.add_child_button().click()

    def click_at_search_button(self):
        self.search_button().click()
