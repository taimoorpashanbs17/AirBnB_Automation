import os
import platform


class getPath:
    @classmethod
    def get_driver(cls):
        os_name = platform.system()
        current_path = os.getcwd()
        selected_driver = None
        parent_directory = os.path.dirname(current_path)
        if os_name == "Windows":
            selected_driver = os.path.abspath(parent_directory +
                                              "//AirBnB_Automation//Resources//Drivers//ChromeDriver//chromedriver_windows.exe")
        elif os_name == "Linux":
            selected_driver = os.path.abspath(parent_directory +
                                              "/AirBnB_Automation/Resources/Drivers/ChromeDriver/chromedriver_linux")
        return selected_driver

    @classmethod
    def get_config(cls):
        os_name = platform.system()
        current_path = os.getcwd()
        parent_directory = os.path.dirname(current_path)
        if os_name == "Windows":
            path = os.path.abspath(parent_directory + "//AirBnB_Automation//Resources//data.ini")
            return path
        elif os_name == "Linux":
            path = os.path.abspath(parent_directory + "/AirBnB_Automation/Resources/data.ini")
            return path
