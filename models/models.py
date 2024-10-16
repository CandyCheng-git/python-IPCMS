# models/models.py

from utils.validators import CheckValidator


class Customer:
    """A customer object."""

    def __init__(
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
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.country = country
        self.city = city
        self.postcode = postcode
        self.created_at = created_at
        self.updated_at = updated_at


class Product:
    """A product object."""

    def __init__(
            self,
            product_id,
            product_name,
            price,
            category,
            stock_quantity,
            created_at,
            updated_at,
    ):
        self.product_id = str(product_id)
        self.product_name = product_name
        self.price = float(price)
        self.category = category
        self.created_at = created_at
        self.updated_at = updated_at
        validator = CheckValidator()
        self.stock_quantity = int(stock_quantity) if validator.is_numeric(stock_quantity) else 0


class OrderedProduct:
    """An ordered product object."""

    def __init__(
        self, product_id, product_name, quantity, price_per_unit, total_price
    ):
        self.product_id = str(product_id)
        self.product_name = product_name
        self.quantity = int(quantity)
        self.price_per_unit = float(price_per_unit)
        self.total_price = float(total_price)


class Order:
    """An order object."""

    def __init__(
            self,
            order_id,
            order_date,
            order_status,
            total_price,
            order_products,
            payment_method,
            created_at,
            updated_at,
            customer_email,
    ):
        self.order_id = order_id
        self.order_date = order_date
        self.order_status = order_status
        self.total_price = float(total_price)
        self.payment_method = payment_method
        self.created_at = created_at
        self.updated_at = updated_at
        self.customer_email = customer_email
        self.order_products = [
            OrderedProduct(
                product_id=prd['product_id'],
                product_name=prd.get('product_name', ''),
                quantity=int(prd['quantity']),
                price_per_unit=float(prd['price_per_unit']),
                total_price=prd.get('total_price', int(prd['quantity']) * float(prd['price_per_unit']))
            ) if isinstance(prd, dict) else prd for prd in order_products
        ]
