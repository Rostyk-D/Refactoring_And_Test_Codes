import unittest
from Users.Users import User
from Orders.Orders2 import Order
from Database.Databases2 import Database, ObjectId

class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.user = User(user_id="67d01ec4402f0d0f24221358", name="John", email="john_Doe@example.com", password="1234")
        self.db.users_data = self.user.register(self.db.users_data, self.db)
        self.db.users_data[self.user.email]['user_id'] = str(self.user.user_id)  # Ensure the user_id matches

    def test_user_registration(self):
        self.assertIn(self.user.email, self.db.users_data)
        self.assertEqual(self.db.users_data[self.user.email]['user_id'], str(self.user.user_id))

    def test_user_login_success(self):
        self.assertTrue(self.user.login(password="1234", users_data=self.db.users_data))

    def test_user_login_failure(self):
        self.assertFalse(self.user.login(password="wrongpassword", users_data=self.db.users_data))

    def test_update_product_quantity_by_name_add(self):
        self.db.update_product_quantity_by_name("Smartphone", 5)

        # Find the product by name
        for product in self.db.products_data.values():
            if product['name'] == "Smartphone":
                # Check the updated quantity
                self.assertEqual(product["stock_quantity"], 95)
                break
        else:
            self.fail("Product 'PS5' not found in the database")

    def test_update_product_quantity_by_name_subtract(self):
        # Update the product quantity
        self.db.update_product_quantity_by_name("Headphones", 5)
        self.db.update_product_quantity_by_name("Headphones", -5)

        # Find the product by name
        for product in self.db.products_data.values():
            if product['name'] == "Headphones":
                # Check the updated quantity
                self.assertEqual(product["stock_quantity"], 80)
                break
        else:
            self.fail("Product 'Headphones' not found in the database")

    def test_update_product_quantity_by_name_nonexistent(self):
        with self.assertRaises(KeyError):
            self.db.update_product_quantity_by_name("NonexistentProduct", 5)

    def test_order_creation(self):
        order = Order(order_id=ObjectId(), user=self.user)
        self.assertEqual(order.user, self.user)

    def test_add_product_to_order(self):
        order = Order(order_id=ObjectId(), user=self.user)
        order.add_product("67d013a8402f0d15784427ed", 2, self.db)
        self.assertIn(("67d013a8402f0d15784427ed", 2), order.products)

    def test_view_order(self):
        order = Order(order_id=ObjectId(), user=self.user)
        order.add_product("67d013a8402f0d15784427ed", 2, self.db)
        order_summary = order.view_order(self.db)
        self.assertIn("PS5", [product[0] for product in order_summary['products']])

    def test_remove_user(self):
        # Add a user to the database
        self.db.users_data['john_Doe@example.com'] = {
            'user_id': '67d01ec4402f0d0f24221358',
            'name': 'John',
            'password': '1234'
        }

        # Remove the user
        self.db.remove_user('john@example.com')

        # Check if the user is removed
        self.assertNotIn('john@example.com', self.db.users_data)

if __name__ == '__main__':
    unittest.main()