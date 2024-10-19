# data/data.py

from models.models import Customer, Product, Order


# Class:: Load and store initial data from the shop.
class EnterpriseData:
    def __init__(self, ipcms_data):
        # Uses an existing IPCMSData by parameter
        self.col_widths = ipcms_data.init_col_widths()
        self.customers = self.load_customers()
        self.products = self.load_products()
        self.orders = self.load_orders()

    # Read: Get required table's fields by category
    def get_required_fields(self, category):
        if category in self.col_widths:
            return list(self.col_widths[category].keys())
        return []

    # Load: customer
    def load_customers(self):
        customers = []
        for data in self.customer_data():
            customer = Customer(**data)
            customers.append(customer)
        return customers

    # load: products
    def load_products(self):
        products = []
        for data in self.products_data():
            product = Product(**data)
            products.append(product)
        return products

    # load: orders
    def load_orders(self):
        orders = []
        for data in self.orders_data():
            order_products = data.pop('order_products')
            data['order_products'] = order_products
            order = Order(**data)
            orders.append(order)
        return orders

    # staticmethod: customer data
    @staticmethod
    def customer_data():
        return [
            {
                'first_name': 'Matthew',
                'last_name': 'Contreras',
                'dob': '1995-10-07',
                'email': 'johnsmith@gmail.com',
                'phone': '0414-627-779',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '8018',
                'created_at': '2023-01-15 10:23:45',
                'updated_at': '2024-09-01 12:30:20',
            },
            {
                'first_name': 'Brenda',
                'last_name': 'Cannon',
                'dob': '1988-10-08',
                'email': 'janedoe@yahoo.com',
                'phone': '0495-195-938',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '6473',
                'created_at': '2023-03-10 14:45:50',
                'updated_at': '2024-09-02 09:15:12',
            },
            {
                'first_name': 'Kathryn',
                'last_name': 'Matthews',
                'dob': '1998-10-06',
                'email': 'bsmith@gmail.com',
                'phone': '0434-330-925',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '8552',
                'created_at': '2023-05-05 16:23:40',
                'updated_at': '2024-09-03 13:50:30',
            },
            {
                'first_name': 'Jeffrey',
                'last_name': 'Harris',
                'dob': '1997-10-06',
                'email': 'brobinson@duncan.com',
                'phone': '0432-125-147',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '6941',
                'created_at': '2023-07-18 11:12:56',
                'updated_at': '2024-09-04 10:24:42',
            },
            {
                'first_name': 'Megan',
                'last_name': 'Hunt',
                'dob': '1998-10-06',
                'email': 'sara11@gmail.com',
                'phone': '0437-725-970',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '9354',
                'created_at': '2023-09-10 15:35:18',
                'updated_at': '2024-09-05 14:45:05',
            },
            {
                'first_name': 'Michelle',
                'last_name': 'Perez',
                'dob': '2005-10-04',
                'email': 'lhall@todd.com',
                'phone': '0417-524-744',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '3806',
                'created_at': '2023-10-01 11:10:10',
                'updated_at': '2024-09-06 09:00:50',
            },
            {
                'first_name': 'Paul',
                'last_name': 'Wells',
                'dob': '1996-10-06',
                'email': 'tfowler@gmail.com',
                'phone': '0493-835-813',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '5999',
                'created_at': '2023-11-11 12:45:30',
                'updated_at': '2024-09-07 16:30:25',
            },
            {
                'first_name': 'April',
                'last_name': 'Jackson',
                'dob': '2003-10-05',
                'email': 'hmoore@gmail.com',
                'phone': '0467-509-349',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '3797',
                'created_at': '2023-12-02 17:22:45',
                'updated_at': '2024-09-08 10:45:00',
            },
            {
                'first_name': 'Steven',
                'last_name': 'Williams',
                'dob': '1996-10-06',
                'email': 'debkirby@gmail.com',
                'phone': '0420-868-981',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '4235',
                'created_at': '2023-05-20 09:13:29',
                'updated_at': '2024-09-09 11:25:35',
            },
            {
                'first_name': 'Johnny',
                'last_name': 'Hunter',
                'dob': '1972-10-12',
                'email': 'jonesh72@hotmail.com',
                'phone': '0416-324-280',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '5570',
                'created_at': '2024-01-15 14:00:00',
                'updated_at': '2024-09-10 08:32:17',
            },
            {
                'first_name': 'Kelly',
                'last_name': 'Nichols',
                'dob': '2000-10-05',
                'email': 'chris@hotmail.com',
                'phone': '0487-151-670',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '5978',
                'created_at': '2024-02-20 15:25:10',
                'updated_at': '2024-09-11 10:12:30',
            },
            {
                'first_name': 'Jeffrey',
                'last_name': 'Khan',
                'dob': '1978-10-11',
                'email': 'bradhunt@morris.com',
                'phone': '0431-567-236',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '2237',
                'created_at': '2024-03-01 18:12:45',
                'updated_at': '2024-09-12 09:45:00',
            },
            {
                'first_name': 'Kylie',
                'last_name': 'Nielsen',
                'dob': '1996-10-06',
                'email': 'susan95@gmail.com',
                'phone': '0478-672-709',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '5185',
                'created_at': '2024-04-15 13:50:20',
                'updated_at': '2024-09-13 08:40:10',
            },
            {
                'first_name': 'Benjamin',
                'last_name': 'Mclean',
                'dob': '1998-10-06',
                'email': 'dennis50@hotmail.com',
                'phone': '0457-727-934',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '4753',
                'created_at': '2024-05-18 14:25:45',
                'updated_at': '2024-09-14 11:15:35',
            },
            {
                'first_name': 'Larry',
                'last_name': 'Griffith',
                'dob': '2001-10-05',
                'email': 'pthompson@mitch.com',
                'phone': '0486-950-661',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '7479',
                'created_at': '2024-06-02 12:30:00',
                'updated_at': '2024-09-15 09:10:00',
            },
            {
                'first_name': 'Mathew',
                'last_name': 'Espinoza',
                'dob': '1995-10-07',
                'email': 'sabrina@cross.bz',
                'phone': '0472-861-982',
                'country': 'Australia',
                'city': 'Melbourne',
                'postcode': '7563',
                'created_at': '2024-07-01 16:10:50',
                'updated_at': '2024-09-16 14:50:50',
            },
            {
                'first_name': 'Haley',
                'last_name': 'Horton',
                'dob': '1962-10-15',
                'email': 'pfitz@yahoo.com',
                'phone': '0477-365-869',
                'country': 'Australia',
                'city': 'Sydney',
                'postcode': '8538',
                'created_at': '2024-08-05 13:35:45',
                'updated_at': '2024-09-17 09:35:50',
            },
            {
                'first_name': 'Vincent',
                'last_name': 'Ferguson',
                'dob': '1975-10-12',
                'email': 'jessica@hotmail.com',
                'phone': '0434-884-896',
                'country': 'Australia',
                'city': 'Brisbane',
                'postcode': '5312',
                'created_at': '2024-09-01 17:45:10',
                'updated_at': '2024-09-18 10:40:30',
            },
            {
                'first_name': 'Karen',
                'last_name': 'Lamb',
                'dob': '2006-10-04',
                'email': 'tonya67@gmail.com',
                'phone': '0487-741-344',
                'country': 'Australia',
                'city': 'Perth',
                'postcode': '7932',
                'created_at': '2024-10-01 18:15:35',
                'updated_at': '2024-09-19 12:25:55',
            },
            {
                'first_name': 'Matthew',
                'last_name': 'Jordan',
                'dob': '2005-10-04',
                'email': 'yvonne35@hotmail.com',
                'phone': '0447-179-830',
                'country': 'Australia',
                'city': 'Adelaide',
                'postcode': '3352',
                'created_at': '2024-11-12 13:12:45',
                'updated_at': '2024-09-20 16:45:30',
            },
        ]

    # staticmethod: product data
    @staticmethod
    def products_data():
        return [
            {
                "product_id": "001",
                "product_name": "EMO Robot (Lite)",
                "price": "311.98",
                "category": "Personal",
                "stock_quantity": "100",
                "created_at": "2024-01-10 09:15:23",
                "updated_at": "2024-09-01 12:45:56",
            },
            {
                "product_id": "002",
                "product_name": "EMO Robot (Classic)",
                "price": "389.98",
                "category": "Personal",
                "stock_quantity": "150",
                "created_at": "2024-02-11 10:45:30",
                "updated_at": "2024-09-02 14:35:40",
            },
            {
                "product_id": "003",
                "product_name": "EMO Robot (Dream)",
                "price": "436.78",
                "category": "Personal",
                "stock_quantity": "120",
                "created_at": "2024-03-12 14:30:00",
                "updated_at": "2024-09-03 16:25:42",
            },
            {
                "product_id": "004",
                "product_name": "EMO Robot (Ultimate)",
                "price": "514.78",
                "category": "Personal",
                "stock_quantity": "80",
                "created_at": "2024-04-14 08:12:45",
                "updated_at": "2024-09-04 09:20:50",
            },
            {
                "product_id": "005",
                "product_name": "Moxie Robot",
                "price": "1246.44",
                "category": "Educational",
                "stock_quantity": "50",
                "created_at": "2024-05-15 11:35:10",
                "updated_at": "2024-09-05 10:12:30",
            },
            {
                "product_id": "006",
                "product_name": "ROYBI Robot",
                "price": "310.44",
                "category": "Educational",
                "stock_quantity": "200",
                "created_at": "2024-06-16 10:15:22",
                "updated_at": "2024-09-06 12:10:15",
            },
            {
                "product_id": "007",
                "product_name": "Aibo Robot",
                "price": "4522.44",
                "category": "Pet",
                "stock_quantity": "30",
                "created_at": "2024-07-18 14:45:35",
                "updated_at": "2024-09-07 11:45:00",
            },
            {
                "product_id": "008",
                "product_name": "The Wild Robot - Roz",
                "price": "713.4",
                "category": "Love",
                "stock_quantity": "99",
                "created_at": "2024-09-18 08:45:35",
                "updated_at": "2024-09-30 11:45:00",
            },
        ]

    # staticmethod: order data
    @staticmethod
    def orders_data():
        return [
            {
                "order_id": "PO0001",
                "order_date": "21-08-2024",
                "order_status": "Shipped",
                "total_price": "2043.50",
                "order_products": [
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "3",
                        "price_per_unit": "389.98",
                        "total_price": "1169.94",
                    },
                    {
                        "product_id": "003",
                        "product_name": "EMO Robot (Dream)",
                        "quantity": "2",
                        "price_per_unit": "436.78",
                        "total_price": "873.56",
                    },
                ],
                "payment_method": "Credit Card",
                "customer_email": "johnsmith@gmail.com",
                "created_at": "2024-08-21 09:00:00",
                "updated_at": "2024-09-01 12:00:00",
            },
            {
                "order_id": "PO0002",
                "order_date": "25-08-2024",
                "order_status": "Delivered",
                "total_price": "3472.50",
                "order_products": [
                    {
                        "product_id": "005",
                        "product_name": "Moxie Robot",
                        "quantity": "1",
                        "price_per_unit": "1246.44",
                        "total_price": "1246.44",
                    },
                    {
                        "product_id": "004",
                        "product_name": "EMO Robot (Ultimate)",
                        "quantity": "1",
                        "price_per_unit": "514.78",
                        "total_price": "514.78",
                    },
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "3",
                        "price_per_unit": "310.44",
                        "total_price": "931.32",
                    },
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "2",
                        "price_per_unit": "389.98",
                        "total_price": "779.96",
                    },
                ],
                "payment_method": "PayPal",
                "customer_email": "janedoe@yahoo.com",
                "created_at": "2024-08-25 10:30:00",
                "updated_at": "2024-09-02 15:00:00",
            },
            {
                "order_id": "PO0003",
                "order_date": "16-08-2024",
                "order_status": "Shipped",
                "total_price": "5458.38",
                "order_products": [
                    {
                        "product_id": "007",
                        "product_name": "Aibo Robot",
                        "quantity": "1",
                        "price_per_unit": "4522.44",
                        "total_price": "4522.44",
                    },
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "3",
                        "price_per_unit": "311.98",
                        "total_price": "935.94",
                    },
                ],
                "payment_method": "Bank Transfer",
                "customer_email": "bjohnson@hotmail.com",
                "created_at": "2024-08-16 09:30:00",
                "updated_at": "2024-09-03 14:30:00",
            },
            {
                "order_id": "PO0004",
                "order_date": "09-08-2024",
                "order_status": "Delivered",
                "total_price": "14971.24",
                "order_products": [
                    {
                        "product_id": "007",
                        "product_name": "Aibo Robot",
                        "quantity": "3",
                        "price_per_unit": "4522.44",
                        "total_price": "13567.32",
                    },
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "2",
                        "price_per_unit": "389.98",
                        "total_price": "779.96",
                    },
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "2",
                        "price_per_unit": "311.98",
                        "total_price": "623.96",
                    },
                ],
                "payment_method": "Credit Card",
                "customer_email": "brobinson@duncan-wal",
                "created_at": "2024-08-09 11:45:00",
                "updated_at": "2024-09-04 16:00:00",
            },
            {
                "order_id": "PO0005",
                "order_date": "30-08-2024",
                "order_status": "Pending",
                "total_price": "9712.48",
                "order_products": [
                    {
                        "product_id": "005",
                        "product_name": "Moxie Robot",
                        "quantity": "3",
                        "price_per_unit": "1246.44",
                        "total_price": "3739.32",
                    },
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "2",
                        "price_per_unit": "311.98",
                        "total_price": "623.96",
                    },
                    {
                        "product_id": "003",
                        "product_name": "EMO Robot (Dream)",
                        "quantity": "1",
                        "price_per_unit": "436.78",
                        "total_price": "436.78",
                    },
                    {
                        "product_id": "007",
                        "product_name": "Aibo Robot",
                        "quantity": "1",
                        "price_per_unit": "4522.44",
                        "total_price": "4522.44",
                    },
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "1",
                        "price_per_unit": "389.98",
                        "total_price": "389.98",
                    },
                ],
                "payment_method": "Credit Card",
                "customer_email": "sara11@ward.com",
                "created_at": "2024-08-30 08:15:00",
                "updated_at": "2024-09-05 09:10:00",
            },
            {
                "order_id": "PO0006",
                "order_date": "02-09-2024",
                "order_status": "Shipped",
                "total_price": "311.98",
                "order_products": [
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "1",
                        "price_per_unit": "311.98",
                        "total_price": "311.98",
                    }
                ],
                "payment_method": "PayPal",
                "customer_email": "lhall@todd.com",
                "created_at": "2024-09-02 10:00:00",
                "updated_at": "2024-09-06 12:00:00",
            },
            {
                "order_id": "PO0007",
                "order_date": "05-09-2024",
                "order_status": "Delivered",
                "total_price": "1334.28",
                "order_products": [
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "2",
                        "price_per_unit": "310.44",
                        "total_price": "620.88",
                    },
                    {
                        "product_id": "008",
                        "product_name": "The Wild Robot - Roz",
                        "quantity": "1",
                        "price_per_unit": "713.40",
                        "total_price": "713.40",
                    },
                ],
                "payment_method": "Credit Card",
                "customer_email": "tfowler@gmail.com",
                "created_at": "2024-09-05 11:30:00",
                "updated_at": "2024-09-07 14:20:00",
            },
            {
                "order_id": "PO0008",
                "order_date": "08-09-2024",
                "order_status": "Pending",
                "total_price": "779.96",
                "order_products": [
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "2",
                        "price_per_unit": "389.98",
                        "total_price": "779.96",
                    }
                ],
                "payment_method": "Bank Transfer",
                "customer_email": "hmoore@gmail.com",
                "created_at": "2024-09-08 09:15:00",
                "updated_at": "2024-09-08 09:15:00",
            },
            {
                "order_id": "PO0009",
                "order_date": "10-09-2024",
                "order_status": "Shipped",
                "total_price": "436.78",
                "order_products": [
                    {
                        "product_id": "003",
                        "product_name": "EMO Robot (Dream)",
                        "quantity": "1",
                        "price_per_unit": "436.78",
                        "total_price": "436.78",
                    }
                ],
                "payment_method": "Credit Card",
                "customer_email": "debbie75@kirby.com",
                "created_at": "2024-09-10 14:45:00",
                "updated_at": "2024-09-09 11:25:35",
            },
            {
                "order_id": "PO0010",
                "order_date": "12-09-2024",
                "order_status": "Delivered",
                "total_price": "310.44",
                "order_products": [
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "1",
                        "price_per_unit": "310.44",
                        "total_price": "310.44",
                    }
                ],
                "payment_method": "PayPal",
                "customer_email": "jonesh@hotmail.com",
                "created_at": "2024-09-12 16:00:00",
                "updated_at": "2024-09-10 08:32:17",
            },
            {
                "order_id": "PO0011",
                "order_date": "14-09-2024",
                "order_status": "Pending",
                "total_price": "514.78",
                "order_products": [
                    {
                        "product_id": "004",
                        "product_name": "EMO Robot (Ultimate)",
                        "quantity": "1",
                        "price_per_unit": "514.78",
                        "total_price": "514.78",
                    }
                ],
                "payment_method": "Credit Card",
                "customer_email": "chrisg14@hotmail.com",
                "created_at": "2024-09-14 10:00:00",
                "updated_at": "2024-09-11 10:12:30",
            },
            {
                "order_id": "PO0012",
                "order_date": "16-09-2024",
                "order_status": "Shipped",
                "total_price": "935.94",
                "order_products": [
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "3",
                        "price_per_unit": "311.98",
                        "total_price": "935.94",
                    }
                ],
                "payment_method": "PayPal",
                "customer_email": "bradleyhunt@morris-s",
                "created_at": "2024-09-16 12:30:00",
                "updated_at": "2024-09-12 09:45:00",
            },
            {
                "order_id": "PO0013",
                "order_date": "18-09-2024",
                "order_status": "Delivered",
                "total_price": "1246.44",
                "order_products": [
                    {
                        "product_id": "005",
                        "product_name": "Moxie Robot",
                        "quantity": "1",
                        "price_per_unit": "1246.44",
                        "total_price": "1246.44",
                    }
                ],
                "payment_method": "Bank Transfer",
                "customer_email": "susan95@horton.com",
                "created_at": "2024-09-18 15:45:00",
                "updated_at": "2024-09-13 08:40:10",
            },
            {
                "order_id": "PO0014",
                "order_date": "20-09-2024",
                "order_status": "Shipped",
                "total_price": "623.96",
                "order_products": [
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "2",
                        "price_per_unit": "311.98",
                        "total_price": "623.96",
                    }
                ],
                "payment_method": "Credit Card",
                "customer_email": "dennis50@hotmail.com",
                "created_at": "2024-09-20 14:20:00",
                "updated_at": "2024-09-14 11:15:35",
            },
            {
                "order_id": "PO0015",
                "order_date": "22-09-2024",
                "order_status": "Delivered",
                "total_price": "1472.14",
                "order_products": [
                    {
                        "product_id": "008",
                        "product_name": "The Wild Robot - Roz",
                        "quantity": "2",
                        "price_per_unit": "713.40",
                        "total_price": "1426.80",
                    },
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "1",
                        "price_per_unit": "389.98",
                        "total_price": "389.98",
                    },
                ],
                "payment_method": "PayPal",
                "customer_email": "pthompson@mitchell-w",
                "created_at": "2024-09-22 11:00:00",
                "updated_at": "2024-09-15 09:10:00",
            },
            {
                "order_id": "PO0016",
                "order_date": "24-09-2024",
                "order_status": "Pending",
                "total_price": "4522.44",
                "order_products": [
                    {
                        "product_id": "007",
                        "product_name": "Aibo Robot",
                        "quantity": "1",
                        "price_per_unit": "4522.44",
                        "total_price": "4522.44",
                    }
                ],
                "payment_method": "Credit Card",
                "customer_email": "sabrinasmith@cross.b",
                "created_at": "2024-09-24 13:45:00",
                "updated_at": "2024-09-16 14:50:50",
            },
            {
                "order_id": "PO0017",
                "order_date": "26-09-2024",
                "order_status": "Shipped",
                "total_price": "389.98",
                "order_products": [
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "1",
                        "price_per_unit": "389.98",
                        "total_price": "389.98",
                    }
                ],
                "payment_method": "PayPal",
                "customer_email": "pfitzgerald@yahoo.co",
                "created_at": "2024-09-26 15:30:00",
                "updated_at": "2024-09-17 09:35:50",
            },
            {
                "order_id": "PO0018",
                "order_date": "28-09-2024",
                "order_status": "Delivered",
                "total_price": "310.44",
                "order_products": [
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "1",
                        "price_per_unit": "310.44",
                        "total_price": "310.44",
                    }
                ],
                "payment_method": "Bank Transfer",
                "customer_email": "jessica11@hotmail.co",
                "created_at": "2024-09-28 09:50:00",
                "updated_at": "2024-09-18 10:40:30",
            },
            {
                "order_id": "PO0019",
                "order_date": "30-09-2024",
                "order_status": "Pending",
                "total_price": "847.22",
                "order_products": [
                    {
                        "product_id": "003",
                        "product_name": "EMO Robot (Dream)",
                        "quantity": "1",
                        "price_per_unit": "436.78",
                        "total_price": "436.78",
                    },
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "1",
                        "price_per_unit": "311.98",
                        "total_price": "311.98",
                    },
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "1",
                        "price_per_unit": "310.44",
                        "total_price": "310.44",
                    },
                ],
                "payment_method": "Credit Card",
                "customer_email": "tonya67@durham.com",
                "created_at": "2024-09-30 11:15:00",
                "updated_at": "2024-09-19 12:25:55",
            },
            {
                "order_id": "PO0020",
                "order_date": "02-10-2024",
                "order_status": "Shipped",
                "total_price": "311.98",
                "order_products": [
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "1",
                        "price_per_unit": "311.98",
                        "total_price": "311.98",
                    }
                ],
                "payment_method": "PayPal",
                "customer_email": "yvonne35@hotmail.com",
                "created_at": "2024-10-02 13:00:00",
                "updated_at": "2024-09-20 16:45:30",
            },
            {
                "order_id": "PO0021",
                "order_date": "04-10-2024",
                "order_status": "Delivered",
                "total_price": "1521.52",
                "order_products": [
                    {
                        "product_id": "004",
                        "product_name": "EMO Robot (Ultimate)",
                        "quantity": "2",
                        "price_per_unit": "514.78",
                        "total_price": "1029.56",
                    },
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "1",
                        "price_per_unit": "389.98",
                        "total_price": "389.98",
                    },
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "1",
                        "price_per_unit": "310.44",
                        "total_price": "310.44",
                    },
                ],
                "payment_method": "Credit Card",
                "customer_email": "ystevenson@gmail.com",
                "created_at": "2024-10-04 14:45:00",
                "updated_at": "2024-09-21 15:25:45",
            },
            {
                "order_id": "PO0022",
                "order_date": "06-10-2024",
                "order_status": "Pending",
                "total_price": "713.40",
                "order_products": [
                    {
                        "product_id": "008",
                        "product_name": "The Wild Robot - Roz",
                        "quantity": "1",
                        "price_per_unit": "713.40",
                        "total_price": "713.40",
                    }
                ],
                "payment_method": "PayPal",
                "customer_email": "sarahnguyen@miranda-",
                "created_at": "2024-10-06 16:30:00",
                "updated_at": "2024-09-22 14:50:30",
            },
            {
                "order_id": "PO0023",
                "order_date": "08-10-2024",
                "order_status": "Shipped",
                "total_price": "623.96",
                "order_products": [
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "2",
                        "price_per_unit": "311.98",
                        "total_price": "623.96",
                    }
                ],
                "payment_method": "Credit Card",
                "customer_email": "david56@mclaughlin.c",
                "created_at": "2024-10-08 09:00:00",
                "updated_at": "2024-09-23 10:12:20",
            },
            {
                "order_id": "PO0024",
                "order_date": "10-10-2024",
                "order_status": "Delivered",
                "total_price": "389.98",
                "order_products": [
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "1",
                        "price_per_unit": "389.98",
                        "total_price": "389.98",
                    }
                ],
                "payment_method": "PayPal",
                "customer_email": "zavalamason@hotmail.",
                "created_at": "2024-10-10 11:15:00",
                "updated_at": "2024-09-24 12:35:00",
            },
            {
                "order_id": "PO0025",
                "order_date": "12-10-2024",
                "order_status": "Pending",
                "total_price": "1246.44",
                "order_products": [
                    {
                        "product_id": "005",
                        "product_name": "Moxie Robot",
                        "quantity": "1",
                        "price_per_unit": "1246.44",
                        "total_price": "1246.44",
                    }
                ],
                "payment_method": "Credit Card",
                "customer_email": "phyllis33@hotmail.co",
                "created_at": "2024-10-12 13:30:00",
                "updated_at": "2024-09-25 11:45:30",
            },
            {
                "order_id": "PO0026",
                "order_date": "14-10-2024",
                "order_status": "Shipped",
                "total_price": "2368.62",
                "order_products": [
                    {
                        "product_id": "005",
                        "product_name": "Moxie Robot",
                        "quantity": "1",
                        "price_per_unit": "1246.44",
                        "total_price": "1246.44",
                    },
                    {
                        "product_id": "003",
                        "product_name": "EMO Robot (Dream)",
                        "quantity": "2",
                        "price_per_unit": "436.78",
                        "total_price": "873.56",
                    },
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "1",
                        "price_per_unit": "310.44",
                        "total_price": "310.44",
                    },
                ],
                "payment_method": "PayPal",
                "customer_email": "phancock@hill-delgad",
                "created_at": "2024-10-14 15:45:00",
                "updated_at": "2024-09-26 13:15:00",
            },
            {
                "order_id": "PO0027",
                "order_date": "16-10-2024",
                "order_status": "Delivered",
                "total_price": "2335.94",
                "order_products": [
                    {
                        "product_id": "007",
                        "product_name": "Aibo Robot",
                        "quantity": "1",
                        "price_per_unit": "4522.44",
                        "total_price": "2261.22",
                    },
                    {
                        "product_id": "001",
                        "product_name": "EMO Robot (Lite)",
                        "quantity": "3",
                        "price_per_unit": "311.98",
                        "total_price": "935.94",
                    },
                ],
                "payment_method": "Bank Transfer",
                "customer_email": "bhess@hawkins-herrer",
                "created_at": "2024-10-16 17:00:00",
                "updated_at": "2024-09-27 14:25:10",
            },
            {
                "order_id": "PO0028",
                "order_date": "18-10-2024",
                "order_status": "Pending",
                "total_price": "826.76",
                "order_products": [
                    {
                        "product_id": "004",
                        "product_name": "EMO Robot (Ultimate)",
                        "quantity": "1",
                        "price_per_unit": "514.78",
                        "total_price": "514.78",
                    },
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "1",
                        "price_per_unit": "310.44",
                        "total_price": "310.44",
                    },
                ],
                "payment_method": "Credit Card",
                "customer_email": "brandon84@ferguson.c",
                "created_at": "2024-10-18 09:15:00",
                "updated_at": "2024-09-28 10:55:30",
            },
            {
                "order_id": "PO0029",
                "order_date": "20-10-2024",
                "order_status": "Shipped",
                "total_price": "1646.16",
                "order_products": [
                    {
                        "product_id": "006",
                        "product_name": "ROYBI Robot",
                        "quantity": "4",
                        "price_per_unit": "310.44",
                        "total_price": "1241.76",
                    },
                    {
                        "product_id": "002",
                        "product_name": "EMO Robot (Classic)",
                        "quantity": "1",
                        "price_per_unit": "389.98",
                        "total_price": "389.98",
                    },
                ],
                "payment_method": "PayPal",
                "customer_email": "anne89@barnes.com",
                "created_at": "2024-10-20 11:30:00",
                "updated_at": "2024-09-29 11:30:15",
            },
            {
                "order_id": "PO0030",
                "order_date": "22-10-2024",
                "order_status": "Delivered",
                "total_price": "1646.16",
                "order_products": [
                    {
                        "product_id": "003",
                        "product_name": "EMO Robot (Dream)",
                        "quantity": "2",
                        "price_per_unit": "436.78",
                        "total_price": "873.56",
                    },
                    {
                        "product_id": "008",
                        "product_name": "The Wild Robot - Roz",
                        "quantity": "1",
                        "price_per_unit": "713.40",
                        "total_price": "713.40",
                    },
                ],
                "payment_method": "Bank Transfer",
                "customer_email": "wdavis@hotmail.com",
                "created_at": "2024-10-22 13:45:00",
                "updated_at": "2024-09-30 09:20:50",
            },
        ]


