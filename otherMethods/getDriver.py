import os
import platform


class getDriver:
    @classmethod
    def get_driver(cls):
        os_name = platform.system()
        current_path = os.getcwd()
        parent_directory = os.path.dirname(current_path)
        if os_name == "Windows":
            selected_driver = os.path.abspath(parent_directory +
                                              "//Resources//Drivers//ChromeDriver//chromedriver_windows.exe")
            return selected_driver
