import unittest
from unittest.mock import patch
from models.models import Customer, Product, OrderedProduct, Order
from utils.validators import CheckValidator


class TestModels(unittest.TestCase):

    def test_customer_creation(self):
        """Test creation of a Customer object."""
        customer = Customer(
            first_name='John',
            last_name='Doe',
            dob='1990-01-01',
            email='john.doe@example.com',
            phone='1234-567-890',
            country='Australia',
            city='Sydney',
            postcode='2001',
            created_at='2023-01-01 00:00:00',
            updated_at='2023-01-02 00:00:00'
        )
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.email, 'john.doe@example.com')
        self.assertEqual(customer.postcode, '2001')

    @patch.object(CheckValidator, 'is_numeric', return_value=True)
    def test_product_creation(self, mock_is_numeric):
        """Test creation of a Product object."""
        product = Product(
            product_id='001',
            product_name='Laptop',
            price='1500.99',
            category='Electronics',
            stock_quantity='10',
            created_at='2023-01-01 00:00:00',
            updated_at='2023-01-02 00:00:00'
        )
        self.assertEqual(product.product_id, '001')
        self.assertEqual(product.product_name, 'Laptop')
        self.assertEqual(product.price, 1500.99)
        self.assertEqual(product.stock_quantity, 10)
        mock_is_numeric.assert_called_with('10')

    def test_ordered_product_creation(self):
        """Test creation of an OrderedProduct object."""
        ordered_product = OrderedProduct(
            product_id='001',
            product_name='Laptop',
            quantity=2,
            price_per_unit=1500.99,
            total_price=3001.98
        )
        self.assertEqual(ordered_product.product_id, '001')
        self.assertEqual(ordered_product.product_name, 'Laptop')
        self.assertEqual(ordered_product.quantity, 2)
        self.assertEqual(ordered_product.price_per_unit, 1500.99)
        self.assertEqual(ordered_product.total_price, 3001.98)

    def test_order_creation(self):
        """Test creation of an Order object with OrderedProduct objects."""
        order_data = {
            "order_id": "PO0001",
            "order_date": "2023-01-01",
            "order_status": "Pending",
            "total_price": "3001.98",
            "order_products": [
                {
                    "product_id": "001",
                    "product_name": "Laptop",
                    "quantity": "2",
                    "price_per_unit": "1500.99",
                    "total_price": "3001.98",
                }
            ],
            "payment_method": "Credit Card",
            "created_at": "2023-01-01 00:00:00",
            "updated_at": "2023-01-02 00:00:00",
            "customer_email": "john.doe@example.com"
        }
        order = Order(**order_data)

        self.assertEqual(order.order_id, 'PO0001')
        self.assertEqual(order.total_price, 3001.98)
        self.assertEqual(len(order.order_products), 1)
        ordered_product = order.order_products[0]
        self.assertEqual(ordered_product.product_id, '001')
        self.assertEqual(ordered_product.product_name, 'Laptop')
        self.assertEqual(ordered_product.total_price, 3001.98)


if __name__ == '__main__':
    unittest.main()
