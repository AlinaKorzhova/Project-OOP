from pyexpat.errors import messages

from src.lawngrass_class import LawnGrass
from src.oop_class import Product
from src.smartphone_class import Smartphone


def test_product(product1):
    assert product1.name == "Огурец"
    assert product1.description == "Овощ"
    assert product1.price == 100.00
    assert product1.quantity == 5


def test_category(product_in_category):
    assert product_in_category.name == "Фрукты"
    assert product_in_category.description == "Разные фрукты"

    assert len(product_in_category.products) == 66
    assert product_in_category.products == "Огурец, 100.0 руб. Остаток: 5 шт.\nБанан, 50.0 руб. Остаток: 10 шт."

    assert product_in_category.category_count == 1
    assert product_in_category.product_count == 2


def test_category_initial_products(category_with_products, product1, product2):
    assert len(category_with_products._Category__products) == 2

    expected_str = (
        f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.\n"
        f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт."
    )
    assert category_with_products.products == expected_str

def test_mixinlog(capsys):
    Product("Огурец", "Овощ", 100.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == ""

    LawnGrass("Овес", "Зерновая культура", 10, 10000, "Россия", "30 дней", "Золотой")
    message = capsys.readouterr()
    assert message.out.strip() == ""

    Smartphone("Samsung", "Сматрфон", 60000.0, 5, 6, "S10", 256, "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == ""