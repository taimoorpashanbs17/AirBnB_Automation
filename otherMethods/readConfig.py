import configparser
from otherMethods.getPath import getPath


class read_Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(getPath().get_config())

    def get_city_name(self):
        return self.config['DEFAULT']['CITY_NAME']

    def base_url(self):
        return self.config['DEFAULT']['BASE_URL']

    def number_of_guests(self):
        return self.config['DEFAULT']['NUMBER_OF_GUESTS']

    def number_of_children(self):
        return self.config['DEFAULT']['NUMBER_OF_KIDS']

    def number_of_bedrooms(self):
        return self.config['DEFAULT']['BEDROOMS']

    def amentity_to_search(self):
        return self.config['DEFAULT']['AMENTITY_TO_SEARCH']
