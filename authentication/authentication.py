# authentication/authentication.py

import logging
from utils.transformers import DataTransformer
from utils.validators import CheckValidator


# Class:: Generate and manage login authentication.
class AuthenticationService:

    def __init__(self, employee_login_dict, employee_data_with_constraints):
        self.employee_login_dict = employee_login_dict
        self.employee_data_with_constraints = employee_data_with_constraints
        self.transformer = DataTransformer()
        self.validator = CheckValidator()

    # Function to handle the login process
    def login_system(self):
        max_attempts = 3
        attempts_left = max_attempts

        while attempts_left > 0:
            username = self.transformer.clean_input(input("\nEnter your Username: "))
            password = input("Enter your Password: ")
            employee_id = self.find_employee_id(username)

            if employee_id is not None and self.employee_login_dict[employee_id]["Password"] == password:
                access_level = self.get_access_level(employee_id)
                if access_level == 'Admin':
                    logging.info("Login successful! You have Admin access.")
                    return True
                else:
                    logging.info("Login successful, but you do not have Admin access.")
                    return False
            else:
                attempts_left -= 1
                logging.error(f"Invalid Username or Password. You have {attempts_left} attempt(s) remaining.")

        logging.error("Maximum login attempts exceeded.")
        return False

    # Function to get the access level by the employee id
    def get_access_level(self, employee_id):
        for each_employee in self.employee_data_with_constraints:
            if each_employee["EmployeeID"] == employee_id:
                return each_employee["System Access Level"]

    # Function to find the Employee ID by username - .items()
    def find_employee_id(self, username):
        for emp_id, emp_data in self.employee_login_dict.items():
            if emp_data["Login Name"] == username:
                return emp_id
        return None
