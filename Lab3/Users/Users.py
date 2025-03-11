
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.orders = []

    def register(self, users_data, db):
        if self.email not in users_data:
            users_data[self.email] = {
                "user_id": str(self.user_id),
                "name": self.name,
                "password": self.password
            }
            db.save_data()
        return users_data

    def login(self, password, users_data):
        if self.email in users_data and users_data[self.email]['password'] == password:
            return True
        return False