# Test.py
import unittest
from pymongo import MongoClient
from bson import ObjectId

from Database.Database import Database
from Orders.Order import OrderRegular, OrderBulk
from Orders.OrderFactory import OrderFactory
from Users.User import User
from Observer import OrderNotifier, OnlineStoreObserver
from Project1.Config.Config import connection_string_mongo

class TestSingletonDatabase(unittest.TestCase):
    def test_singleton_database_instance(self):
        db1 = Database()
        db2 = Database()
        self.assertIs(db1, db2, "Database instances are not the same (Singleton pattern failed)")

class TestFactoryPattern(unittest.TestCase):
    def test_factory_create_regular_order(self):
        user = User(user_id=ObjectId(), name="Factory Test User", email="factory@example.com", password="pwd")
        order = OrderFactory.create_order('regular', ObjectId(), user)
        self.assertIsInstance(order, OrderRegular, "Factory did not create a regular order")

    def test_factory_create_bulk_order(self):
        user = User(user_id=ObjectId(), name="Factory Test User", email="factory2@example.com", password="pwd")
        order = OrderFactory.create_order('bulk', ObjectId(), user)
        self.assertIsInstance(order, OrderBulk, "Factory did not create a bulk order")

    def test_factory_invalid_order_type(self):
        user = User(user_id=ObjectId(), name="Factory Test User", email="factory3@example.com", password="pwd")
        with self.assertRaises(ValueError):
            OrderFactory.create_order('invalid', ObjectId(), user)

class DummyObserver:
    def __init__(self):
        self.notifications = []

    def update(self, order):
        self.notifications.append(order)

class TestObserverPattern(unittest.TestCase):
    def test_observer_notified_on_order(self):
        notifier = OrderNotifier()
        dummy = DummyObserver()
        notifier.subscribe(dummy)
        user = User(user_id=ObjectId(), name="Observer User", email="observer@example.com", password="pwd")
        order = OrderFactory.create_order('regular', ObjectId(), user)
        order.total_amount = 100
        notifier.notify(order)
        self.assertEqual(len(dummy.notifications), 1, "Observer was not notified correctly")
        self.assertEqual(dummy.notifications[0].total_amount, 100)

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        self.db_instance = Database()
        self.client = MongoClient(connection_string_mongo)
        self.db = self.client['My']
        # Очищення колекцій для ізольованого тестування
        self.db['Products'].delete_many({})
        self.db['Orders'].delete_many({})
        self.db['Accounts'].delete_many({})
        self.db_instance.initialize_products()

    def tearDown(self):
        self.db['Products'].delete_many({})
        self.db['Orders'].delete_many({})
        self.db['Accounts'].delete_many({})

    def test_initialize_products(self):
        products = list(self.db['Products'].find({}))
        self.assertGreaterEqual(len(products), 4)

    def test_update_product_quantity_by_name_success(self):
        product_before = self.db_instance.get_product_by_name("Laptop")
        initial_qty = product_before["stock_quantity"]
        result = self.db_instance.update_product_quantity_by_name("Laptop", 5)
        product_after = self.db_instance.get_product_by_name("Laptop")
        self.assertTrue(result)
        self.assertEqual(product_after["stock_quantity"], initial_qty + 5)

    def test_get_product_by_name_nonexistent(self):
        product = self.db_instance.get_product_by_name("Tablet")
        self.assertIsNone(product)

class TestOrderOperations(unittest.TestCase):
    def setUp(self):
        self.db_instance = Database()
        self.client = MongoClient(connection_string_mongo)
        self.db = self.client['My']
        self.db['Products'].delete_many({})
        self.db['Orders'].delete_many({})
        self.db['Accounts'].delete_many({})
        self.db_instance.initialize_products()
        self.user = User(user_id=ObjectId(), name="Order Test User", email="order@example.com", password="pwd")

    def tearDown(self):
        self.db['Products'].delete_many({})
        self.db['Orders'].delete_many({})
        self.db['Accounts'].delete_many({})

    def test_add_product_success(self):
        order = OrderFactory.create_order('regular', ObjectId(), self.user)
        order.add_product("Laptop", 2, self.db_instance)
        self.assertEqual(len(order.products), 1)

    def test_total_amount_calculation_regular(self):
        order = OrderFactory.create_order('regular', ObjectId(), self.user)
        product = self.db_instance.get_product_by_name("Laptop")
        order.add_product("Laptop", 2, self.db_instance)
        expected_total = product["price"] * 2
        self.assertEqual(order.total_amount, expected_total)

    def test_total_amount_calculation_bulk(self):
        order = OrderFactory.create_order('bulk', ObjectId(), self.user)
        product = self.db_instance.get_product_by_name("Laptop")
        order.add_product("Laptop", 2, self.db_instance)
        expected_total = product["price"] * 2 * 0.9  # враховуючи знижку bulk
        self.assertEqual(order.total_amount, expected_total)

    def test_view_order(self):
        order = OrderFactory.create_order('regular', ObjectId(), self.user)
        order.add_product("PS5", 1, self.db_instance)
        details = order.view_order(self.db_instance)
        self.assertEqual(details["user"], self.user.name)
        self.assertEqual(len(details["products"]), 1)

    def test_save_order(self):
        order = OrderFactory.create_order('regular', ObjectId(), self.user)
        order.add_product("Headphones", 2, self.db_instance)
        result = order.save_order(self.db_instance)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
