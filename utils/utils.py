# utils/utils.py

import os


# Function: Get the current working directory
def get_cur_location():
    return os.getcwd()


# Function: Display a welcome message
def welcome_message():
    dirty_message = '\n,   Welcome to the Integrated Payroll and Customer Management System (IPCMS) !,,,'
    print(dirty_message.strip('\n, '))


# Function: Get sales quantity
def get_sales_quantity(item):
    return item[1]
