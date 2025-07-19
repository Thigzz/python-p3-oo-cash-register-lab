#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.last_transaction_amount = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        self.last_transaction_amount = item_total
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self, percentage=None):
        actual_percentage = percentage if percentage is not None else self.discount

        if actual_percentage > 0:
            discount_factor = (100 - actual_percentage) / 100.0
            self.total = int(self.total * discount_factor)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction_amount > 0 and self.items:
            self.total -= self.last_transaction_amount
            self.items.pop()
            self.last_transaction_amount = 0

    def get_total(self):
        return self.total