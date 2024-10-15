# utils.py

import os

def get_cur_location():
    """Get the current working directory."""
    return os.getcwd()

def welcome_message():
    """Display a welcome message."""
    dirty_message = '\n,   Welcome to the Integrated Payroll and Customer Management System (IPCMS) !,,,'
    print(dirty_message.strip('\n, '))

# Function get_sales_quantity: Get sales quantity
def get_sales_quantity(item):
    return item[1]