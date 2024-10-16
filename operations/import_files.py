# import.py

import csv
import json
import logging
from utils.utils import get_cur_location
from utils.validators import CheckValidator
from utils.transformers import DataTransformer


class ImportOperations:
    def __init__(self, customer_manager, product_manager, order_manager, erp_data):
        self.customer_manager = customer_manager
        self.product_manager = product_manager
        self.order_manager = order_manager
        self.erp_data = erp_data
        self.check_valid_method = CheckValidator()
        self.transform_data_method = DataTransformer()

    # Import Function read_csv: Read the csv and save the data by inputted object_name name
    def read_csv(self, object_name):
        assume_filename = "".join([object_name + 's', '.csv'])
        try:
            with open(assume_filename, newline='') as csv_file:
                if object_name == 'customer':
                    correct_headers = self.erp_data.custom_headers[object_name + 's']
                    csv_reader = csv.DictReader(csv_file, fieldnames=correct_headers)
                    # Skips the heading - Using next() method
                    next(csv_file)
                    for row in csv_reader:
                        try:
                            # Check
                            first_name = row['first_name'].strip()
                            if not self.check_valid_method.is_alpha(first_name):
                                logging.error(f"Invalid first name '{first_name}'. Skipping this record.")
                                continue
                            last_name = row['last_name'].strip()
                            if not self.check_valid_method.is_alpha(last_name):
                                logging.error(f"Invalid last name '{last_name}'. Skipping this record.")
                                continue
                            dob = row['dob'].strip()
                            dob = self.transform_data_method.to_std_dateformat(dob)
                            if not self.check_valid_method.is_valid_date_of_birth(dob):
                                logging.error(f"Invalid date of birth '{dob}'. Skipping this record.")
                                continue
                            email = row['email'].strip()
                            if not self.check_valid_method.is_email(email):
                                logging.error(f"Invalid email '{email}'. Skipping this record.")
                                continue
                            phone = row['phone'].strip()
                            if not self.check_valid_method.is_phone_num(phone):
                                logging.error(f"Invalid phone number '{phone}'. Skipping this record.")
                                continue
                            country = row['country'].strip()
                            if not self.check_valid_method.is_served_country(
                                    country,
                                    self.erp_data.full_served_countries
                            ):
                                logging.error(f"Invalid country '{country}'. Skipping this record.")
                                continue
                            city = row['city'].strip()
                            if not self.check_valid_method.is_alpha(city):
                                logging.error(f"Invalid city '{city}'. Skipping this record.")
                                continue
                            postcode = row['pc'].strip()
                            if not self.check_valid_method.is_postcode(country, postcode,
                                                                       self.erp_data.full_served_countries):
                                logging.error(f"Invalid postcode '{postcode}'. Skipping this record.")
                                continue
                            created_at = row['created_at'].strip()
                            created_at = self.transform_data_method.to_std_datetimeformat(created_at)
                            if not self.check_valid_method.is_datetime(created_at):
                                logging.error(f"Invalid created datetime '{created_at}'. Skipping this record.")
                                continue
                            updated_at = row['updated_at'].strip()
                            updated_at = self.transform_data_method.to_std_datetimeformat(updated_at)
                            if not self.check_valid_method.is_datetime(updated_at):
                                logging.error(f"Invalid updated datetime '{updated_at}'. Skipping this record.")
                                continue
                            # Add or Edit
                            self.customer_manager.create_customer(
                                row['first_name'], row['last_name'], row['dob'], row['email'], row['phone'],
                                row['country'], row['city'], row['pc'], row['created_at'], row['updated_at']
                            )
                        except Exception as er_msg:
                            logging.error(f"Error: adding customer '{row['email']}' - {str(er_msg)}")

                elif object_name == 'product':
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        try:
                            # Check
                            product_id = row['pid'].strip()
                            if not product_id:
                                logging.error("Product ID is missing. Skipping this record.")
                                continue
                            product_name = row['product_name'].strip()
                            if not product_name:
                                logging.error(f"Product name is missing for ID '{product_id}'. Skipping this record.")
                                continue
                            price = row['price'].strip()
                            if not self.check_valid_method.is_decimal(price):
                                logging.error(f"Invalid price '{price}' for product '{product_name}'. Skipping this record.")
                                continue
                            price = float(price)
                            category = row['category'].strip()
                            if not category:
                                logging.error(f"Category is missing for product '{product_name}'. Skipping this record.")
                                continue
                            stock_quantity = row['qty'].strip()
                            if not self.check_valid_method.is_numeric(stock_quantity):
                                logging.error(
                                    f"Invalid stock quantity '{stock_quantity}' for product '{product_name}'. Skipping this record.")
                                continue
                            stock_quantity = int(stock_quantity)
                            created_at = row['created_at'].strip()
                            created_at = self.transform_data_method.to_std_datetimeformat(created_at)
                            if not self.check_valid_method.is_datetime(created_at):
                                logging.error(f"Invalid created datetime '{created_at}'. Skipping this record.")
                                continue
                            updated_at = row['updated_at'].strip()
                            updated_at = self.transform_data_method.to_std_datetimeformat(updated_at)
                            if not self.check_valid_method.is_datetime(updated_at):
                                logging.error(f"Invalid updated datetime '{updated_at}'. Skipping this record.")
                                continue
                            # Add
                            self.product_manager.create_product(
                                product_id, product_name, price, category, stock_quantity,
                                created_at, updated_at
                            )
                        except Exception as er_msg:
                            logging.error(f"Error: adding product '{product_name}' - {str(er_msg)}")

                file_loca_message = f'Location: "{get_cur_location()}\\{assume_filename}"'
                csv_file_message = f'CSV file "{assume_filename}" has been imported successfully.'
                logging.info("{} \n {}".format(file_loca_message, csv_file_message))
        except Exception as er_msg:
            logging.error(f"Error: importing {object_name} list - {str(er_msg)}")

    # Import Function read_json: Read the JSON and save the data by inputted object_name name
    def read_json(self, object_name):
        assume_filename = "".join([object_name + 's', '.json'])
        try:
            with open(assume_filename, 'r') as json_file:
                data = json.load(json_file)

                if object_name == 'order':
                    for order_data in data:
                        try:
                            # Check
                            for ordered_product in order_data['order_products']:
                                product = self.product_manager.get_product_by_id(ordered_product['product_id'])
                                if not product:
                                    logging.error(
                                        f"Product with ID {ordered_product['product_id']} "
                                        f"does not exist. Skipping this product.")
                                    continue
                                required_product_fields = ['product_id', 'product_name', 'quantity', 'price_per_unit',
                                                           'total_price']
                                for field in required_product_fields:
                                    if field not in ordered_product:
                                        if field == 'price_per_unit':
                                            ordered_product['price_per_unit'] = product.price
                                        elif field == 'total_price':
                                            ordered_product['total_price'] = ordered_product['quantity'] * \
                                                                             ordered_product[
                                                                                 'price_per_unit']
                                        else:
                                            logging.error(
                                                f"Error: Missing required field '{field}' in product "
                                                f"{ordered_product.get('product_name', '')}. Skipping this product.")
                                            continue

                            # Add or Edit
                            self.order_manager.create_order(
                                order_data['order_id'], order_data['order_date'], order_data['total_price'],
                                order_data['order_products'], order_data['payment_method'],
                                order_data['order_status'], order_data['created_at'],
                                order_data['updated_at'], order_data['customer_email']
                            )
                        except Exception as er_msg:
                            logging.error(f"Error: adding order '{order_data['order_id']}' - {str(er_msg)}")
            logging.info(f'JSON file "{assume_filename}" has been imported successfully.')
        except Exception as er_msg:
            logging.error(f"Error: importing {object_name} list - {str(er_msg)}")
