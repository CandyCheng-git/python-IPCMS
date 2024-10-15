
# IPCMS (Integrated Product and Customer Management System)

## Overview
**IPCMS** is an Integrated Product and Customer Management System designed to streamline business operations involving customer management, product management, and order handling. It includes various modules for customer data processing, product management, sales reporting, and data visualization. The system is built in Python, leveraging several custom modules and libraries.

## Features
- **Customer Management**: Add, update, delete, and view customer information.
- **Product Management**: Manage product catalog, including stock levels and pricing.
- **Order Processing**: Process and track customer orders, calculate totals, and generate order insights.
- **Data Visualization**: Generate charts for product performance, customer demographics, and order statistics.
- **Reports**: Automatically generate detailed marketing reports with sales KPIs, product performance, and customer insights.
- **Data Import/Export**: Import and export customer, product, and order data in CSV and JSON formats.

## Project Structure

```bash
IPCMS
│  customers.csv               # Customer data (CSV)
│  customer_age_distribution.png # Customer age distribution chart
│  customer_location_distribution.png # Customer location distribution chart
│  ipcms_main.py               # Main application script
│  main.py                     # Core application logic
│  marketing_report_20241015141837.docx # Sample marketing report
│  orders.json                 # Order data (JSON)
│  products.csv                # Product data (CSV)
│  top-selling_products.png    # Top-selling products chart
├─authentication               # Handles user authentication
├─charts                       # Chart generation logic
├─controllers                  # Controllers for managing main operations
├─data                         # Data handling and manipulation
├─models                       # Data models for the system
├─operations                   # Modules for CRUD operations
├─reports                      # Report generation logic
├─tests                        # Unit tests for each module
├─utils                        # Utility functions including transformers and validators
└─__pycache__
```

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CandyCheng-git/python-IPCMS.git
   cd ipcms
   ```

2. **Install dependencies**:
   This project uses Python 3. Make sure you have the required libraries installed. You can install them using the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   To run the application, execute the `main.py` file:
   ```bash
   python main.py
   ```

## Modules

- **Authentication** (`authentication/authentication.py`): Handles user login and session management.
- **Charts** (`charts/charts.py`): Generates visual representations of customer and product data.
- **Controllers** (`controllers/controllers.py`): Centralizes logic for managing customer, product, and order operations.
- **Data** (`data/data.py`): Handles data extraction and transformations.
- **Reports** (`reports/reports.py`): Generates automated reports with detailed sales and customer insights.
- **CRUD Operations** (`operations/`): Modules for Create, Read, Update, Delete (CRUD) functionalities for products, customers, and orders.
- **Utilities** (`utils/`): Utility functions for data transformation and validation.

## Tests
The project includes unit tests to validate functionality across modules. Tests are located in the `tests/` folder and can be run using a Python test framework (e.g., `pytest`).

To run all tests:
```bash
pytest
```

## Example Usage
Upon running the application, you can perform the following operations:
- View, add, update, and delete customer records.
- Manage products and view product performance metrics.
- Process orders and generate reports with insights into customer demographics, sales KPIs, and stock levels.
- Export reports in Word format and visualize data in charts.

## Sample Report
A sample marketing report (`marketing_report_20241015141837.docx`) is included in the root directory of the project. It contains KPIs, product performance, order insights, and charts illustrating sales data.
