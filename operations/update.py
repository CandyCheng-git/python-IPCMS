# operations/update.py
import logging

from utils.validators import CheckValidator
from datetime import datetime


# Class: All operations of update
class UpdateOperations:
    def __init__(self, customer_manager, erp_data):
        self.customer_manager = customer_manager
        self.erp_data = erp_data
        self.validator = CheckValidator()
        self.currency_conversion_table = erp_data.currency_conversion_table

    """ For the IP System """
    # Update: currency conversion table
    def update_currency_conversion_table(self):
        curr_code = input("Enter Currency Code to update (or press Enter to skip): ").upper()
        if curr_code == "":  # Allow the user to skip then return
            return

        # Ensure the currency code contains is only in alphabetic characters
        if not self.validator.is_alpha(curr_code):
            logging.error("Invalid Currency Code. It should contain only alphabetic characters.")
            return

        # Find the currency by loop
        curr_found = False
        for each_data in self.currency_conversion_table:
            if each_data["Curr Code"] == curr_code:
                curr_found = True
                new_rate = None
                while True:
                    user_input = input("Enter new rate (leave blank to keep current): ")
                    if user_input == "":  # Allow the user to keep the current by leaving it blank
                        break
                    # Ensure the input is a valid decimal number
                    if self.validator.is_decimal(user_input):
                        new_rate = float(user_input)
                        break
                    else:
                        logging.error("Invalid input. Please enter a valid decimal number.")

                if new_rate is not None:
                    each_data["Rate to AUD"] = new_rate
                    logging.info(f"Updated {curr_code} to {new_rate}")
                else:
                    logging.error(f"No changes made to {curr_code}")
                break

        if not curr_found:
            logging.error("Currency Code not found.")

    """ CMS """

    # Update: Customer details
    def update_customer(self, customer):
        print("\nUpdate Customer")
        # Check Input one by one
        n_first_name = input(
            f"Enter new first name (current: {customer.first_name}): "
        ).strip()
        if n_first_name:
            if not self.validator.is_alpha(n_first_name):
                logging.error("Invalid first name. Update cancelled.")
                return
            customer.first_name = n_first_name
        n_last_name = input(
            f"Enter new last name (current: {customer.last_name}): "
        ).strip()
        if n_last_name:
            if not self.validator.is_alpha(n_last_name):
                logging.error("Invalid last name. Update cancelled.")
                return
            customer.last_name = n_last_name
        n_dob = input(
            f"Enter new date of birth (YYYY-MM-DD) (current: {customer.dob}): "
        ).strip()
        if n_dob:
            if not self.validator.is_valid_date_of_birth(n_dob):
                logging.error("Invalid date of birth. Update cancelled.")
                return
            customer.dob = n_dob
        n_phone = input(
            f"Enter new phone number (current: {customer.phone}): "
        ).strip()
        if n_phone:
            if not self.validator.is_phone_num(n_phone):
                logging.error("Invalid phone number. Update cancelled.")
                return
            customer.phone = n_phone
        n_country = input(
            f"Enter new country (current: {customer.country}): "
        ).strip()
        if n_country:
            if not self.validator.is_served_country(
                    n_country, self.erp_data.full_served_countries
            ):
                logging.error("Invalid country name. Update cancelled.")
                return
            customer.country = n_country

        n_city = input(f"Enter new city (current: {customer.city}): ").strip()
        if n_city:
            if not self.validator.is_alpha(n_city):
                logging.error("Invalid city name. Update cancelled.")
                return
            customer.city = n_city
        n_postcode = input(
            f"Enter new postcode (current: {customer.postcode}): "
        ).strip()
        if n_postcode:
            if not self.validator.is_postcode(
                    n_country, n_postcode, self.erp_data.full_served_countries
            ):
                logging.error("Invalid postcode. Update cancelled.")
                return
            customer.postcode = n_postcode
        # Update the updated_at as current
        customer.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info("Customer updated successfully.")

    # Update: Run update_customer b4 checking by Email
    def update_customer_by_email(self):
        input_email = input("Enter the email of the customer to update: ").strip()
        the_customer = self.customer_manager.get_customer_by_email(input_email)
        if not the_customer:
            logging.error("Customer not found.")
            return
        self.update_customer(the_customer)
