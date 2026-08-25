import pytest
from shoppingcart.inventory import InventoryItem, Inventory
from shoppingcart.shopping_cart import ShoppingCart

@pytest.mark.integration
@pytest.mark.task3
def test_add_inventory_item_in_stock(sample_inventory):
    """
    Tests that add_inventory_item() correctly adds inventory items in stock to shopping_cart.
    :param sample_inventory: a sample inventory object from fixture
    """

    inventory_item = InventoryItem(100, "slaghammare", 250, 5)

    sample_inventory.add_inventory_item(inventory_item)
    assert inventory_item in sample_inventory.inventory_items

    shopping_cart = ShoppingCart(sample_inventory)
    shopping_cart.add_inventory_item(inventory_item, 2)

    assert len(shopping_cart.items_in_cart) == 1
    assert shopping_cart.items_in_cart[0].id == 100
    assert shopping_cart.items_in_cart[0].amount_in_cart == 2


@pytest.mark.integration
@pytest.mark.task3
def test_add_inventory_item_not_in_stock(sample_inventory):
    """
    Tests that add_inventory_item() correctly does not add inventory items not in stock to shopping_cart.
    :param sample_inventory: a sample inventory object from fixture
    """

    inventory_item = InventoryItem(100, "slaghammare", 250, 0)

    sample_inventory.add_inventory_item(inventory_item)
    assert inventory_item in sample_inventory.inventory_items

    shopping_cart = ShoppingCart(sample_inventory)

    with pytest.raises(ValueError):
        shopping_cart.add_inventory_item(inventory_item, 1)

    assert len(shopping_cart.items_in_cart) == 0


@pytest.mark.integration
@pytest.mark.task3
def test_add_inventory_not_enough_items_in_stock(sample_inventory):
    """
    Tests that add_inventory_item() correctly does not add inventory items to shopping_cart when not enought items in stock.
    :param sample_inventory: a sample inventory object from fixture
    """

    inventory_item = InventoryItem(100, "slaghammare", 250, 3)

    sample_inventory.add_inventory_item(inventory_item)
    assert inventory_item in sample_inventory.inventory_items

    shopping_cart = ShoppingCart(sample_inventory)

    with pytest.raises(ValueError):
        shopping_cart.add_inventory_item(inventory_item, 4)

    assert len(shopping_cart.items_in_cart) == 0


@pytest.mark.integration
@pytest.mark.task3
def test_add_inventory_two_carts_same_item_type_in_stock(sample_inventory):
    """
    Tests that add_inventory_item() correctly adds inventory items in stock to two shopping_cart adding same item type.
    :param sample_inventory: a sample inventory object from fixture
    """

    inventory_item = InventoryItem(100, "slaghammare", 250, 3)

    sample_inventory.add_inventory_item(inventory_item)

    shopping_cart_a = ShoppingCart(sample_inventory)
    shopping_cart_a.add_inventory_item(inventory_item, 1)

    assert len(shopping_cart_a.items_in_cart) == 1
    assert shopping_cart_a.items_in_cart[0].id == 100
    assert shopping_cart_a.items_in_cart[0].amount_in_cart == 1

    shopping_cart_b = ShoppingCart(sample_inventory)
    shopping_cart_b.add_inventory_item(inventory_item, 1)

    assert len(shopping_cart_b.items_in_cart) == 1
    assert shopping_cart_b.items_in_cart[0].id == 100
    assert shopping_cart_b.items_in_cart[0].amount_in_cart == 1

    assert inventory_item.amount_in_stock == 1


@pytest.mark.integration
@pytest.mark.task3
def test_add_inventory_two_carts_same_item_type_not_in_stock(sample_inventory):
    """
    Tests that add_inventory_item() correctly does not add inventory items to second shopping_cart when first
    shopping cart reduced available items.
    :param sample_inventory: a sample inventory object from fixture
    """

    inventory_item = InventoryItem(100, "slaghammare", 250, 3)
    sample_inventory.add_inventory_item(inventory_item)

    shopping_cart_a = ShoppingCart(sample_inventory)
    shopping_cart_a.add_inventory_item(inventory_item, 2)

    assert len(shopping_cart_a.items_in_cart) == 1
    assert shopping_cart_a.items_in_cart[0].id == 100
    assert shopping_cart_a.items_in_cart[0].amount_in_cart == 2

    shopping_cart_b = ShoppingCart(sample_inventory)

    with pytest.raises(ValueError):
        shopping_cart_b.add_inventory_item(inventory_item, 2)

    assert len(shopping_cart_b.items_in_cart) == 0

    assert inventory_item.amount_in_stock == 1

