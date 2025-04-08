# Observer.py
class OrderNotifier:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, order):
        for observer in self.observers:
            observer.update(order)

class OnlineStoreObserver:
    def update(self, order):
        print(f"Інтернет-магазин сповіщає: нове замовлення від {order.user.name} отримано. Загальна сума: {order.total_amount}")
