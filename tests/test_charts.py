import unittest
from unittest.mock import patch, MagicMock
from charts.charts import ChartGenerator
import logging


class TestChartGenerator(unittest.TestCase):

    def setUp(self):
        # Create mock objects for customer_manager and order_manager
        self.mock_customer_manager = MagicMock()
        self.mock_order_manager = MagicMock()

        # Instantiate the ChartGenerator with mock managers
        self.chart_generator = ChartGenerator(self.mock_customer_manager, self.mock_order_manager)

    @patch('matplotlib.pyplot.show')
    def test_gen_bar_chart_top_selling_products(self, mock_show):
        """Test the generation of the top-selling products chart."""
        # Mock the get_all_orders method to return sample orders
        self.mock_order_manager.get_all_orders.return_value = [
            MagicMock(order_products=[{'product_name': 'Product1', 'quantity': 2}]),
            MagicMock(order_products=[{'product_name': 'Product2', 'quantity': 5}]),
            MagicMock(order_products=[{'product_name': 'Product1', 'quantity': 1}])
        ]

        # Call the chart generation method
        self.chart_generator.gen_bar_chart_top_selling_products()

        # Verify that the chart is displayed (mocking plt.show)
        mock_show.assert_called()

    @patch('matplotlib.pyplot.show')
    def test_gen_customer_location_distribution_chart(self, mock_show):
        """Test the generation of the customer location distribution chart."""
        # Mock the get_all_customers method to return sample customers
        self.mock_customer_manager.get_all_customers.return_value = [
            MagicMock(city='New York'),
            MagicMock(city='New York'),
            MagicMock(city='Los Angeles')
        ]

        # Call the chart generation method
        self.chart_generator.gen_customer_location_distribution_chart()

        # Verify that the chart is displayed
        mock_show.assert_called()

    @patch('matplotlib.pyplot.show')
    def test_gen_customer_age_distribution_chart(self, mock_show):
        """Test the generation of the customer age distribution chart."""
        # Mock the get_all_customers method with customers having valid date of births
        self.mock_customer_manager.get_all_customers.return_value = [
            MagicMock(dob='1990-01-01'),
            MagicMock(dob='1985-06-15'),
            MagicMock(dob='2000-12-25')
        ]

        # Call the chart generation method
        self.chart_generator.gen_customer_age_distribution_chart()

        # Verify that the chart is displayed
        mock_show.assert_called()

    @patch('matplotlib.pyplot.Figure.savefig')
    @patch('matplotlib.pyplot.show')
    def test_export_all_charts(self, mock_show, mock_savefig):
        """Test the export of all charts."""
        # Mock the get_all_customers and get_all_orders methods to provide sample data
        self.mock_order_manager.get_all_orders.return_value = [
            MagicMock(order_products=[{'product_name': 'Product1', 'quantity': 2}])
        ]
        self.mock_customer_manager.get_all_customers.return_value = [
            MagicMock(dob='1990-01-01', city='New York')
        ]

        # Call the export function
        self.chart_generator.export_all_charts()

        # Verify that charts were saved and not displayed
        mock_savefig.assert_called()
        mock_show.assert_not_called()

    @patch('matplotlib.pyplot.close')
    def test_save_chart(self, mock_close):
        """Test the chart saving functionality."""
        # Mock figure object with its savefig method
        mock_fig = MagicMock()
        mock_fig.savefig = MagicMock()

        # Call save_chart
        self.chart_generator.save_chart(mock_fig, "Test Chart")

        # Verify that the chart was saved with the correct filename
        mock_fig.savefig.assert_called_with("test_chart.png")

        # Verify that plt.close() was called
        mock_close.assert_called_with(mock_fig)


if __name__ == '__main__':
    unittest.main()
