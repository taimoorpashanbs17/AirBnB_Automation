import time
import unittest
from Pages.homePage import home_page_actions as home_page
from Pages.searchPage import search_page_actions as search_action
from environmentalSetup import environmental_Setup
from otherMethods import getDates


class search_results(environmental_Setup):

    # def test_results_match_criteria(self):
    #     home_page(self.driver).get_page("https://www.airbnb.com/")
    #     home_page(self.driver).enter_on_search_field("Rome, Italy")
    #     home_page(self.driver).click_on_calender()
    #     home_page(self.driver).enter_date(getDates.get_current_date())
    #     home_page(self.driver).enter_date(getDates.get_end_date())
    #     home_page(self.driver).click_on_guest_button()
    #     checkIn_out_date = home_page(self.driver).get_checkIn_date()
    #     checkIn_date = checkIn_out_date[0]
    #     checkOut_date = checkIn_out_date[1][-2:]
    #     date_entered = checkIn_date + " - " + checkOut_date
    #     home_page(self.driver).add_number_of_guest()
    #     home_page(self.driver).click_at_search_button()
    #     search_action(self.driver).entered_searched_values()
    #     self.assertTrue("Rome" in search_action(self.driver).get_entered_location_from_portal(),
    #                     "Location name is not Correct")
    #     self.assertTrue(date_entered in search_action(self.driver).get_entered_date_from_portal(),
    #                     "Date is not Correct")
    #     self.assertTrue(str(3) in search_action(self.driver).get_guests_from_portal(),
    #                     "Number of Guests is correct")
    #     self.assertTrue(all(x >= 3 for x in search_action(self.driver).get_all_number_guests_results()),
    #                     "List is Showing Results for less than 3 Guests")

    def test_results_details_match_filters(self):
        home_page(self.driver).get_page("https://www.airbnb.com/")
        home_page(self.driver).enter_on_search_field("Rome, Italy")
        home_page(self.driver).click_on_calender()
        home_page(self.driver).enter_date(getDates.get_current_date())
        home_page(self.driver).enter_date(getDates.get_end_date())
        home_page(self.driver).click_on_guest_button()
        home_page(self.driver).add_number_of_guest()
        home_page(self.driver).click_at_search_button()
        search_action(self.driver).entered_searched_values()
        search_action(self.driver).click_on_more_filters()
        search_action(self.driver).click_on_number_of_bedrooms(5)
        search_action(self.driver).click_on_show_records()
        self.assertTrue(all(x >= 5 for x in search_action(self.driver).get_all_bedroom_results()),
                        "List is Showing Results for less than 5 Guests")
        search_action(self.driver).click_on_first_record()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
