import unittest
from utils.validators import CheckValidator
from unittest.mock import patch


class TestCheckValidator(unittest.TestCase):

    def setUp(self):
        self.validator = CheckValidator()

    def test_is_numeric_valid(self):
        self.assertTrue(self.validator.is_numeric('123'))
        self.assertTrue(self.validator.is_numeric(456))

    def test_is_numeric_invalid(self):
        self.assertFalse(self.validator.is_numeric('abc'))
        self.assertFalse(self.validator.is_numeric(None))
        self.assertFalse(self.validator.is_numeric(''))

    def test_is_decimal_valid(self):
        self.assertTrue(self.validator.is_decimal('123.45'))
        self.assertTrue(self.validator.is_decimal(678.90))

    def test_is_decimal_invalid(self):
        self.assertFalse(self.validator.is_decimal('abc'))
        self.assertFalse(self.validator.is_decimal(None))
        self.assertFalse(self.validator.is_decimal(''))

    def test_is_alpha_valid(self):
        self.assertTrue(self.validator.is_alpha('John'))
        self.assertTrue(self.validator.is_alpha('Doe'))

    def test_is_alpha_invalid(self):
        self.assertFalse(self.validator.is_alpha('John123'))
        self.assertFalse(self.validator.is_alpha(''))
        self.assertFalse(self.validator.is_alpha(None))

    def test_is_valid_date_of_birth_valid(self):
        self.assertTrue(self.validator.is_valid_date_of_birth('1990-01-01'))

    def test_is_valid_date_of_birth_invalid(self):
        self.assertFalse(self.validator.is_valid_date_of_birth('01-01-1990'))
        self.assertFalse(self.validator.is_valid_date_of_birth('invalid-date'))
        self.assertFalse(self.validator.is_valid_date_of_birth(None))

    def test_is_datetime_valid(self):
        self.assertTrue(self.validator.is_datetime('2023-01-01 12:00:00'))

    def test_is_datetime_invalid(self):
        self.assertFalse(self.validator.is_datetime('2023/01/01 12:00:00'))
        self.assertFalse(self.validator.is_datetime('invalid-date'))
        self.assertFalse(self.validator.is_datetime(None))

    def test_is_phone_num_valid(self):
        self.assertTrue(self.validator.is_phone_num('0414-123-456'))

    def test_is_phone_num_invalid(self):
        self.assertFalse(self.validator.is_phone_num('414-123-456'))
        self.assertFalse(self.validator.is_phone_num('0414123456'))
        self.assertFalse(self.validator.is_phone_num(None))

    def test_is_email_valid(self):
        self.assertTrue(self.validator.is_email('test@example.com'))

    def test_is_email_invalid(self):
        self.assertFalse(self.validator.is_email('test@.com'))
        self.assertFalse(self.validator.is_email('test@example'))
        self.assertFalse(self.validator.is_email(None))

    def test_is_served_country_valid(self):
        served_countries = ['Australia', 'China', 'India']
        self.assertTrue(self.validator.is_served_country('Australia', served_countries))

    def test_is_served_country_invalid(self):
        served_countries = ['Australia', 'China', 'India']
        self.assertFalse(self.validator.is_served_country('Germany', served_countries))
        self.assertFalse(self.validator.is_served_country(None, served_countries))

    def test_is_postcode_valid(self):
        served_countries = {
            'Australia': {'Postcode Format': r'^\d{4}$'},
            'China': {'Postcode Format': r'^\d{6}$'}
        }
        self.assertTrue(self.validator.is_postcode('Australia', '3000', served_countries))

    def test_is_postcode_invalid(self):
        served_countries = {
            'Australia': {'Postcode Format': r'^\d{4}$'},
            'China': {'Postcode Format': r'^\d{6}$'}
        }
        self.assertFalse(self.validator.is_postcode('Australia', '123', served_countries))
        self.assertFalse(self.validator.is_postcode('China', '12345', served_countries))
        self.assertFalse(self.validator.is_postcode('Australia', None, served_countries))


if __name__ == '__main__':
    unittest.main()
