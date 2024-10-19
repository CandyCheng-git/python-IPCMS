# operations/delete.py

# Class:: All operations of delete
class DeleteOperations:
    def __init__(self, customer_manager, order_manager, erp_data):
        self.customer_manager = customer_manager
        self.order_manager = order_manager
        self.erp_data = erp_data

    # Delete: customer and their related orders.
    def delete_customer(self, customer):
        """TBC"""

    # Delete: payslip by ID.
    def delete_payslip_by_id(self):
        """TBC"""
