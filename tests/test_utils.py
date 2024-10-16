import unittest
from unittest.mock import patch
from utils.utils import get_cur_location, welcome_message, get_sales_quantity
import os
from io import StringIO


class TestUtils(unittest.TestCase):

    def test_get_cur_location(self):
        """Test the get_cur_location function."""
        expected_location = os.getcwd()
        result = get_cur_location()
        self.assertEqual(result, expected_location)

    @patch('sys.stdout', new_callable=StringIO)
    def test_welcome_message(self, mock_stdout):
        """Test the welcome_message function."""
        welcome_message()
        expected_output = 'Welcome to the Integrated Payroll and Customer Management System (IPCMS) !'
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_get_sales_quantity(self):
        """Test the get_sales_quantity function."""
        # Test with a tuple
        item_tuple = ('Product A', 10)
        result = get_sales_quantity(item_tuple)
        self.assertEqual(result, 10)

        # Test with a list
        item_list = ['Product B', 5]
        result = get_sales_quantity(item_list)
        self.assertEqual(result, 5)

        # Test with invalid input (missing quantity)
        with self.assertRaises(IndexError):
            get_sales_quantity(['Product C'])  # Missing quantity


if __name__ == '__main__':
    unittest.main()
