

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount):
        pass


class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        discount = 0.05  # 5% discount
        return order_amount * (1 - discount)


class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        discount = 0.10  # 10% discount
        return order_amount * (1 - discount)


class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        discount = 0.20  # 20% discount
        return order_amount * (1 - discount)


class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount
        self.discount_strategy = self._get_discount_strategy()

    def _get_discount_strategy(self):
        if self.customer_type == "Regular":
            return RegularDiscount()
        elif self.customer_type == "Premium":
            return PremiumDiscount()
        elif self.customer_type == "VIP":
            return VIPDiscount()
        else:
            raise ValueError("Unknown customer type")

    def final_price(self):
        return self.discount_strategy.apply_discount(self.order_amount)

order1 = Order("Regular", 100)
print(f"Final price for Regular customer: ${order1.final_price():.2f}")

order2 = Order("Premium", 200)
print(f"Final price for Premium customer: ${order2.final_price():.2f}")

order3 = Order("VIP", 300)
print(f"Final price for VIP customer: ${order3.final_price():.2f}")
