
class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.products = []  # Зберігаються пари (ID продукту, кількість)
        self.total_amount = 0  # Загальна сума замовлення

    def check_product_availability(self, product_id, quantity, db):
        """Перевірка наявності товару в достатній кількості"""
        product = db.get_product_by_id(product_id)
        if product and product['stock_quantity'] >= quantity:
            return True
        return False

    def update_order_amount(self, product_id, quantity, db):
        """Оновлює суму замовлення"""
        product = db.get_product_by_id(product_id)
        self.total_amount += product['price'] * quantity

    def add_product(self, product_id, quantity, db):
        """Додає продукт до замовлення за ID, зменшуючи кількість товару"""
        if self.check_product_availability(product_id, quantity, db):
            self.products.append((product_id, quantity))  # Додаємо пару (ID продукту, кількість)
            self.update_order_amount(product_id, quantity, db)  # Оновлюємо суму
            db.update_product_stock(product_id, quantity)  # Оновлюємо кількість продукту
            db.update_order(self)  # Оновлюємо ордер у базі
        else:
            print(f"Продукт з ID {product_id} не знайдений або недостатньо на складі.")
        db.save_data()

    def view_order(self, db):
        """Повертає деталі замовлення з інформацією про продукти"""
        order_details = {
            'order_id': str(self.order_id),
            'user': self.user.name,
            'products': [(db.get_product_by_id(product_id)['name'], quantity) for product_id, quantity in self.products],
            'total_amount': self.total_amount
        }
        return order_details