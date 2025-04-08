# OrderFactory.py
from .Order import OrderRegular, OrderBulk

class OrderFactory:
    @staticmethod
    def create_order(order_type, order_id, user):
        if order_type == 'regular':
            return OrderRegular(order_id, user)
        elif order_type == 'bulk':
            return OrderBulk(order_id, user)
        else:
            raise ValueError("Unknown order type")
