from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(3)

def test_can_add_item_to_cart(cart):
    cart.add("manzana")

    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add("pera")

    assert "pera" in cart.get_items()

def test_when_add_more_than_max_items_should_fail(cart):
    for i in range(3):
        cart.add(i)
    
    print(f"Estoy aqui {cart.size()}")
    with pytest.raises(OverflowError):
        cart.add("manzana")

def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")

    def mock_get_item(item: str):
        if item =="apple":
            return 1.0
        if item == "orange":
            return 2.0
    
    item_database = ItemDatabase()
    item_database.get = MagicMock(side_effect = mock_get_item)

    assert cart.get_total_price(item_database) == 3.0

