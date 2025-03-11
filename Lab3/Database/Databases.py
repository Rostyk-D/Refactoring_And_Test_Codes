import json
from bson import ObjectId

class Database:
    def __init__(self, file_name="Data/data.json"):
        self.file_name = file_name
        self.load_data()
        self.initialize_products()  # Додаємо продукти, якщо база пуста

    def load_data(self):
        """Завантаження даних з файлу"""
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.products_data = data.get("products", {})
                self.users_data = data.get("users", {})
                self.orders_data = data.get("orders", {})
        except FileNotFoundError:
            self.products_data = {}
            self.users_data = {}
            self.orders_data = {}

    def initialize_products(self):
        """Додає стартові продукти, якщо їх немає в базі даних"""
        if not self.products_data:
            self.products_data = {
                str(ObjectId()): {"name": "Laptop", "price": 1000, "stock_quantity": 100},
                str(ObjectId()): {"name": "Smartphone", "price": 500, "stock_quantity": 200},
                str(ObjectId()): {"name": "Headphones", "price": 100, "stock_quantity": 300},
                str(ObjectId()): {"name": "PS5", "price": 2250, "stock_quantity": 300}
            }
            self.save_data()  # Збереження після додавання стартових продуктів

    def save_data(self):
        """Збереження даних у файл"""
        data = {
            "products": self.convert_objectid_to_str(self.products_data),
            "users": self.convert_objectid_to_str(self.users_data),
            "orders": self.convert_objectid_to_str(self.orders_data)
        }
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def convert_objectid_to_str(self, data):
        """Перетворює всі ObjectId в рядки у даних"""
        if isinstance(data, dict):
            return {k: self.convert_objectid_to_str(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self.convert_objectid_to_str(item) for item in data]
        elif isinstance(data, ObjectId):
            return str(data)
        else:
            return data

    def get_product_by_id(self, product_id):
        """Повертає продукт за ID з бази даних"""
        return self.products_data.get(str(product_id))

    def update_product_stock(self, product_id, quantity):
        """Оновлює кількість товару після додавання до замовлення"""
        product = self.get_product_by_id(product_id)
        if product and product['stock_quantity'] >= quantity:
            product['stock_quantity'] -= quantity
            return True
        return False

    def update_order(self, order):
        """Оновлює ордер у базі даних"""
        self.orders_data[str(order.order_id)] = {
            'order_id': str(order.order_id),
            'user': {
                'user_id': str(order.user.user_id),
                'name': order.user.name,
                'email': order.user.email
            },
            'products': [(product_id, quantity) for product_id, quantity in order.products],
            'total_amount': order.total_amount
        }