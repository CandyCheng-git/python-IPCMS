# delete.py

import logging


class DeleteOperations:
    def __init__(self, customer_manager, order_manager, erp_data):
        self.customer_manager = customer_manager
        self.order_manager = order_manager
        self.erp_data = erp_data

    def delete_customer(self, customer):
        """Delete a customer and their related orders."""
        # ... Rest of the function remains the same ...

    def delete_payslip_by_id(self):
        """Delete a payslip by ID."""
        # ... Implementation as shown earlier ...
