#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0
    
  def add_item(self, title, price,quantity=1):
    self.total += price * quantity
    self.last_transaction_amount = price * quantity
    for _ in range(quantity):
      self.items.append(title)
      
      
  def apply_discount(self):
    if self.discount > 0:
      discount_amount = (self.discount / 100) * self.total 
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    self.total -= self.last_transaction_amount