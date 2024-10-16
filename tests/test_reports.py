import unittest
from unittest.mock import MagicMock, patch
from reports.reports import ReportGenerator
import logging


class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        # Mock dependencies: customer_manager, product_manager, order_manager, and chart_generator
        self.customer_manager = MagicMock()
        self.product_manager = MagicMock()
        self.order_manager = MagicMock()
        self.chart_generator = MagicMock()

        # Create an instance of ReportGenerator with the mock managers
        self.report_generator = ReportGenerator(
            self.customer_manager,
            self.product_manager,
            self.order_manager,
            self.chart_generator
        )

        # Set logging level to ensure logs are captured
        logging.basicConfig(level=logging.INFO)

    @patch('utils.utils.get_cur_location', return_value='/fake/path')
    @patch('reports.reports.datetime')
    @patch('reports.reports.Document')
    def test_export_report(self, mock_document, mock_datetime, mock_get_cur_location):
        # Set up mock datetime for filename generation
        mock_datetime.now.return_value.strftime.return_value = '20241015123000'

        # Set up mock Document instance and its save method
        mock_document_instance = MagicMock()
        mock_document.return_value = mock_document_instance

        # Mock the method that generates the report content
        self.report_generator.create_report_content = MagicMock(return_value={
            'kpis': {
                'Total Sales': "$1,000.00",
                'Total Customers': 10,
                'Average Order Value': "$100.00",
                'Customer Retention Rate': "90.00%"
            },
            'product_performance': {
                'Best-Selling Product': 'Product A',
                'Low Stock Alert': ['Product B – 5 units'],
                'Product Table': [
                    {'Product Name': 'Product A', 'Units Sold': 10, 'Total Revenue': "$100.00"},
                    {'Product Name': 'Product B', 'Units Sold': 5, 'Total Revenue': "$50.00"},
                ]
            },
            'order_customer_insights': {
                'Recent Orders': [
                    {'Order ID': 'PO0001', 'Date': '2024-10-01', 'Total': "$100.00"}
                ],
                'Customer Demographics': [
                    {'City': 'Melbourne', 'Number of Customers': 5},
                    {'City': 'Sydney', 'Number of Customers': 3},
                ]
            },
            'charts': ['chart1.png', 'chart2.png']
        })

        # Call the method under test
        with self.assertLogs(level='INFO') as log:
            self.report_generator.export_report()

        # Verify that the expected log message contains the correct report creation message
        expected_log_message = 'Report "marketing_report_20241015123000.docx" created successfully.'
        self.assertIn(expected_log_message, log.output[0])

        # Verify the document object was created
        mock_document.assert_called_once()

        # Verify the document save method was called with the expected filename
        mock_document_instance.save.assert_called_once_with('marketing_report_20241015123000.docx')

        # Verify that the chart export was called
        self.chart_generator.export_all_charts.assert_called_once()


if __name__ == '__main__':
    unittest.main()
