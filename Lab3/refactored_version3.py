from Users.Users import User
from Orders.Orders2 import Order
from Database.Databases2 import Database, ObjectId

# Приклад використання
db = Database()

# Оновлення кількості товару за назвою
db.update_product_quantity_by_name("PS5", 5)  # Додати 5 одиниць до PS5
db.update_product_quantity_by_name("Laptop", 15)  # Додати 10 одиниць до Laptop
db.update_product_quantity_by_name("Smartphone", 30)  # Зменшити 3 одиниці для Smartphone
db.update_product_quantity_by_name("Headphones", 10)  # Зменшити 3 одиниці для Smartphone

# Створення користувача
user1 = User(user_id=ObjectId(), name="John Doe", email="john@example.com", password="1234")
db.users_data = user1.register(db.users_data, db)  # Користувач 1 реєструється

# Логін користувача
if user1.login(password="1234", users_data=db.users_data):
    print("User logged in successfully")
else:
    print("Invalid credentials")

# Створення замовлення без додавання нових продуктів
order = Order(order_id=ObjectId(), user=user1)
order.add_product("67d013a8402f0d15784427ea", 2, db)  # Додати 2 одиниці продукту (Laptop)
order.add_product("67d013a8402f0d15784427ec", 3, db)  # Додати 3 одиниці продукту (Headphones)
order.add_product("67d013a8402f0d15784427eb", 5, db)  # Додати 3 одиниці продукту (Smartphone)

# Перегляд замовлення
print(order.view_order(db))  # Має вивести правильну суму 3500

# Збереження всіх даних
db.save_data()
