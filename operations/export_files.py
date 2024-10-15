# export.py

import csv
import json
import logging
from utils.utils import get_cur_location



class ExportOperations:
    def __init__(self, customer_manager, product_manager, order_manager, erp_data):
        self.customer_manager = customer_manager
        self.product_manager = product_manager
        self.order_manager = order_manager
        self.erp_data = erp_data

    # Export Function export_csv: Create a csv by data list, then export
    def export_csv(self, object_name):
        name_in_col_widths = object_name + 's'
        assume_filename = "".join([name_in_col_widths, '.csv'])
        try:
            headers = self.erp_data.custom_headers[object_name + 's']
            csv_data = []
            if object_name == 'customer':
                if "No." not in headers:
                    headers.insert(0, "No.")
                customers = self.customer_manager.get_all_customers()
                if not customers:
                    print(f"No customers found to export to {assume_filename}")
                    return
                csv_data = [
                    {
                        "No.": idx + 1,
                        "first_name": customer.first_name,
                        "last_name": customer.last_name,
                        "dob": customer.dob,
                        "email": customer.email,
                        "phone": customer.phone,
                        "country": customer.country,
                        "city": customer.city,
                        "pc": customer.postcode,
                        "created_at": customer.created_at,
                        "updated_at": customer.updated_at,
                    }
                    for idx, customer in enumerate(customers)
                ]
            elif object_name == 'product':
                products = self.product_manager.get_all_products()
                if not products:
                    print(f"No products found to export to {assume_filename}")
                    return
                csv_data = [
                    {
                        "pid": product.product_id,
                        "product_name": product.product_name,
                        "price": product.price,
                        "category": product.category,
                        "qty": product.stock_quantity,
                        "created_at": product.created_at,
                        "updated_at": product.updated_at,
                    }
                    for product in self.product_manager.get_all_products()
                ]
            # Write the data to the CSV file
            with open(assume_filename, 'w', newline='') as file:
                csv_writer = csv.DictWriter(file, fieldnames=headers)
                csv_writer.writeheader()
                csv_writer.writerows(csv_data)
                csv_file_message = f'CSV file "{assume_filename}" has been created successfully.'
                file_loca_message = f'Location: "{get_cur_location()}\\{assume_filename}"'
                print("{} \n {}".format(csv_file_message, file_loca_message))
        except Exception as er_msg:
            print(f"Error: exporting {object_name} list - {str(er_msg)}")

    # Export Function export_orders_json: Create a jason by Orders, then export
    def export_orders_json(self):
        set_filename = 'orders.json'
        try:
            orders_data = []
            orders = self.order_manager.get_all_orders()
            if not orders:
                print(f"No orders found to export to {set_filename}")
                return
            for order in orders:
                order_dict = vars(order)
                order_dict['order_products'] = [
                    vars(prd) for prd in order.order_products
                ]
                orders_data.append(order_dict)
            with open(set_filename, 'w') as json_file:
                json.dump(orders_data, json_file, indent=4)
            print(
                f'JSON file "{set_filename}" created successfully. \nLocation: "{get_cur_location()}\\{set_filename}"')
        except Exception as er_msg:
            print(f"Error: exporting orders: {er_msg}")
