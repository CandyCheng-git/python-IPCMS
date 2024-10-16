import unittest
from unittest.mock import MagicMock, patch
from controllers.controllers import CustomerController, ProductController, OrderController
from models.models import Customer, Product, Order


class TestCustomerController(unittest.TestCase):

    def setUp(self):
        self.mock_order_manager = MagicMock()
        self.customer_controller = CustomerController(self.mock_order_manager)

    def test_create_customer(self):
        self.customer_controller.create_customer(
            'John', 'Doe', '1990-01-01', 'john.doe@example.com', '1234567890',
            'USA', 'New York', '10001', '2023-01-01', '2023-01-01'
        )
        customer = self.customer_controller.get_customer_by_email('john.doe@example.com')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.first_name, 'John')

    def test_update_customer(self):
        self.customer_controller.create_customer(
            'John', 'Doe', '1990-01-01', 'john.doe@example.com', '1234567890',
            'USA', 'New York', '10001', '2023-01-01', '2023-01-01'
        )
        self.customer_controller.create_customer(
            'John', 'Doe', '1990-01-01', 'john.doe@example.com', '0987654321',
            'USA', 'New York', '10001', '2023-01-01', '2023-01-01'
        )
        customer = self.customer_controller.get_customer_by_email('john.doe@example.com')
        self.assertEqual(customer.phone, '0987654321')

    @patch('builtins.input', side_effect=['y'])
    def test_delete_customer(self, mock_input):
        self.customer_controller.create_customer(
            'John', 'Doe', '1990-01-01', 'john.doe@example.com', '1234567890',
            'USA', 'New York', '10001', '2023-01-01', '2023-01-01'
        )
        self.customer_controller.delete_customer('john.doe@example.com')
        customer = self.customer_controller.get_customer_by_email('john.doe@example.com')
        self.assertIsNone(customer)


class TestProductController(unittest.TestCase):

    def setUp(self):
        self.product_controller = ProductController()

    def test_create_product(self):
        self.product_controller.create_product(
            '1', 'Laptop', 1000, 'Electronics', 10, '2023-01-01', '2023-01-01'
        )
        product = self.product_controller.get_product_by_id('1')
        self.assertIsNotNone(product)
        self.assertEqual(product.product_name, 'Laptop')

    def test_update_product(self):
        self.product_controller.create_product(
            '1', 'Laptop', 1000, 'Electronics', 10, '2023-01-01', '2023-01-01'
        )
        self.product_controller.create_product(
            '1', 'Laptop Pro', 1200, 'Electronics', 15, '2023-01-01', '2023-01-01'
        )
        product = self.product_controller.get_product_by_id('1')
        self.assertEqual(product.product_name, 'Laptop Pro')
        self.assertEqual(product.price, 1200)

    def test_get_all_products(self):
        self.product_controller.create_product(
            '1', 'Laptop', 1000, 'Electronics', 10, '2023-01-01', '2023-01-01'
        )
        self.product_controller.create_product(
            '2', 'Phone', 500, 'Electronics', 20, '2023-01-01', '2023-01-01'
        )
        products = self.product_controller.get_all_products()
        self.assertEqual(len(products), 2)


class TestOrderController(unittest.TestCase):

    def setUp(self):
        self.mock_product_manager = MagicMock()
        self.order_controller = OrderController(self.mock_product_manager)

    def test_create_order(self):
        self.mock_product_manager.get_product_by_id.return_value = MagicMock()
        # Ensure total_price is a float, not a list
        self.order_controller.create_order(
            '1', '01-01-2023', 1500.0,  # total_price is a float
            [{'product_id': '1', 'quantity': 1, 'price_per_unit': 1500.0}],  # order_products has price_per_unit
            'Credit Card', 'Pending',
            '2023-01-01 00:00:00', '2023-01-01 00:00:00',
            'john.doe@example.com'
        )
        order = self.order_controller.get_order_by_id('1')
        self.assertIsNotNone(order)
        self.assertEqual(order.order_id, '1')

    def test_update_order(self):
        self.mock_product_manager.get_product_by_id.return_value = MagicMock()
        self.order_controller.create_order(
            '1', '01-01-2023', 1500.0,
            [{'product_id': '1', 'quantity': 1, 'price_per_unit': 1500.0}],
            'Credit Card', 'Pending',
            '2023-01-01 00:00:00', '2023-01-01 00:00:00',
            'john.doe@example.com'
        )
        # When updating the order, make sure `total_price` is a float, and `order_products` has valid fields
        updated_order = Order(
            '1', '01-01-2023', 'Completed',
            1600.0,  # Corrected float value for total_price
            [{'product_id': '1', 'quantity': 1, 'price_per_unit': 1600.0}],  # Corrected order_products
            'Credit Card', '2023-01-01 00:00:00', '2023-01-01 00:00:00', 'john.doe@example.com'
        )
        self.order_controller.update_order_by_id(updated_order)
        order = self.order_controller.get_order_by_id('1')
        self.assertEqual(order.order_status, 'Completed')

    def test_delete_orders_by_customer_email(self):
        self.mock_product_manager.get_product_by_id.return_value = MagicMock()
        self.order_controller.create_order(
            '1', '01-01-2023', 1500.0,
            [{'product_id': '1', 'quantity': 1, 'price_per_unit': 1500.0}],
            'Credit Card', 'Pending',
            '2023-01-01 00:00:00', '2023-01-01 00:00:00',
            'john.doe@example.com'
        )
        self.order_controller.delete_orders_by_customer_email('john.doe@example.com')
        order = self.order_controller.get_order_by_id('1')
        self.assertIsNone(order)


if __name__ == '__main__':
    unittest.main()
