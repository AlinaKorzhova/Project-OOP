from src.oop_class import Product, Category


def test_product(product1):
    assert product1.name == "Огурец"
    assert product1.description == "Овощ"
    assert product1.price == 100.00
    assert product1.quantity == 5


def test_category(product_in_category):
    assert product_in_category.name == "Фрукты"
    assert product_in_category.description == "Разные фрукты"

    assert len(product_in_category.products) == 67
    assert product_in_category.products == "Огурец, 100.0 руб. Остаток: 5 шт.\nБанан, 50.0 руб. Остаток: 10 шт.\n"

    assert product_in_category.total_categories == 1


def test_category_products_property():
    category = Category("Фрукты", "Разные фрукты")
    category.add_product(Product("Банан", "Фрукт", 50.0, 10))
    category.add_product(Product("Яблоко", "Фрукт", 80.0, 5))
    expected = "Банан, 50.0 руб. Остаток: 10 шт.\nЯблоко, 80.0 руб. Остаток: 5 шт.\n"
    assert category.products == expected


def test_add_product():
    prod1 = Product("Огурец", "Овощ", 100.00, 5)
    prod2 = Product("Банан", "Фрукт", 50.00, 10)
    assert prod1 + prod2 == (100.00 * 5) + (50.00 * 10)


def test_category_str_representation():
    category = Category("Фрукты", "Разные фрукты")
    category.add_product(Product("Банан", "Фрукт", 50.0, 10))
    category.add_product(Product("Яблоко", "Фрукт", 80.0, 5))
    assert str(category) == "Фрукты, количество продуктов: 15 шт."