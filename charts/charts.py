# charts.py

import matplotlib.pyplot as plt
import numpy as np
import os
import logging
from utils.utils import get_cur_location
from datetime import datetime
from matplotlib import pyplot as plt


class ChartGenerator:
    """Class to generate and manage charts."""

    def __init__(self, customer_manager, order_manager):
        self.customer_manager = customer_manager
        self.order_manager = order_manager

    def save_chart(self, fig, chart_title):
        """Save the chart with the given title."""
        filename = f"{chart_title.replace(' ', '_').lower()}.png"
        fig.savefig(filename)
        logging.info(f'Chart "{filename}" has been created successfully.')
        plt.close(fig)

    # Read Function display_charts: View a chart by selection
    def display_charts(self):
        while True:
            print(f"""
            Reports Menu:
            1. Top-Selling Products
            2. Customer Location Distribution
            3. Customer Age Distribution
            b. Go Back\n""")

            usr_chs = input("Enter your choice: ")
            if usr_chs == '1':
                self.gen_bar_chart_top_selling_products()
            elif usr_chs == '2':
                self.gen_customer_location_distribution_chart()
            elif usr_chs == '3':
                self.gen_customer_age_distribution_chart()
            elif usr_chs == 'b':
                break
            else:
                print("Invalid choice. Please try again.")

    def gen_chart(self, data, labels, chart_title, xlabel, ylabel, export=False):
        """Generate a bar chart."""
        fig, ax = plt.subplots()
        ax.bar(labels, data)
        ax.set_title(chart_title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        if export:
            self.save_chart(fig, chart_title)
        else:
            logging.info("Displaying chart. Please close the chart window to continue.")
            plt.show()
        return fig, ax

    def gen_bar_chart_top_selling_products(self, export=False):
        """Generate a bar chart of top-selling products."""
        product_sales = {}
        for order in self.order_manager.get_all_orders():
            for op in order.order_products:
                if isinstance(op, dict):
                    product_name = op['product_name']
                    quantity = int(op['quantity'])
                else:
                    product_name = op.product_name
                    quantity = int(op.quantity)
                product_sales[product_name] = product_sales.get(product_name, 0) + quantity

        if not product_sales:
            logging.info("No sales data available.")
            return

        data = list(product_sales.values())
        labels = list(product_sales.keys())
        self.gen_chart(
            data,
            labels,
            'Top-Selling Products',
            'Products',
            'Units Sold',
            export
        )

    def gen_customer_location_distribution_chart(self, export=False):
        """Generate a bar chart of customer location distribution."""
        city_counts = {}
        for customer in self.customer_manager.get_all_customers():
            city = customer.city
            city_counts[city] = city_counts.get(city, 0) + 1

        if not city_counts:
            logging.info("No customer location data available.")
            return

        data = list(city_counts.values())
        labels = list(city_counts.keys())
        self.gen_chart(
            data,
            labels,
            'Customer Location Distribution',
            'City',
            'Number of Customers',
            export
        )

    def gen_customer_age_distribution_chart(self, export=False):
        """Generate a histogram chart of customer age distribution."""
        customers = self.customer_manager.get_all_customers()
        if not customers:
            logging.info("No customer data available.")
            return

        ages = []
        for customer in customers:
            try:
                dob = datetime.strptime(customer.dob, '%Y-%m-%d')
                age = (datetime.now() - dob).days // 365
                ages.append(age)
            except ValueError:
                logging.warning(f"Invalid date of birth for customer {customer.email}. Skipping.")

        if not ages:
            logging.info("No valid date of birth data available.")
            return

        # Create bins/ranges of ages
        counts, bins = np.histogram(ages, bins=10)
        labels = [f"{int(bins[i])}-{int(bins[i + 1])}" for i in range(len(bins) - 1)]

        self.gen_chart(
            counts,
            labels,
            'Customer Age Distribution',
            'Age Range',
            'Number of Customers',
            export
        )

    # Export Function export_all_charts: Call all the gen chart functions as export
    def export_all_charts(self):
        print("\nExporting all charts as .png files...")
        self.gen_bar_chart_top_selling_products(export=True)
        self.gen_customer_location_distribution_chart(export=True)
        self.gen_customer_age_distribution_chart(export=True)
        file_loca_message = f'Location: "{get_cur_location()}\\"'
        print("All charts have been exported successfully.")
        print(file_loca_message)
