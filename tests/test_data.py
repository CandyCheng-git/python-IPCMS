import unittest
from data.data import EnterpriseData, IPCMSData


class TestEnterpriseData(unittest.TestCase):

    def setUp(self):
        self.ipcms_data = IPCMSData()
        self.enterprise_data = EnterpriseData(self.ipcms_data)

    def test_load_customers(self):
        """Test loading of customers into the system."""
        self.assertEqual(len(self.enterprise_data.customers), 20)  # Should have 20 customers
        customer = self.enterprise_data.customers[0]
        self.assertEqual(customer.first_name, "Matthew")
        self.assertEqual(customer.email, "johnsmith@gmail.com")

    def test_load_products(self):
        """Test loading of products into the system."""
        self.assertEqual(len(self.enterprise_data.products), 8)  # Should have 8 products
        product = self.enterprise_data.products[0]
        self.assertEqual(product.product_name, "EMO Robot (Lite)")
        self.assertEqual(float(product.price), 311.98)

    def test_load_orders(self):
        """Test loading of orders into the system."""
        self.assertEqual(len(self.enterprise_data.orders), 30)  # Should have 30 orders
        order = self.enterprise_data.orders[0]
        self.assertEqual(order.order_id, "PO0001")
        self.assertEqual(order.total_price, 2043.50)
        self.assertEqual(len(order.order_products), 2)

    def test_get_required_fields(self):
        """Test the retrieval of required fields for customers, products, and orders."""
        customer_fields = self.enterprise_data.get_required_fields('customers')
        self.assertIn('first_name', customer_fields)
        self.assertIn('email', customer_fields)

        product_fields = self.enterprise_data.get_required_fields('products')
        self.assertIn('product_name', product_fields)
        self.assertIn('price', product_fields)

        order_fields = self.enterprise_data.get_required_fields('orders')
        self.assertIn('order_id', order_fields)
        self.assertIn('total_price', order_fields)

    def test_col_widths(self):
        """Test that column widths are initialized correctly."""
        self.assertIn('first_name', self.enterprise_data.col_widths['customers'])
        self.assertIn('product_name', self.enterprise_data.col_widths['products'])
        self.assertIn('order_id', self.enterprise_data.col_widths['orders'])

    def test_customer_data(self):
        """Test customer data consistency."""
        customer_data = EnterpriseData.customer_data()
        self.assertEqual(len(customer_data), 20)
        self.assertEqual(customer_data[0]['first_name'], 'Matthew')

    def test_product_data(self):
        """Test product data consistency."""
        product_data = EnterpriseData.products_data()
        self.assertEqual(len(product_data), 8)
        self.assertEqual(product_data[0]['product_name'], 'EMO Robot (Lite)')

    def test_order_data(self):
        """Test order data consistency."""
        order_data = EnterpriseData.orders_data()
        self.assertEqual(len(order_data), 30)
        self.assertEqual(order_data[0]['order_id'], 'PO0001')
        self.assertEqual(order_data[0]['total_price'], '2043.50')


if __name__ == '__main__':
    unittest.main()
