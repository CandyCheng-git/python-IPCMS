# operations/create.py
import logging

from utils.validators import CheckValidator
from utils.transformers import DataTransformer
from operations.read import ReadOperations
from datetime import datetime


# Class:: All operations of create
class CreateOperations:
    def __init__(self,
                 customer_manager,
                 product_manager,
                 order_manager,
                 erp_data,
                 chart_generator):
        self.customer_manager = customer_manager
        self.product_manager = product_manager
        self.order_manager = order_manager
        self.erp_data = erp_data
        self.chart_generator = chart_generator
        self.read_ops = ReadOperations(
            self.customer_manager,
            self.product_manager,
            self.order_manager,
            self.erp_data
        )
        self.validator = CheckValidator()
        self.transformer = DataTransformer()
        self.employee_data_with_constraints = erp_data.employee_data_with_constraints
        self.payslip_table = erp_data.payslip_table
        self.victoria_tax_table = erp_data.victoria_tax_table
        self.currency_conversion_table = erp_data.currency_conversion_table

    """ For the CMSystem """

    # Create: Customer
    def create_new_customer(self):
        print("\nCreate a New Customer")
        email = input("Enter email: ").strip()

        # Check
        if not self.validator.is_email(email) or self.customer_manager.get_customer_by_email(email):
            logging.error("Invalid email or customer already exists.")
            return
        first_name = input("Enter first name: ")
        if not self.validator.is_alpha(first_name): return
        last_name = input("Enter last name: ")
        if not self.validator.is_alpha(last_name): return
        dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
        if not self.validator.is_valid_date_of_birth(dob): return
        phone = input("Enter phone number (0000-000-000): ").strip()
        if not self.validator.is_phone_num(phone): return
        country = input("Enter country: ").strip()
        if not self.validator.is_served_country(country, self.erp_data.full_served_countries): return
        city = input("Enter city: ")
        if not self.validator.is_alpha(city): return
        postcode = input("Enter postcode: ").strip()
        if not self.validator.is_postcode(country, postcode, self.erp_data.full_served_countries): return

        # Confirm
        logging.info(
            f"\nConfirm customer info:\nEmail: {email}\nFirst Name: {first_name}\nLast Name: {last_name}"
            f"\nDOB: {dob}\nPhone: {phone}\nCountry: {country}\nCity: {city}\nPostcode: {postcode}")
        if input("Is this information correct? (y/n): ").strip().lower() != 'y':
            logging.warning("Customer creation cancelled.")
            return

        created_at = updated_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Try Create
        try:
            self.customer_manager.create_customer(
                first_name, last_name, dob, email, phone, country, city, postcode,
                created_at, updated_at)
            logging.info("Customer created successfully.")
        except Exception as er_msg:
            logging.error("Error: creating customer:", str(er_msg))

    """  For the IP System"""

    # Create: payslip by employee id
    def create_payslip(self):
        input_employee_id = input("Enter Employee ID to create payslip (or press Enter to skip): ")
        if input_employee_id == "":  # Allow the user to skip then return
            return
        elif self.validator.is_numeric(input_employee_id):
            input_employee_id = int(input_employee_id)
            employee = None
            for each_employee in self.employee_data_with_constraints:
                if each_employee["EmployeeID"] == input_employee_id:
                    employee = each_employee
                    break

            if not employee:
                logging.error("Employee not found.")
                return

            payslip_id = id(employee)

            for payslip in self.payslip_table:
                if payslip["ID"] == payslip_id:
                    logging.warning("Duplicate ID found, replacing the old payslip with the new one.")
                    self.payslip_table.remove(payslip)
                    break

            base_yearly_salary = employee["Base Yearly Salary"]

            #  Calculate and prompt format salary details by using the helper function
            (tax_str, superannuation_str, net_salary_str,
             converted_salary_str, currency_code) \
                = self.transformer.calculate_and_format_salary(base_yearly_salary, employee["Country"])

            new_payslip = {
                "ID": payslip_id,
                "EmployeeID": input_employee_id,
                "Full Name": self.transformer.format_name(employee["Full Name"]),
                "Department": employee["Department"],
                "Title": employee["Title"],
                "Gross Salary (AUD)": base_yearly_salary,
                "Tax (AUD)": tax_str,
                "Net Salary (AUD)": net_salary_str,
                "Superannuation (AUD)": superannuation_str,
                "Converted Net Yearly Salary": f"{currency_code} {converted_salary_str}"
            }

            self.payslip_table.append(new_payslip)
            logging.info("Payslip created successfully.")
            self.read_ops.display_payslip_details(new_payslip)
        else:
            logging.error("Employee not found.")
            return