# Class:: Load and store initial data specific to the ERP system.
class IPCMSData:
    def __init__(self):
        self.welcome_message = "Welcome to the ERP System!"
        self.full_served_countries = self.load_full_served_countries()
        # Initialize EnterpriseData after IPCMSData is fully set up
        self.enterprise_data = EnterpriseData(self)
        self.custom_headers = {
            'customers': self.gen_customer_headers(),
            'products': self.gen_product_headers(),
            'orders': self.gen_order_headers(),
        }
        self.col_widths = self.init_col_widths()
        self.employee_login_dict = self.load_employee_login_dict()
        self.currency_conversion_table = self.load_currency_conversion_table()
        self.employee_data_with_constraints = self.load_employee_data_with_constraints()
        self.victoria_tax_table = self.load_victoria_tax_table()
        self.payslip_table = self.load_payslip_table()

    # staticmethod: Initialize column widths for tables.
    @staticmethod
    def init_col_widths():
        return {
            'customers': {
                "first_name": 12, "last_name": 12, "dob": 12, "email": 20,
                "phone": 12, "country": 12, "city": 12, "postcode": 4,
                "created_at": 19, "updated_at": 19,
            },
            'products': {
                "product_id": 3, "product_name": 30, "price": 10,
                "category": 10, "stock_quantity": 6, "created_at": 19,
                "updated_at": 19,
            },
            'orders': {
                "order_id": 6, "order_date": 10, "order_status": 10,
                "total_price": 10, "order_products": {
                    "product_id": 3, "product_name": 30, "quantity": 3,
                    "price_per_unit": 10, "total_price": 10,
                },
                "payment_method": 20, "customer_email": 20,
                "created_at": 19, "updated_at": 19,
            },
            'employee_login_dict': {
                "EmployeeID": 10,
                "Login Name": 8,
                "Password": 8
            },
            'currency_conversion_table': {
                "Country": 15,
                "Curr Code": 10,
                "Rate to AUD": 10
            },
            'employee_data_with_constraints': {
                "EmployeeID": 10,
                "Full Name": 20,
                "Department": 20,
                "Title": 20,
                "Base Yearly Salary": 15,
                "System Access Level": 5,
                "Workstation Name": 10,
                "Country": 15
            },
            'victoria_tax_table': {
                "Income Range Min": 20,
                "Income Range Max": 20,
                "Tax Rate (%)": 15
            },
            'payslip_table': {
                "ID": 20,
                "EmployeeID": 10,
                "Full Name": 20,
                "Department": 20,
                "Title": 20,
            }
        }

    # Load: full served countries
    def load_full_served_countries(self):
        full_served_countries = {}
        served_countries = self.served_countries()
        served_postcode_format = self.served_postcode_format()

        for country in served_countries:
            country_name = country["Country"]
            full_served_countries[country_name] = {
                "Country Code": country["Country Code"],
                "Curr Code": country["Curr Code"],
                "Rate to AUD": country["Rate to AUD"],
            }

        for country_name, postcode_format in served_postcode_format.items():
            if country_name in full_served_countries:
                full_served_countries[country_name]["Postcode Format"] = postcode_format

        return full_served_countries

    # Load: employee login data
    @staticmethod
    def load_employee_login_dict():
        return {
            100000: {"Login Name": "admin", "Password": "admin123"},
            100001: {"Login Name": "jdoe", "Password": "e4a5Tc2m"},
            100002: {"Login Name": "jsmith", "Password": "9TpXk8Mb"},
            100003: {"Login Name": "ajohnson", "Password": "Ls7qP5Bm"},
            100004: {"Login Name": "ebrown", "Password": "Tn4kW2Vh"},
            100005: {"Login Name": "mdavis", "Password": "6QwEr3Xj"},
            100006: {"Login Name": "swilson", "Password": "Jh9qL6Pn"},
            100007: {"Login Name": "rlee", "Password": "Ap8sK2Qw"},
            100008: {"Login Name": "jwhite", "Password": "Dm3nP9Xh"},
            100009: {"Login Name": "dtaylor", "Password": "Fs6vL4Xn"},
            100010: {"Login Name": "athomas", "Password": "Zk2sW8Tj"},
            100011: {"Login Name": "amartin", "Password": "Xr3vP9Qn"},
            100012: {"Login Name": "mjackson", "Password": "Yn7mK4Ws"},
            100013: {"Login Name": "wharris", "Password": "Qj8tL6Pn"},
            100014: {"Login Name": "orobinson", "Password": "Vs4mP7Xn"},
            100015: {"Login Name": "jclark", "Password": "Hs9vK3Pm"},
            100016: {"Login Name": "slewis", "Password": "Bm7pW2Qx"},
            100017: {"Login Name": "lwalker", "Password": "Kn5qV9Xs"},
            100018: {"Login Name": "chall", "Password": "Ps6vL4Xj"},
            100019: {"Login Name": "ballen", "Password": "Zk3mW8Vn"},
            100020: {"Login Name": "myoung", "Password": "Qs7tP4Wm"}
        }

    # Load: currency conversion data
    @staticmethod
    def load_currency_conversion_table():
        return (
            {"Country": "Australia", "Curr Code": "AUD", "Rate to AUD": 1.0},
            {"Country": "Hong Kong", "Curr Code": "HKD", "Rate to AUD": 5.6},
            {"Country": "China", "Curr Code": "CNY", "Rate to AUD": 4.6},
            {"Country": "Malaysia", "Curr Code": "MYR", "Rate to AUD": 3.2},
            {"Country": "Vietnam", "Curr Code": "VND", "Rate to AUD": 16000.0},
            {"Country": "India", "Curr Code": "INR", "Rate to AUD": 55.3}
        )

    # Load: employee data with constraints
    @staticmethod
    def load_employee_data_with_constraints():
        return [
            {
                "EmployeeID": 100000,
                "Full Name": "Admin User",
                "Department": "Administration",
                "Title": "Administrator",
                "Base Yearly Salary": 150000,
                "Country": "Australia",
                "System Access Level": "Admin",
                "Workstation Name": "WS-Admin"
            },
            {
                "EmployeeID": 100001,
                "Full Name": "John Doe",
                "Department": "IT Department",
                "Title": "System Administrator",
                "Base Yearly Salary": 80000.23,
                "Country": "Australia",
                "System Access Level": "Admin",
                "Workstation Name": "WS-1001"
            },
            {
                "EmployeeID": 100002,
                "Full Name": "Jane Smith",
                "Department": "HR Department",
                "Title": "HR Specialist",
                "Base Yearly Salary": 65000.75,
                "Country": "India",
                "System Access Level": "User",
                "Workstation Name": "WS-1002"
            },
            {
                "EmployeeID": 100003,
                "Full Name": "Albert Johnson",
                "Department": "Finance Department",
                "Title": "Accountant",
                "Base Yearly Salary": 90000.5,
                "Country": "China",
                "System Access Level": "User",
                "Workstation Name": "WS-1003"
            },
            {
                "EmployeeID": 100004,
                "Full Name": "Emily Brown",
                "Department": "Logistics Solution",
                "Title": "Flight Coordinator",
                "Base Yearly Salary": 78000,
                "Country": "Hong Kong",
                "System Access Level": "User",
                "Workstation Name": "WS-1004"
            },
            {
                "EmployeeID": 100005,
                "Full Name": "Michael Davis",
                "Department": "Sales Department",
                "Title": "Sales Executive",
                "Base Yearly Salary": 85000,
                "Country": "Australia",
                "System Access Level": "User",
                "Workstation Name": "WS-1005"
            },
            {
                "EmployeeID": 100006,
                "Full Name": "Sarah Wilson",
                "Department": "IT Department",
                "Title": "Developer",
                "Base Yearly Salary": 95000,
                "Country": "Vietnam",
                "System Access Level": "User",
                "Workstation Name": "WS-1006"
            },
            {
                "EmployeeID": 100007,
                "Full Name": "Robert Lee",
                "Department": "HR Department",
                "Title": "HR Manager",
                "Base Yearly Salary": 110000,
                "Country": "Malaysia",
                "System Access Level": "Admin",
                "Workstation Name": "WS-1007"
            },
            {
                "EmployeeID": 100008,
                "Full Name": "Jessica White",
                "Department": "Finance Department",
                "Title": "Payroll Specialist",
                "Base Yearly Salary": 67000,
                "Country": "India",
                "System Access Level": "User",
                "Workstation Name": "WS-1008"
            },
            {
                "EmployeeID": 100009,
                "Full Name": "Daniel Taylor",
                "Department": "Logistics Solution",
                "Title": "Shipping Coordinator",
                "Base Yearly Salary": 76000,
                "Country": "China",
                "System Access Level": "User",
                "Workstation Name": "WS-1009"
            },
            {
                "EmployeeID": 100010,
                "Full Name": "Amanda Thomas",
                "Department": "Sales Department",
                "Title": "Sales Associate",
                "Base Yearly Salary": 64000,
                "Country": "Australia",
                "System Access Level": "User",
                "Workstation Name": "WS-1010"
            },
            {
                "EmployeeID": 100011,
                "Full Name": "Andrew Martin",
                "Department": "IT Department",
                "Title": "IT Manager",
                "Base Yearly Salary": 120000,
                "Country": "Hong Kong",
                "System Access Level": "Admin",
                "Workstation Name": "WS-1011"
            },
            {
                "EmployeeID": 100012,
                "Full Name": "Megan Jackson",
                "Department": "HR Department",
                "Title": "HR Specialist",
                "Base Yearly Salary": 68000,
                "Country": "Vietnam",
                "System Access Level": "User",
                "Workstation Name": "WS-1012"
            },
            {
                "EmployeeID": 100013,
                "Full Name": "William Harris",
                "Department": "Finance Department",
                "Title": "Finance Manager",
                "Base Yearly Salary": 130000,
                "Country": "Malaysia",
                "System Access Level": "Admin",
                "Workstation Name": "WS-1013"
            },
            {
                "EmployeeID": 100014,
                "Full Name": "Olivia Robinson",
                "Department": "Logistics Solution",
                "Title": "Logistics Manager",
                "Base Yearly Salary": 115000,
                "Country": "China",
                "System Access Level": "Admin",
                "Workstation Name": "WS-1014"
            },
            {
                "EmployeeID": 100015,
                "Full Name": "James Clark",
                "Department": "Sales Department",
                "Title": "Sales Manager",
                "Base Yearly Salary": 125000,
                "Country": "Vietnam",
                "System Access Level": "Admin",
                "Workstation Name": "WS-1015"
            },
            {
                "EmployeeID": 100016,
                "Full Name": "Sophia Lewis",
                "Department": "IT Department",
                "Title": "Developer",
                "Base Yearly Salary": 85000,
                "Country": "India",
                "System Access Level": "User",
                "Workstation Name": "WS-1016"
            },
            {
                "EmployeeID": 100017,
                "Full Name": "Liam Walker",
                "Department": "HR Department",
                "Title": "HR Specialist",
                "Base Yearly Salary": 72000,
                "Country": "Australia",
                "System Access Level": "User",
                "Workstation Name": "WS-1017"
            },
            {
                "EmployeeID": 100018,
                "Full Name": "Chloe Hall",
                "Department": "Finance Department",
                "Title": "Payroll Specialist",
                "Base Yearly Salary": 66000,
                "Country": "Malaysia",
                "System Access Level": "User",
                "Workstation Name": "WS-1018"
            },
            {
                "EmployeeID": 100019,
                "Full Name": "Benjamin Allen",
                "Department": "Logistics Solution",
                "Title": "Shipping Coordinator",
                "Base Yearly Salary": 80000,
                "Country": "Hong Kong",
                "System Access Level": "User",
                "Workstation Name": "WS-1019"
            },
            {
                "EmployeeID": 100020,
                "Full Name": "Mia Young",
                "Department": "Sales Department",
                "Title": "Sales Executive",
                "Base Yearly Salary": 92000,
                "Country": "China",
                "System Access Level": "User",
                "Workstation Name": "WS-1020"
            }
        ]

    # Load: Victoria tax table data
    @staticmethod
    def load_victoria_tax_table():
        return {
            (0, 18200.0, 0.0),
            (18201, 45000.0, 19.0),
            (45001, 120000.0, 32.5),
            (120001, 180000.0, 37.0),
            (180001, None, 45.0)
        }

    # Load: Initialize payslip table
    @staticmethod
    def load_payslip_table():
        return []

    # staticmethod: served countries data
    @staticmethod
    def served_countries():
        return [
            {"Country": "Australia", "Country Code": "AUS", "Curr Code": "AUD", "Rate to AUD": 1.0},
            {"Country": "Hong Kong", "Country Code": "HKG", "Curr Code": "HKD", "Rate to AUD": 5.6},
            {"Country": "China", "Country Code": "CHN", "Curr Code": "CNY", "Rate to AUD": 4.6},
            {"Country": "Malaysia", "Country Code": "MYS", "Curr Code": "MYR", "Rate to AUD": 3.2},
            {"Country": "Vietnam", "Country Code": "VNM", "Curr Code": "VND", "Rate to AUD": 16000.0},
            {"Country": "India", "Country Code": "IND", "Curr Code": "INR", "Rate to AUD": 55.3},
        ]

    # staticmethod: served postcode format data
    @staticmethod
    def served_postcode_format():
        return {
            "Australia": r'^\d{4}$',
            "Hong Kong": r'^0000$',
            "China": r'^\d{6}$',
            "Malaysia": r'^\d{5}$',
            "Vietnam": r'^\d{6}$',
            "India": r'^\d{6}$',
        }

    # Read: Generate customized customer table's headers
    def gen_customer_headers(self):
        headers = list(self.enterprise_data.col_widths['customers'].keys())
        if 'postcode' in headers:
            headers[headers.index('postcode')] = 'pc'
        headers.insert(0, "No.")
        return headers

    # Read: Generate customized product table's headers
    def gen_product_headers(self):
        headers = list(self.enterprise_data.col_widths['products'].keys())
        headers[headers.index('product_id')] = 'pid'
        headers[headers.index('stock_quantity')] = 'qty'
        return headers

    # Read: Generate customized order table's headers
    def gen_order_headers(self):
        headers = list(self.enterprise_data.col_widths['orders'].keys())
        return headers
