# Main.py
from bson import ObjectId
from Users.User import User
from Orders.OrderFactory import OrderFactory
from Database.Database import Database
from Observer import OrderNotifier, OnlineStoreObserver

# Ініціалізація бази даних (Singleton)
db = Database()

# Оновлення кількості товару
db.update_product_quantity_by_name("PS5", 5)
db.update_product_quantity_by_name("Laptop", 15)
db.update_product_quantity_by_name("Smartphone", 30)
db.update_product_quantity_by_name("Headphones", 20)

# Створення користувача
user1 = User(user_id=ObjectId(), name="John Doe", email="john@example.com", password="1306986")
if user1.register(db):
    print("Користувач успішно зареєстрований.")
else:
    print("Реєстрація не вдалася.")

# Логін користувача
if user1.login("1306986", db):
    print("Користувач успішно увійшов.")
else:
    print("Невірні облікові дані.")

# Використання фабрики для створення замовлення (regular)
order = OrderFactory.create_order('regular', ObjectId(), user1)
order.add_product("Laptop", 10, db)
order.add_product("PS5", 5, db)
order.add_product("Smartphone", 15, db)

# Налаштування Observer для сповіщення інтернет-магазину
notifier = OrderNotifier()
store_observer = OnlineStoreObserver()
notifier.subscribe(store_observer)

# Перегляд замовлення
order_details = order.view_order(db)
print("Деталі замовлення:", order_details)

# Збереження замовлення в базі даних
if order.save_order(db):
    print("Замовлення збережено.")
    # Сповіщення інтернет-магазину про нове замовлення
    notifier.notify(order)
else:
    print("Помилка збереження замовлення.")
