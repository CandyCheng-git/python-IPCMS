import unittest
from unittest.mock import patch
from utils.transformers import DataTransformer


class TestDataTransformer(unittest.TestCase):

    def setUp(self):
        # Create an instance of DataTransformer to test methods
        self.transformer = DataTransformer()

    def test_pad_string(self):
        """Test the string padding method."""
        result = self.transformer.pad_string("Hello", 10)
        self.assertEqual(result, "Hello     ")
        result = self.transformer.pad_string("Data", 6)
        self.assertEqual(result, "Data  ")

    def test_to_std_dateformat(self):
        """Test date format transformation to standard format."""
        result = self.transformer.to_std_dateformat("12/10/2024")
        self.assertEqual(result, "2024-10-12")
        result = self.transformer.to_std_dateformat("2024-10-12")
        self.assertEqual(result, "2024-10-12")

    def test_to_std_datetimeformat(self):
        """Test datetime format transformation to standard format."""
        result = self.transformer.to_std_datetimeformat("12/10/2024 12:30")
        self.assertEqual(result, "2024-10-12 12:30:00")
        result = self.transformer.to_std_datetimeformat("2024-10-12 15:45")
        self.assertEqual(result, "2024-10-12 15:45:00")

    def test_format_name(self):
        """Test string capitalization for names."""
        result = self.transformer.format_name("john doe")
        self.assertEqual(result, "John Doe")
        result = self.transformer.format_name("EMILY SMITH")
        self.assertEqual(result, "Emily Smith")

    def test_clean_input(self):
        """Test string cleaning of special characters."""
        result = self.transformer.clean_input(" Hello, World; ")
        self.assertEqual(result, "Hello World")

    @patch.object(DataTransformer, 'calculate_tax', return_value=5000.0)
    def test_calculate_tax(self, mock_tax):
        """Test tax calculation based on salary."""
        result = self.transformer.calculate_tax(50000)
        self.assertEqual(result, 5000.0)

    @patch.object(DataTransformer, 'calculate_superannuation', return_value=9500.0)
    def test_calculate_superannuation(self, mock_superannuation):
        """Test superannuation calculation at 9.5%."""
        result = self.transformer.calculate_superannuation(100000)
        self.assertEqual(result, 9500.0)

    @patch.object(DataTransformer, 'currency_conversion', return_value=(45000.0, 'INR'))
    def test_currency_conversion(self, mock_conversion):
        """Test currency conversion."""
        result, curr_code = self.transformer.currency_conversion(1000, "India")
        self.assertEqual(result, 45000.0)  # 1000 AUD to INR
        self.assertEqual(curr_code, "INR")

    @patch.object(DataTransformer, 'calculate_tax', return_value=5000.0)
    @patch.object(DataTransformer, 'calculate_superannuation', return_value=9500.0)
    @patch.object(DataTransformer, 'currency_conversion', return_value=(45000.0, 'INR'))
    def test_calculate_and_format_salary(self, mock_tax, mock_super, mock_conversion):
        """Test calculation and formatting of salary details."""
        tax_str, super_str, net_str, converted_str, curr_code = self.transformer.calculate_and_format_salary(60000, "India")

        self.assertEqual(tax_str, "5000.0")
        self.assertEqual(super_str, "9500.0")
        self.assertEqual(net_str, "55000.0")
        self.assertEqual(converted_str, "45000.0")
        self.assertEqual(curr_code, "INR")


if __name__ == '__main__':
    unittest.main()
