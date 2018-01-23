# Module: purchase_items
class PurchaseItem():
    # Class constructor
    def __init__(self):
        self.items_price = {'a': 10, 'b': 15, 'c': 20, 'd': 25, 'e': 30}
        self.items_quantity = {'a': 5, 'b': 12, 'c': 22, 'd': 10, 'e': 10}

    # Function: pick up item
    def purchase_item(self, item, amount):
        item_price = self.items_price[item]
        current_quantity = self.items_quantity[item]
        self.items_quantity[item] = current_quantity - amount
        return item_price * amount

    # Function: Get items and quantities for each in stock
    def get_items(self):
        return self.items_quantity

    # Function: Get items and their prices
    def get_items_prices(self):
        return self.items_price
