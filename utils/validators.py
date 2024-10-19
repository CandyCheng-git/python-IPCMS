# utils/validators.py

import re
from datetime import datetime
import logging


# Class:: Group all validation functions
class CheckValidator:

    # Check: is an integer number
    @staticmethod
    def is_numeric(value):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        try:
            int(value)
            return True
        except (ValueError, TypeError) as e:
            logging.error(f"'{value}' is not a valid number. - {str(e)}")
            return False

    # Check: is float/decimal number
    @staticmethod
    def is_decimal(value):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        try:
            float(value)
            return True
        except (ValueError, TypeError) as e:
            logging.error(f"'{value}' is not a valid decimal. - {str(e)}")
            return False

    # Check: is only alphabetic characters
    @staticmethod
    def is_alpha(value):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        if not value.isalpha():
            logging.error(f"'{value}' contains non-alphabetic characters.")
            return False
        return True

    # Check: is a valid date of birth in YYYY-MM-DD format
    @staticmethod
    def is_valid_date_of_birth(value):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        try:
            birth_date = datetime.strptime(value, '%Y-%m-%d')
            current_year = datetime.now().year
            if 1900 <= birth_date.year <= current_year:
                return True
            else:
                logging.error(f"Year '{birth_date.year}' is out of valid range.")
                return False
        except ValueError as e:
            logging.error(f"'{value}' is not a valid date of birth. - {str(e)}")
            return False

    # Check: s a valid datetime in YYYY-MM-DD HH:MM:SS format
    @staticmethod
    def is_datetime(value):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        try:
            datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError as e:
            logging.error(f"'{value}' is not a valid datetime. - {str(e)}")
            return False

    # Check: is a valid Australian phone number (e.g. '0000-000-000')
    @staticmethod
    def is_phone_num(value):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        pattern = r'^0\d{3}-\d{3}-\d{3}$'
        if re.match(pattern, value):
            return True
        logging.error(f"'{value}' is not a valid Australian phone number. "
                      f"Suggest format: 0000-000-000")
        return False

    # Check: is a valid email address
    @staticmethod
    def is_email(value):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, value):
            return True
        logging.error(f"'{value}' is not a valid email address. "
                      f"Suggest format: user@example.com")
        return False

    # Check: is in the list of served countries
    def is_served_country(self, value, served_countries):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        if self.is_alpha(value) and value in served_countries:
            return True
        logging.error(f"'{value}' is not in the served countries.")
        return False

    # Check: is a valid postcode for the given country
    def is_postcode(self, country_name, value, served_countries):
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        pattern = served_countries.get(country_name, {}).get("Postcode Format")
        if pattern and re.match(pattern, value):
            return True
        logging.error(f"'{value}' is not a valid postcode for {country_name}.")
        return False

    # Check: is employee's department in HR
    def is_hr_department(self, employee):
        return employee["Department"] == "HR"
