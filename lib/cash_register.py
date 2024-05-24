#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount= 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transaction = []

  def add_item(self, item, price, amount=1):
     if amount <= 0:
        print("Amount must be a positive integer. Item not added.")
        return
     
     self.total += price * amount

     for _ in range(amount):
      self.items.append(item)

     self.previous_transaction.append(
         {'item': item, 'amount' : amount, 'price': price}
    )

  def apply_discount(self):
      if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f'After the discount, the total comes to ${self.total}.')

      else:
            print('There is no discount to apply.')

  def void_last_transaction(self):
    if not self.previous_transaction:
       return 'There is no previous transaction to void.'
    
    transaction = self.previous_transaction[-1]
    for _ in range(transaction['amount']):
        self.items.pop()

    self.total -= transaction['price'] * transaction['amount']
    self.previous_transaction.pop()


