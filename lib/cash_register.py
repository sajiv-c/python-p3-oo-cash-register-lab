#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    print("Building")
    self.discount = discount
    self.total = total
    self.items = []
    self.last_transaction = 0
    print("Finished Building")

  def add_item(self, title, price, quantity = 1):
    self.total += (price * quantity)

    self.last_transaction = (price * quantity)

    i = 0

    for i in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    discount_percent = self.discount * 0.01
    if((type(self.discount) == int) and (self.discount > 0)):
      self.total = int(self.total - (self.total * discount_percent))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= float(self.last_transaction)
    