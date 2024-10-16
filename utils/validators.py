# utils/validators.py

import re
from datetime import datetime
import logging


class CheckValidator:
    """Group all validation functions."""

    @staticmethod
    def is_numeric(value):
        """Check if the input is an integer."""
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        try:
            int(value)
            return True
        except (ValueError, TypeError) as e:
            logging.error(f"'{value}' is not a valid number. - {str(e)}")
            return False

    @staticmethod
    def is_decimal(value):
        """Check if the input is a float/decimal number."""
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        try:
            float(value)
            return True
        except (ValueError, TypeError) as e:
            logging.error(f"'{value}' is not a valid decimal. - {str(e)}")
            return False

    @staticmethod
    def is_alpha(value):
        """Check if the input contains only alphabetic characters."""
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        if not value.isalpha():
            logging.error(f"'{value}' contains non-alphabetic characters.")
            return False
        return True

    @staticmethod
    def is_valid_date_of_birth(value):
        """Check if the input is a valid date of birth in YYYY-MM-DD format."""
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

    @staticmethod
    def is_datetime(value):
        """Check if the input is a valid datetime in YYYY-MM-DD HH:MM:SS format."""
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        try:
            datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError as e:
            logging.error(f"'{value}' is not a valid datetime. - {str(e)}")
            return False

    @staticmethod
    def is_phone_num(value):
        """Check if the input is a valid Australian phone number (e.g. '0000-000-000')."""
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        pattern = r'^0\d{3}-\d{3}-\d{3}$'
        if re.match(pattern, value):
            return True
        logging.error(f"'{value}' is not a valid Australian phone number. Suggest format: 0000-000-000")
        return False

    @staticmethod
    def is_email(value):
        """Check if the input is a valid email address."""
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, value):
            return True
        logging.error(f"'{value}' is not a valid email address. Suggest format: user@example.com")
        return False

    def is_served_country(self, value, served_countries):
        """Check if the input is in the list of served countries."""
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        if self.is_alpha(value) and value in served_countries:
            return True
        logging.error(f"'{value}' is not in the served countries.")
        return False

    def is_postcode(self, country_name, value, served_countries):
        """Check if the input is a valid postcode for the given country."""
        if value is None or value == '':
            logging.error("Input cannot be empty.")
            return False
        pattern = served_countries.get(country_name, {}).get("Postcode Format")
        if pattern and re.match(pattern, value):
            return True
        logging.error(f"'{value}' is not a valid postcode for {country_name}.")
        return False
