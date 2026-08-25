
class Inventory :
    """
    Class Inventory represents a shop inventory
    """
    def __init__(self):
        self.inventory_items = []

    def add_inventory_item(self, inventory_item):
        """
        Adds an inventory item to the inventory list
        :param inventory_item:
        """
        self.inventory_items.append(inventory_item)


class InventoryItem:
    """
    Class InventoryItem represents a shop inventory item
    """
    def __init__(self, id, name, price, amount_in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.amount_in_stock = amount_in_stock
