import unittest
from selenium import webdriver
import datetime
from otherMethods.getDriver import getDriver


class environmental_Setup(unittest.TestCase):
    def setUp(self):
        print("Test Environment Started at " + str(datetime.datetime.now()))
        self.driver = webdriver.Chrome(executable_path=getDriver.get_driver())
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        if self.driver is not None:
            print("--------------------------------------")
            print("Test Environment is Destroyed")
            print("Run Completed at " + str(datetime.datetime.now()))
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
