
class ShoppingCart:
    """
    Class ShoppingCart represents a shopping cart
    """
    def __init__(self, inventory):
        self.inventory = inventory

        self.items_in_cart = []


    def add_inventory_item(self, item, amount):
        """
        Add an items to the shopping cart
        :param item: item type to add
        :param amount: amount of items to add
        """

        if item not in self.inventory.inventory_items:
            raise ValueError("Item is not in inventory")

        if item.amount_in_stock < amount:
            raise ValueError("Not enough items in stock")

        cart_item = CartItem(
            item.id,
            item.name,
            item.price,
            amount
        )

        self.items_in_cart.append(cart_item) # adds the selected item as a cart item into cart
        item.amount_in_stock -= amount # remove items from inventory


class CartItem:
    """
    Class CartItem represents a cart item
    """
    def __init__(self, id, name, price, amount_in_cart):
        self.id = id
        self.name = name
        self.price = price
        self.amount_in_cart = amount_in_cart