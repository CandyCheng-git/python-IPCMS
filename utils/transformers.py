# utils/transformers.py

from datetime import datetime
from data.data import IPCMSData
import logging


# Class:: Group all transform functions
class DataTransformer:
    def __init__(self):
        self.IPCMS_data = IPCMSData()

    # Transfer: Pad the string to match the target width
    @staticmethod
    def pad_string(input_string, target_width):
        input_string = str(input_string)
        return input_string.ljust(target_width)

    # Transfer: Convert different date formats to YYYY-MM-DD.
    @staticmethod
    def to_std_dateformat(date_str):
        formats = ('%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d', '%Y/%m/%d')
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
            except ValueError:
                continue
        logging.error(f"'{date_str}' is not in a valid date format.")
        return None

    # Transfer: Convert different datetime formats to YYYY-MM-DD HH:MM:SS
    @staticmethod
    def to_std_datetimeformat(datetime_str):
        formats = (
            '%d/%m/%Y %H:%M:%S', '%d-%m-%Y %H:%M:%S', '%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S',
            '%d/%m/%Y %H:%M', '%d-%m-%Y %H:%M', '%Y-%m-%d %H:%M', '%Y/%m/%d %H:%M'
        )
        for fmt in formats:
            try:
                return datetime.strptime(datetime_str, fmt).strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                continue
        logging.error(f"'{datetime_str}' is not in a valid datetime format.")
        return None

    # Transfer: Capitalize the first letter of each word.
    @staticmethod
    def format_name(string):
        return string.title()

    # Transfer: Clean up string input by removing unnecessary spaces or symbols.
    @staticmethod
    def clean_input(input_string):
        return input_string.replace(",", "").replace(";", "").strip()

    # Transfer: order date to %d-%m-%Y
    @staticmethod
    def transform_order_date(order):
        return datetime.strptime(order.order_date, '%d-%m-%Y')

    # Transfer: calculate tax by income
    def calculate_tax(self, salary):
        tax_amount = 0  # Initialize tax amount
        for each_bracket in self.IPCMS_data.victoria_tax_table:
            min_income, max_income, rate = each_bracket
            if salary > min_income:
                if max_income is None or salary <= max_income:
                    # Calculate tax on the portion of salary within the current bracket
                    tax_amount += (salary - min_income) * (rate / 100)
                    break
                else:
                    tax_amount += (max_income - min_income) * (rate / 100)
        return abs(round(tax_amount, 2))

    # Transfer: calculate superannuation at a standard rate 9.5%
    def calculate_superannuation(self, salary):
        return salary * 0.095

    # Transfer: convert salary by country
    def currency_conversion(self, salary, country):
        for each_data in self.IPCMS_data.currency_conversion_table:
            if each_data["Country"].lower() == country.lower():
                return salary * each_data["Rate to AUD"], each_data["Curr Code"]

    # Transfer: Helper function to calculate and format salary details
    def calculate_and_format_salary(self, gross_salary, country):
        tax = self.calculate_tax(gross_salary)
        net_salary = gross_salary - tax
        superannuation = self.calculate_superannuation(gross_salary)

        # Manual string formatting for 2 decimal places
        tax_str = str(round(tax, 2))
        superannuation_str = str(round(superannuation, 2))
        net_salary_str = str(round(net_salary, 2))

        converted_salary, currency_code = self.currency_conversion(net_salary, country)
        converted_salary_str = str(round(converted_salary, 2))

        return tax_str, superannuation_str, net_salary_str, converted_salary_str, currency_code
