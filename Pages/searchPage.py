from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from otherMethods import splitText


class search_page_elements:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def search_welcome_header(self):
        return self.driver.find_element_by_tag_name('h1')

    def more_filters_button(self):
        return self.driver.find_element_by_xpath("//button[contains(., 'More filters')]")

    def add_bedroom_button(self):
        return self.driver.find_element_by_xpath('//*[@id="filterItem-stepper-min_bedrooms-0"]/button[2]/span')

    def show_results_button(self):
        return self.driver.find_element_by_xpath("//button[@class='_m095vcq']")

    def first_record(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"_ttw0d")]')

    def map_pin_point(self):
        return self.driver.find_element_by_xpath("//div[contains(@style,"
                                                 "'background-color: rgb(34, 34, 34)')]")

    def cross_button_map(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"_1xt4bgs4")]')

    def get_room_type_from_list(self):
        return self.driver.find_elements_by_xpath('//div[contains(@class,"_167qordg")]')[0].text

    def hotel_name_list(self):
        return self.driver.find_elements_by_xpath('//div[contains(@class,"_1c2n35az")]')[0].text

    def hotel_price_from_list(self):
        return self.driver.find_elements_by_xpath('//div[contains(@class,"_1fwiw8gv")]')[0].text

    def hotel_price_in_map(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"_mvzr1f2")]').text

    def hotel_name_from_map(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"_v96gnbz")]').text

    def get_room_type_from_map(self):
        text = self.driver.find_element_by_css_selector('ol._194e2vt2').text
        formatting_text = splitText.format_text(text, 0)
        formatting_city = splitText.format_text(text, 1)
        hotel_type = [formatting_text, formatting_city]
        return hotel_type


class customWaits(search_page_elements):
    def wait_till_element_displays(self, element):
        return self.wait.until(ec.presence_of_element_located((By.XPATH, element)))

    def wait_till_element_visible(self, element):
        return self.wait.until(ec.invisibility_of_element((By.XPATH, element)))

    def wait_till_element_clickable(self, element):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, element)))


class search_page_actions(search_page_elements):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_method = None

    def entered_searched_values(self):
        customWaits(self.driver).wait_till_element_displays('//button[contains(@class, "_15yckkgv")]')
        data = []
        results = self.driver.find_elements_by_xpath('//button[contains(@class, "_15yckkgv")]')
        for res in results:
            data.append(res.text)
        return data

    def get_all_number_guests_results(self):
        customWaits(self.driver).wait_till_element_clickable('//div[contains(@class,"_kqh46o")]')
        data = []
        results = self.driver.find_elements_by_css_selector("div[style='margin-top: 9px;']")
        for res in results:
            data.append(res.text)
        guest_numbers = []
        for num in data:
            guest_numbers.append(num[:2])
        guest_numbers = [int(i) for i in guest_numbers]
        return guest_numbers

    def get_entered_location_from_portal(self):
        return self.entered_searched_values()[0]

    def get_entered_date_from_portal(self):
        return self.entered_searched_values()[1]

    def get_guests_from_portal(self):
        value = self.entered_searched_values()[2]
        new_value = value.replace("\n", "\t")
        return new_value[7:]

    def click_on_more_filters(self):
        self.more_filters_button().click()

    def click_on_number_of_bedrooms(self, number_of_times):
        customWaits(self.driver).wait_till_element_displays('//*[@id="filterItem-stepper-min_bedrooms-0"]'
                                                            '/button[2]/span')
        customWaits(self.driver).wait_till_element_clickable('//*[@id="filterItem-stepper-min_bedrooms-0"]'
                                                             '/button[2]/span')
        for i in range(number_of_times):
            self.add_bedroom_button().click()

    def click_on_show_records(self):
        self.show_results_button().click()

    def get_all_bedroom_results(self):
        customWaits(self.driver).wait_till_element_displays('//div[contains(@class,"_kqh46o")]')
        data = []
        results = self.driver.find_elements_by_css_selector("div[style='margin-top: 9px;']")
        for res in results:
            data.append(res.text)
        get_bedrooms_info = []
        for i in data:
            for ele in i.split(' · '):
                if 'bedrooms' in ele:
                    get_bedrooms_info.append(ele[:2])
        get_bedrooms_info = [int(i) for i in get_bedrooms_info]
        return get_bedrooms_info

    def click_on_first_record(self):
        customWaits(self.driver).wait_till_element_clickable('//div[contains(@class,"_ttw0d")]')
        ActionChains(self.driver).move_to_element(self.first_record()) \
            .click(self.first_record()).perform()

    def move_to_first_record(self):
        customWaits(self.driver).wait_till_element_displays('//div[contains(@class,"_kqh46o")]')
        customWaits(self.driver).wait_till_element_clickable('//div[contains(@class,"_ttw0d")]')
        ActionChains(self.driver).move_to_element(self.first_record()).perform()

    def map_pin_appeared(self):
        customWaits(self.driver).wait_till_element_displays("//div[contains(@style,"
                                                            "'background-color: rgb(255, 255, 255)')]")
        return self.map_pin_point().is_displayed()

    def click_on_selected_location_pin(self):
        self.map_pin_point().click()
