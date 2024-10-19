# operations/read.py
import logging

from utils.transformers import DataTransformer
from utils.validators import CheckValidator


# Class: All operations of read
class ReadOperations:
    def __init__(self, 
                 customer_manager, 
                 product_manager, 
                 order_manager, 
                 erp_data
                 ):
        self.customer_manager = customer_manager
        self.product_manager = product_manager
        self.order_manager = order_manager
        self.erp_data = erp_data
        self.transformer = DataTransformer()
        self.validator = CheckValidator()

        # Access data structures
        self.col_widths = erp_data.col_widths
        self.employee_data_with_constraints = erp_data.employee_data_with_constraints
        self.victoria_tax_table = erp_data.victoria_tax_table
        self.payslip_table = erp_data.payslip_table

    # Display:: data in an aligned table format
    def display_table(self, data, headers, col_widths):
        header_line = "|".join([
            self.transformer.pad_string(
                header, col_widths.get(header, 10)
            ) for header in headers
        ])
        print(header_line)
        print('-' * len(header_line))
        for row in data:
            row_line = "|".join([
                self.transformer.pad_string(
                    str(row.get(header, '')), col_widths.get(header, 10)
                ) for header in headers
            ])
            print(row_line)

    """ For the IP System """

    # Display: Helper function to display detailed payroll information by employee payroll mapping
    def display_payslip_details(self, payslip):
        formatted_info = (f"EmployeeID: {payslip['EmployeeID']} "
                          f"Department: {payslip['Department']} "
                          f"Title: {payslip['Title']}")
        print(f"\nPayslip Details:")
        print(formatted_info)
        print(f"Tax: {payslip['Tax (AUD)']}")
        print(f"Superannuation: {payslip['Superannuation (AUD)']}")
        print(f"Net Yearly Salary (AUD): {payslip['Net Salary (AUD)']}")
        print(f"Converted Net Yearly Salary: {payslip['Converted Net Yearly Salary']}")

    # Read: employee who has the highest salary
    def get_highest_salary_employee(self):
        highest_salary_employee = max(
            self.employee_data_with_constraints, key=lambda emp: emp["Base Yearly Salary"]
        )
        print(f"Employee with the highest salary: {highest_salary_employee['Full Name']}"
              f"- ${highest_salary_employee['Base Yearly Salary']}")

    # Read: employee who has the lowest salary
    def get_lowest_salary_employee(self):
        lowest_salary_employee = min(
            self.employee_data_with_constraints, key=lambda emp: emp["Base Yearly Salary"]
        )
        print(f"Employee with the lowest salary: {lowest_salary_employee['Full Name']}"
              f" - ${lowest_salary_employee['Base Yearly Salary']}")

    # Read: employee's salary
    def get_employee_salary(self, employee):
        return employee["Base Yearly Salary"]

    # Read: employee information with some findings
    def view_employee_info(self):
        # Update headers to add "No."
        new_headers = ["No.", "EmployeeID", "Full Name", "Department", "Title", "Country"]

        # Update temp col_widths to add "No."
        col_widths_emp_data = self.col_widths['employee_data_with_constraints'].copy()
        col_widths_emp_data["No."] = 5

        # Update table_data to add "No." column
        table_data = [
            {
                "No.": str(index + 1),
                "EmployeeID": str(each_employee["EmployeeID"]),
                "Full Name": each_employee["Full Name"],
                "Department": each_employee["Department"],
                "Title": each_employee["Title"],
                "Country": each_employee["Country"]
            }
            for index, each_employee in enumerate(self.employee_data_with_constraints)
        ]

        # Display new table
        self.display_table(table_data, new_headers, col_widths_emp_data)

    # Read: Tax Table Data in Victoria, Australia
    def view_victoria_tax_table(self):
        table_headers = ["Income Range Min", "Income Range Max", "Tax Rate (%)"]
        table_data = [
            {
                "Income Range Min": str(each_bracket[0]),
                "Income Range Max": str(each_bracket[1]),
                "Tax Rate (%)": str(each_bracket[2])
            }
            for each_bracket in sorted(self.victoria_tax_table)
        ]
        col_widths_tax = self.col_widths['victoria_tax_table']
        self.display_table(table_data, table_headers, col_widths_tax)

    # Read: AUD currency conversion table data
    def view_currency_conversion_table(self):
        table_headers = ["Country", "Curr Code", "Rate to AUD"]
        table_data = [
            {
                "Country": each_currency["Country"],
                "Curr Code": each_currency["Curr Code"],
                "Rate to AUD": str(each_currency["Rate to AUD"])
            }
            for each_currency in self.erp_data.currency_conversion_table
        ]
        col_widths_currency = self.col_widths['currency_conversion_table']
        self.display_table(table_data, table_headers, col_widths_currency)

    # Read: all payslips and ask the id for details
    def view_all_payslips(self):
        table_headers = ["ID", "EmployeeID", "Full Name", "Department", "Title"]
        table_data = [
            {
                "ID": str(each_payslip["ID"]),
                "EmployeeID": str(each_payslip["EmployeeID"]),
                "Full Name": each_payslip["Full Name"],
                "Department": each_payslip["Department"],
                "Title": each_payslip["Title"]
            }
            for each_payslip in reversed(self.payslip_table)  # Display the latest payslip first
        ]
        col_widths_payslip = self.col_widths['payslip_table']

        self.display_table(table_data, table_headers, col_widths_payslip)

        # Ask the user to enter the payslip ID to view details
        input_payslip_id = input("Enter the ID of the payslip to view details (or press Enter to skip): ")
        if input_payslip_id == "":
            return None
        elif self.validator.is_numeric(input_payslip_id):
            payslip_id = int(input_payslip_id)
            for payslip in self.payslip_table:
                if payslip["ID"] == payslip_id:
                    self.display_payslip_details(payslip)
                    return payslip  # Return the selected payslip

            logging.error("Payslip ID not found.")
            return None
        else:
            logging.error("Invalid input. Please enter a numeric ID.")
            return None

    """ For the CMSystem """

    # Read: Products table for more details
    def display_product_table(self):
        products = self.product_manager.get_all_products()
        if not products:
            logging.error("No products available.")
            return

        # Customize the Header
        col_widths = self.erp_data.col_widths['products'].copy()
        col_widths_with_no = {
            'No.': 4,
            'pid': col_widths['product_id'],
            'product_name': col_widths['product_name'],
            'price': col_widths['price'],
            'category': col_widths['category'],
            'qty': col_widths['stock_quantity'],
            'created_at': col_widths['created_at'],
            'updated_at': col_widths['updated_at']
        }
        headers = self.erp_data.custom_headers['products']

        data = [
            {
                'No.': str(i),
                'pid': p.product_id,
                'product_name': p.product_name,
                'price': str(p.price),
                'category': p.category,
                'qty': str(p.stock_quantity),
                'created_at': self.transformer.to_std_datetimeformat(p.created_at),
                'updated_at': self.transformer.to_std_datetimeformat(p.updated_at)
            }
            for i, p in enumerate(products, start=1)
        ]

        self.display_table(data, headers, col_widths_with_no)

        while True:
            usr_chs = input("\nEnter product number to view details, or 'b' to go back: ").strip().lower()
            if usr_chs == 'b':
                break
            if self.validator.is_numeric(usr_chs) and 1 <= int(usr_chs) <= len(products):
                self.display_product_details(products[int(usr_chs) - 1])
            else:
                logging.error("Invalid choice. Please try again.")

    # Read: Product's details
    def display_product_details(self, product):
        print(f"""
Product Details for {product.product_name}:
Product ID: {product.product_id}
Name: {product.product_name}
Price: {product.price}
Category: {product.category}
Quantity (qty): {product.stock_quantity}
Created Date: {self.transformer.to_std_datetimeformat(product.created_at)}
Updated Date: {self.transformer.to_std_datetimeformat(product.updated_at)}""")

    # Read: Customers for more details
    def display_customers(self):
        customers = self.customer_manager.get_all_customers()
        if not customers:
            logging.error("No customers available.")
            return None

        self.display_customer_table(customers)

        while True:
            usr_chs = input("\nEnter customer number to view details, or 'b' to go back: ").strip()
            if usr_chs.lower() == 'b':
                break
            elif self.validator.is_numeric(usr_chs):
                idx = int(usr_chs) - 1
                if 0 <= idx < len(customers):
                    selected_customer = customers[idx]
                    return selected_customer
                else:
                    logging.error("Invalid customer number. Please try again.")
            else:
                logging.error("Invalid choice. Please try again.")
        return None

    # Read: Customers table by custom
    def display_customer_table(self, customers):
        col_widths = self.erp_data.col_widths['customers'].copy()
        if 'postcode' in col_widths:
            col_widths['pc'] = col_widths.pop('postcode')

        headers = self.erp_data.custom_headers['customers']

        col_widths_with_no = {'No.': 4}
        col_widths_with_no.update(col_widths)

        data = [
            {
                'No.': str(i),
                'first_name': a_cus.first_name,
                'last_name': a_cus.last_name,
                'dob': a_cus.dob,
                'email': a_cus.email,
                'phone': a_cus.phone,
                'country': a_cus.country,
                'city': a_cus.city,
                'pc': a_cus.postcode,
                'created_at': self.transformer.to_std_datetimeformat(a_cus.created_at),
                'updated_at': self.transformer.to_std_datetimeformat(a_cus.updated_at)
            }
            for i, a_cus in enumerate(customers, start=1)
        ]

        self.display_table(data, headers, col_widths_with_no)

    # Read: Customers by more details
    def display_customer_details(self, customer):
        while True:
            print(f"""
Customer Details:
{customer.first_name} {customer.last_name}
Email: {customer.email}
Date of Birth: {customer.dob}
Phone: {customer.phone}
Country: {customer.country}
City: {customer.city}
Postcode: {customer.postcode}
Created Date: {self.transformer.to_std_datetimeformat(customer.created_at)}
Updated Date: {self.transformer.to_std_datetimeformat(customer.updated_at)}""")

            print("\nOptions:")
            print("1. Update Customer")
            print("2. Delete Customer")
            print("b. Go Back")
            usr_chs = input("Enter your choice: ").strip().lower()
            if usr_chs == '1':
                return 'update', customer
            elif usr_chs == '2':
                return 'delete', customer
            elif usr_chs == 'b':
                return None, None  # Return when the user goes back
            else:
                logging.error("Invalid choice. Please try again.")

    # Read: chart by selection
    def display_charts(self):
        while True:
            print(f"""
            Reports Menu:
            1. Top-Selling Products
            2. Customer Location Distribution
            3. Customer Age Distribution
            b. Go Back\n""")

            usr_chs = input("Enter your choice: ")
            if usr_chs == '1':
                return 'top_selling_products'
            elif usr_chs == '2':
                return 'customer_location_distribution'
            elif usr_chs == '3':
                return 'customer_age_distribution'
            elif usr_chs == 'b':
                break
            else:
                logging.error("Invalid choice. Please try again.")
        return None

    # Read: Orders for more details
    def display_orders(self):
        orders = self.order_manager.get_all_orders()
        if not orders:
            logging.error("No orders available.")
            return
        for i, a_order in enumerate(orders, start=1):
            print(f"{i}. Order ID: {a_order.order_id}, "
                  f"Customer Email: {a_order.customer_email}, Total Price: {a_order.total_price}")

        while True:
            usr_chs = input("\nEnter order number to view details, or 'b' to go back: ").strip().lower()
            if usr_chs == 'b':
                break
            if self.validator.is_numeric(usr_chs) and 1 <= int(usr_chs) <= len(orders):
                self.display_order_details(orders[int(usr_chs) - 1])
            else:
                logging.error("Invalid choice. Please try again.")

    # Read : Order's details
    def display_order_details(self, order):
        print(f"""
Order Details for Order ID: {order.order_id}
Order Date: {order.order_date}
Customer Email: {order.customer_email}
Order Status: {order.order_status}
Payment Method: {order.payment_method}
Total Price: {order.total_price}
Created Date: {self.transformer.to_std_datetimeformat(order.created_at)}
Updated Date: {self.transformer.to_std_datetimeformat(order.updated_at)}""")
        print("\nOrdered Products:")
        for op in order.order_products:
            print(f"- Product ID: {op.product_id}, "
                  f"Name: {op.product_name}, Quantity: {op.quantity}, "
                  f"Price per Unit: {op.price_per_unit}, Total Price: {op.total_price}")
