from Database.Databases import Database, ObjectId
from Orders.Orders import Order
from Users.Users import User

# Приклад використання
db = Database()

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
order.add_product("67c6dd63402f0d22e46daa54", 2, db)  # Додати 2 одиниці продукту (Laptop)
order.add_product("67c6dd63402f0d22e46daa55", 3, db)  # Додати 3 одиниці продукту (Headphones)
order.add_product("67c6dd63402f0d22e46daa56", 5, db)  # Додати 3 одиниці продукту (Smartphone)

# Перегляд замовлення
print(order.view_order(db))  # Має вивести правильну суму 3500

# Збереження всіх даних
db.save_data()
