# controllers/controllers.py

from datetime import datetime
import logging
from models.models import Customer, Product, Order


# Class:: Manage all operations which is related to a Customer
class CustomerController:
    def __init__(self, order_manager):
        self.customers = []
        self.order_manager = order_manager

    # Create: customer
    def create_customer(
            self,
            first_name,
            last_name,
            dob,
            email,
            phone,
            country,
            city,
            postcode,
            created_at,
            updated_at,
    ):
        new_customer = Customer(
            first_name,
            last_name,
            dob,
            email,
            phone,
            country,
            city,
            postcode,
            created_at,
            updated_at,
        )
        existing_customer = self.get_customer_by_email(new_customer.email)
        if existing_customer:
            self.update_customer_by_email(new_customer)
        else:
            self.customers.append(new_customer)

    # Read: get a customer by email
    def get_customer_by_email(self, email):
        return next((c for c in self.customers if c.email == email), None)

    # Read: Get a list of all customers.
    def get_all_customers(self):
        return self.customers

    # Update: Update a customer's information by email.
    def update_customer_by_email(self, new_customer):
        for idx, existing_customer in enumerate(self.customers):
            if existing_customer.email == new_customer.email:
                new_customer.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.customers[idx] = new_customer
                logging.info(f"Customer '{new_customer.email}' updated successfully.")
                return
        logging.error(f"Customer '{new_customer.email}' not found.")

    # Delete: Delete a customer by email.
    def delete_customer(self, email):
        existing_customer = self.get_customer_by_email(email)
        if existing_customer:
            confirmation = input(f"Are you sure you want to delete {email}? (y/n): ")
            if confirmation.lower() == 'y':
                self.order_manager.delete_orders_by_customer_email(email)
                self.customers.remove(existing_customer)
                logging.info(f"Customer '{email}' deleted.")
            else:
                logging.info("Deletion cancelled.")
        else:
            logging.error(f"Customer with email '{email}' does not exist.")


# Class:: Manage all operations related to a Product.
class ProductController:
    def __init__(self):
        self.products = []

    # Create: product
    def create_product(
            self,
            product_id,
            product_name,
            price,
            category,
            stock_quantity,
            created_at,
            updated_at,
    ):
        if price < 0:
            logging.error("Invalid price: Price cannot be negative.")
            return False
        product = Product(
            product_id,
            product_name,
            price,
            category,
            stock_quantity,
            created_at,
            updated_at,
        )
        existing_product = self.get_product_by_id(product_id)
        if existing_product:
            self.update_product_by_id(product)
        else:
            self.products.append(product)

    # Read: Get a product by product ID.
    def get_product_by_id(self, product_id):
        return next((p for p in self.products if p.product_id == str(product_id).strip()), None)

    # Read: Get a list of all products.
    def get_all_products(self):
        return self.products

    # Update: Update a product's information by product ID.
    def update_product_by_id(self, new_product):
        if new_product is None:
            logging.error("Cannot update a None product.")
            return False
        for idx, existing_product in enumerate(self.products):
            if existing_product.product_id == new_product.product_id:
                existing_product.product_name = new_product.product_name
                existing_product.price = new_product.price
                existing_product.category = new_product.category
                existing_product.stock_quantity = new_product.stock_quantity
                existing_product.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logging.info(f"Product '{new_product.product_name}' updated successfully.")
                return True
        logging.error(f"Product '{new_product.product_id}' not found.")
        return False


# Class:: Manage all operations related to an Order.
class OrderController:
    def __init__(self, product_manager):
        self.orders = []
        self.product_manager = product_manager

    # Create: order
    def create_order(
            self,
            order_id,
            order_date,
            total_price,
            order_products,
            payment_method,
            order_status,
            created_at,
            updated_at,
            customer_email
    ):
        for prd in order_products:
            if not self.product_manager.get_product_by_id(prd['product_id']):
                logging.error(f"Product {prd['product_id']} does not exist. Order creation cancelled.")
                return None
        order = Order(
            order_id,
            order_date,
            order_status,
            total_price,
            order_products,
            payment_method,
            created_at,
            updated_at,
            customer_email
        )
        existing_order = self.get_order_by_id(order_id)
        if existing_order:
            self.update_order_by_id(order)
        else:
            self.orders.append(order)

    # Read: Get an order by order ID.
    def get_order_by_id(self, order_id):
        return next((order for order in self.orders if order.order_id == order_id), None)

    # Read: Get a list of all orders.
    def get_all_orders(self):
        return self.orders

    # Update: Update an order's information by order ID.
    def update_order_by_id(self, new_order):
        for idx, existing_order in enumerate(self.orders):
            if existing_order.order_id == new_order.order_id:
                for key, value in vars(new_order).items():
                    setattr(existing_order, key, value)
                existing_order.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logging.info(f"Order '{new_order.order_id}' updated successfully.")
                return True
        logging.error(f"Order '{new_order.order_id}' not found.")
        return False

    # Delete: Delete all orders associated with a customer's email.
    def delete_orders_by_customer_email(self, customer_email):
        self.orders = [
            order for order in self.orders if order.customer_email != customer_email
        ]
        logging.info(f"All orders for customer '{customer_email}' have been deleted.")
