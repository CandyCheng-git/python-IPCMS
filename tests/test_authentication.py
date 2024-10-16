import unittest
from unittest.mock import patch
from authentication.authentication import AuthenticationService  # Adjusted import path


class TestAuthenticationService(unittest.TestCase):

    def setUp(self):
        self.employee_login_dict = {
            '1': {'Login Name': 'admin_user', 'Password': 'admin_pass'},
            '2': {'Login Name': 'normal_user', 'Password': 'user_pass'}
        }

        self.employee_data_with_constraints = [
            {"EmployeeID": '1', "System Access Level": 'Admin'},
            {"EmployeeID": '2', "System Access Level": 'User'}
        ]

        # Mock DataTransformer and CheckValidator classes from utils.transformers and utils.validators
        with patch('utils.transformers.DataTransformer', autospec=True) as mock_transformer, \
                patch('utils.validators.CheckValidator', autospec=True) as mock_validator:
            self.mock_transformer = mock_transformer.return_value
            self.mock_validator = mock_validator.return_value
            self.mock_transformer.clean_input.return_value = 'admin_user'

            # Instantiate AuthenticationService with mocked dependencies
            self.auth_service = AuthenticationService(self.employee_login_dict, self.employee_data_with_constraints)

    @patch('builtins.input', side_effect=['admin_user', 'admin_pass'])
    @patch('logging.info')
    def test_successful_admin_login(self, mock_logging, mock_input):
        """Test that an admin user can log in successfully."""
        result = self.auth_service.login_system()
        self.assertTrue(result)
        mock_logging.assert_called_with("Login successful! You have Admin access.")

    @patch('builtins.input', side_effect=['normal_user', 'user_pass'])
    @patch('logging.info')
    def test_successful_user_login_without_admin_access(self, mock_logging, mock_input):
        """Test that a normal user can log in but does not have Admin access."""
        result = self.auth_service.login_system()
        self.assertFalse(result)
        mock_logging.assert_called_with("Login successful, but you do not have Admin access.")

    @patch('builtins.input', side_effect=[
        'invalid_user',
        'invalid_pass',
        'invalid_user',
        'invalid_pass',
        'invalid_user',
        'invalid_pass'
    ])
    @patch('logging.error')
    def test_failed_login_due_to_invalid_credentials(self, mock_logging, mock_input):
        """Test login failure due to invalid username and password."""
        result = self.auth_service.login_system()
        self.assertFalse(result)
        mock_logging.assert_called_with("Maximum login attempts exceeded.")

    @patch('builtins.input', side_effect=[
        'admin_user',
        'wrong_pass',
        'admin_user',
        'wrong_pass',
        'admin_user',
        'wrong_pass'
    ])
    @patch('logging.error')
    def test_failed_login_after_max_attempts(self, mock_logging, mock_input):
        """Test that login fails after maximum attempts with wrong credentials."""
        result = self.auth_service.login_system()
        self.assertFalse(result)
        mock_logging.assert_called_with("Maximum login attempts exceeded.")


if __name__ == '__main__':
    unittest.main()
