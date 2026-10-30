import pytest

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


def test_new_product_existing_product_updates_quantity_and_price():
    existing = Product("Огурец", "Овощ", 100.0, 5)
    products_list = [existing]

    new_data = {"name": "Огурец", "price": 120.0, "quantity": 3}

    result = Product.new_product(new_data, products_list)

    assert result is existing
    assert existing.quantity == 8
    assert existing.price == 120.0


def test_new_product_creates_new_when_not_found():
    products_list = []
    new_data = {"name": "Помидор", "price": "80.0", "quantity": "4"}  # строки, чтобы проверить float/int

    result = Product.new_product(new_data, products_list)

    assert len(products_list) == 1
    assert products_list[0] is result
    assert result.name == "Помидор"
    assert result.price == 80.0
    assert result.quantity == 4


def test_new_product_multiple_products_in_list_finds_correct_one():
    p1 = Product("Огурец", "Овощ", 100.0, 5)
    p2 = Product("Банан", "Фрукт", 50.0, 10)
    products_list = [p1, p2]

    new_data = {"name": "Банан", "price": 60.0, "quantity": 5}

    result = Product.new_product(new_data, products_list)

    assert result is p2  # обновился именно Банан
    assert p2.quantity == 15
    assert p2.price == 60.0


def test_new_product_no_update_if_name_mismatch():
    p = Product("Огурец", "Овощ", 100.0, 5)
    products_list = [p]

    new_data = {"name": "Томат", "price": 90.0, "quantity": 3}

    result = Product.new_product(new_data, products_list)

    assert result is not p  # это новый объект
    assert len(products_list) == 2


def test_price_setter_updates_price_when_positive(capsys):
    p = Product("Огурец", "Овощ", 100.0, 5)
    p.price = 120.0

    assert p.price == 120.0
    out, _ = capsys.readouterr()
    assert out.strip() == "Product('Огурец', 'Овощ', 100.0, 5)"


def test_price_setter_rejects_zero_and_prints_message(capsys):
    p = Product("Огурец", "Овощ", 100.0, 5)
    p.price = 0

    assert p.price == 100.0

    out, _ = capsys.readouterr()
    expected_msg = "Цена не должна быть нулевая или отрицательная"
    assert expected_msg in out


def test_add_two_products_returns_sum_of_total_cost():
    p1 = Product("Огурец", "Овощ", 100.0, 5)   # total_cost = 500.0
    p2 = Product("Банан", "Фрукт", 50.0, 10)   # total_cost = 500.0

    result = p1 + p2

    assert result == 1000.0



def test_price_setter_updates_price_when_positive(capsys):
    # Сначала сбрасываем буфер, чтобы не мешали другие принты
    capsys.readouterr()

    p = Product("Огурец", "Овощ", 100.0, 5)
    # Если MixinLog печатает при создании, прочитаем и отбросим это
    capsys.readouterr()

    p.price = 120.0  # меняем цену

    assert p.price == 120.0

    out, _ = capsys.readouterr()  # читаем, что напечаталось именно при смене цены
    assert out.strip() == ""  # при корректной цене print не вызывается



def test_category_initial_products(category_with_products, product1, product2):
    assert len(category_with_products._Category__products) == 2

    expected_str = (
        f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.\n"
        f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт."
    )
    assert category_with_products.products == expected_str

def test_mixinlog_prints_correct_message(capsys):
    Product("Огурец", "Овощ", 100.0, 5)
    out, _ = capsys.readouterr()

    expected = "Product('Огурец', 'Овощ', 100.0, 5)\n"
    assert out == expected

    LawnGrass("Овес", "Зерновая культура", 10, 10000, "Россия", "30 дней", "Золотой")
    out, _ = capsys.readouterr()

    expected = "LawnGrass('Овес', 'Зерновая культура', 10, 10000)\n"
    assert out == expected

    Smartphone("Samsung", "Сматрфон", 60000.0, 5, 6, "S10", 256, "Зеленый")
    out, _ = capsys.readouterr()

    expected = "Smartphone('Samsung', 'Сматрфон', 60000.0, 5)\n"
    assert out == expected


def test_product_raises():
    with pytest.raises(ValueError) as e_info:
        Product("Огурец", "Овощ", 100.0, 0)

