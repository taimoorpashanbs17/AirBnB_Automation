import unittest
from Pages.homePage import home_page_actions as home_page
from Pages.searchPage import search_page_actions as search_action
from environmentalSetup import environmental_Setup
from otherMethods import getDates
from Pages.selectHotelPage import selectHotel_page_actions
from Pages.searchPage import search_page_elements as search_elements
from otherMethods import name_verification


class search_results(environmental_Setup):

    def test_results_match_criteria(self):
        home_page(self.driver).get_page("https://www.airbnb.com/")
        home_page(self.driver).enter_on_search_field("Rome, Italy")
        home_page(self.driver).click_on_calender()
        home_page(self.driver).enter_date(getDates.get_current_date())
        home_page(self.driver).enter_date(getDates.get_end_date())
        home_page(self.driver).click_on_guest_button()
        checkIn_out_date = home_page(self.driver).get_checkIn_date()
        checkIn_date = checkIn_out_date[0]
        checkOut_date = checkIn_out_date[1][-2:]
        date_entered = checkIn_date + " - " + checkOut_date
        home_page(self.driver).add_number_of_guest()
        home_page(self.driver).click_at_search_button()
        search_action(self.driver).entered_searched_values()
        self.assertTrue("Rome" in search_action(self.driver).get_entered_location_from_portal(),
                        "Location name is not Correct")
        self.assertTrue(date_entered in search_action(self.driver).get_entered_date_from_portal(),
                        "Date is not Correct")
        self.assertTrue(str(3) in search_action(self.driver).get_guests_from_portal(),
                        "Number of Guests is correct")
        self.assertTrue(all(x >= 3 for x in search_action(self.driver).get_all_number_guests_results()),
                        "List is Showing Results for less than 3 Guests")

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
        selectHotel_page_actions(self.driver).amentities_to_scroll()
        selectHotel_page_actions(self.driver).click_on_show_amentities_button()
        self.assertTrue("Pool" in selectHotel_page_actions(self.driver).get_all_amentities_values(),
                        "Pool is not displaying Under that Property.")

    def test_verify_property_displaying_on_map(self):
        home_page(self.driver).get_page("https://www.airbnb.com/")
        home_page(self.driver).enter_on_search_field("Rome, Italy")
        home_page(self.driver).click_on_calender()
        home_page(self.driver).enter_date(getDates.get_current_date())
        home_page(self.driver).enter_date(getDates.get_end_date())
        home_page(self.driver).click_on_guest_button()
        home_page(self.driver).add_number_of_guest()
        home_page(self.driver).click_at_search_button()
        search_action(self.driver).move_to_first_record()
        self.assertTrue(search_action(self.driver).map_pin_appeared(),
                        "Map is not Displaying Pin point")
        search_action(self.driver).click_on_selected_location_pin()
        hotel_type_from_map = search_elements(self.driver).get_room_type_from_map()
        hotel_type_from_list = search_elements(self.driver).get_room_type_from_list()
        self.assertTrue(name_verification.hotel_name_verification
                        (hotel_type_from_map, hotel_type_from_list),
                        "Hotel Types are different showing on both Map and List")
        hotel_name_from_map = search_elements(self.driver).hotel_name_from_map()
        hotel_name_from_list = search_elements(self.driver).hotel_name_list()
        self.assertEqual(hotel_name_from_list, hotel_name_from_map,
                         "Names are different showing on both map and List")
        hotel_price_in_list = search_elements(self.driver).hotel_price_from_list()
        hotel_price_in_map = search_elements(self.driver).hotel_price_in_map()
        self.assertEqual(hotel_price_in_list, hotel_price_in_map,
                         "Prices displaying are same on both map and list")


if __name__ == "__main__":
    unittest.main()
