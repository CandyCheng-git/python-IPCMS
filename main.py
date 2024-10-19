import logging
from utils.utils import get_cur_location, welcome_message
from authentication.authentication import AuthenticationService
from operations.create import CreateOperations
from operations.read import ReadOperations
from operations.update import UpdateOperations
from operations.delete import DeleteOperations
from operations.export_files import ExportOperations
from operations.import_files import ImportOperations
from charts.charts import ChartGenerator
from reports.reports import ReportGenerator
from data.data import EnterpriseData, IPCMSData
from controllers.controllers import CustomerController, ProductController, OrderController
from utils.validators import CheckValidator
from utils.transformers import DataTransformer

logging.basicConfig(level=logging.INFO, format='%(message)s')


# Class:: Main application class for the IPCMS system
class IPCMSApp:
    def __init__(self, for_test_mode=False):
        # Create utility instances
        self.check_valid_method = CheckValidator()
        self.transform_data_method = DataTransformer()

        # Initialize controllers/managers
        self.product_manager = ProductController()
        self.order_manager = OrderController(self.product_manager)
        self.customer_manager = CustomerController(self.order_manager)

        # Load the datasets into the controllers/managers
        self.IPCMS_data = IPCMSData()
        self.enterprise_data = EnterpriseData(self.IPCMS_data)

        # Adjust logging level to suppress messages during data loading
        logging.getLogger().setLevel(logging.CRITICAL)
        self.load_data()
        # Reset logging level back to INFO (or your desired level)
        logging.getLogger().setLevel(logging.INFO)

        # Access data structures
        self.col_widths = self.IPCMS_data.col_widths
        self.employee_login_dict = self.IPCMS_data.employee_login_dict
        self.currency_conversion_table = self.IPCMS_data.currency_conversion_table
        self.employee_data_with_constraints = self.IPCMS_data.employee_data_with_constraints
        self.victoria_tax_table = self.IPCMS_data.victoria_tax_table
        self.payslip_table = self.IPCMS_data.payslip_table
        self.auth_service = AuthenticationService(
            self.employee_login_dict,
            self.employee_data_with_constraints
        )

        # Initialize operation modules
        self.chart_generator = ChartGenerator(self.customer_manager, self.order_manager)

        self.delete_ops = DeleteOperations(self.customer_manager, self.order_manager, self.IPCMS_data)

        self.create_ops = CreateOperations(
            self.customer_manager,
            self.product_manager,
            self.order_manager,
            self.IPCMS_data,
            self.chart_generator
        )

        self.read_ops = ReadOperations(
            self.customer_manager,
            self.product_manager,
            self.order_manager,
            self.IPCMS_data
        )

        self.update_ops = UpdateOperations(
            self.customer_manager,
            self.IPCMS_data
        )

        self.import_ops = ImportOperations(
            self.customer_manager,
            self.product_manager,
            self.order_manager,
            self.IPCMS_data
        )

        self.export_ops = ExportOperations(
            self.customer_manager,
            self.product_manager,
            self.order_manager,
            self.IPCMS_data
        )

        self.report_generator = ReportGenerator(
            self.customer_manager,
            self.product_manager,
            self.order_manager,
            self.chart_generator
        )

        # Initialize the IPCMS UI for startup
        if not for_test_mode:
            welcome_message()
            if self.auth_service.login_system():
                self.menu_page()
            else:
                logging.error("Access denied.")

    # Load: Load data into controllers/managers
    def load_data(self):
        # Load customers
        for customer in self.enterprise_data.customers:
            try:
                self.customer_manager.create_customer(
                    first_name=customer.first_name,
                    last_name=customer.last_name,
                    dob=customer.dob,
                    email=customer.email,
                    phone=customer.phone,
                    country=customer.country,
                    city=customer.city,
                    postcode=customer.postcode,
                    created_at=customer.created_at,
                    updated_at=customer.updated_at,
                )
            except Exception as e:
                logging.error(f"Error loading customer '{customer.email}' - {str(e)}")

        # Load products
        for product in self.enterprise_data.products:
            try:
                self.product_manager.create_product(
                    product_id=product.product_id,
                    product_name=product.product_name,
                    price=product.price,
                    category=product.category,
                    stock_quantity=product.stock_quantity,
                    created_at=product.created_at,
                    updated_at=product.updated_at,
                )
            except Exception as e:
                logging.error(f"Error loading product '{product.product_id}' - {str(e)}")

        # Load orders
        for order in self.enterprise_data.orders:
            try:
                self.order_manager.create_order(
                    order_id=order.order_id,
                    order_date=order.order_date,
                    total_price=order.total_price,
                    order_products=[op.__dict__ for op in order.order_products],
                    payment_method=order.payment_method,
                    order_status=order.order_status,
                    created_at=order.created_at,
                    updated_at=order.updated_at,
                    customer_email=order.customer_email,
                )
            except Exception as e:
                logging.error(f"Error loading order '{order.order_id}' - {str(e)}")

    # Read: Display the main menu and handle user choices
    def menu_page(self):
        menu_options = {
            '1': ("Create a new Customer", self.create_ops.create_new_customer),
            '2': ("Create Payslip", self.create_ops.create_payslip),
            '3': ("View Customer", self.menu_view_customers),
            '4': ("View Currency Conversion Table Data", self.read_ops.view_currency_conversion_table),
            '5': ("View All Payslips", self.read_ops.view_all_payslips),
            '6': ("View Employee Information", self.read_ops.view_employee_info),
            '7': ("View Victoria Tax Table Data", self.read_ops.view_victoria_tax_table),
            '8': ("View Product", self.read_ops.display_product_table),
            '9': ("View Order", self.read_ops.display_orders),
            '10': ("View Chart", self.menu_display_charts),
            '11': ("Export Charts (.png)", self.chart_generator.export_all_charts),
            '12': ("Export Customer (customers.csv)", lambda: self.export_ops.export_csv('customer')),
            '13': ("Export Product (products.csv)", lambda: self.export_ops.export_csv('product')),
            '14': ("Export Orders (orders.json)", self.export_ops.export_orders_json),
            '15': ("Export Report (docx)", self.report_generator.export_report),
            '16': ("Import Customer (customers.csv)", lambda: self.import_ops.read_csv('customer')),
            '17': ("Import Product (products.csv)", lambda: self.import_ops.read_csv('product')),
            '18': ("Import Order (orders.json)", lambda: self.import_ops.read_json('order')),
        }

        while True:
            print(f"""
            --- Main Menu ---
    
            [ Create ]
            1. {menu_options['1'][0]}
            2. {menu_options['2'][0]}
            
            [ Read ] [ Update ] [ Delete ]
            3. {menu_options['3'][0]}
            
            [ Read ] [ Update ]
            4. {menu_options['4'][0]}
            
            [ Read ] [ Delete ]
            5. {menu_options['5'][0]}
            
            [ Read ]
            6. {menu_options['6'][0]}
            7. {menu_options['7'][0]}
            8. {menu_options['8'][0]}
            9. {menu_options['9'][0]}
            10. {menu_options['10'][0]}
    
            [ Export ]
            11. {menu_options['11'][0]}
            12. {menu_options['12'][0]}
            13. {menu_options['13'][0]}
            14. {menu_options['14'][0]}
            15. {menu_options['15'][0]}
    
            [ Import ]
            Please note that your files must be in the below path:
            {get_cur_location()}
            16. {menu_options['16'][0]}
            17. {menu_options['17'][0]}
            18. {menu_options['18'][0]}
            """)

            usr_chs = input("Enter your choice: ")

            # Check if the user's choice is valid
            if usr_chs in menu_options:
                # Execute the corresponding method
                menu_options[usr_chs][1]()
            else:
                logging.error("Invalid choice. Please try again.")

    # Read: Helper function of running the "View Customer" options in menu
    def menu_view_customers(self):
        while True:
            selected_customer = self.read_ops.display_customers()
            if selected_customer:
                action, customer = self.read_ops.display_customer_details(selected_customer)
                if action == 'update':
                    self.update_ops.update_customer(customer)
                elif action == 'delete':
                    self.delete_ops.delete_customer(customer)
                else:
                    logging.error("No valid action selected.")
            else:
                break  # Exit the loop if no customer is selected

    # Read: Helper function of running the "View Chart" options in menu
    def menu_display_charts(self):
        action = self.read_ops.display_charts()
        if action == 'top_selling_products':
            self.chart_generator.gen_bar_chart_top_selling_products()
        elif action == 'customer_location_distribution':
            self.chart_generator.gen_customer_location_distribution_chart()
        elif action == 'customer_age_distribution':
            self.chart_generator.gen_customer_age_distribution_chart()


if __name__ == "__main__":
    app = IPCMSApp()
