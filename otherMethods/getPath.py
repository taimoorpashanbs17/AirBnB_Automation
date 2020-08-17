import os
import platform


class getPath:
    @classmethod
    def get_driver(cls):
        os_name = platform.system()
        current_path = os.getcwd()
        parent_directory = os.path.dirname(current_path)
        if os_name == "Windows":
            selected_driver = os.path.abspath(parent_directory +
                                              "//Resources//Drivers//ChromeDriver//chromedriver_windows.exe")
            return selected_driver

    @classmethod
    def get_config(cls):
        os_name = platform.system()
        current_path = os.getcwd()
        parent_directory = os.path.dirname(current_path)
        if os_name == "Windows":
            path = os.path.abspath(parent_directory + "//Resources//data.ini")
            return path
