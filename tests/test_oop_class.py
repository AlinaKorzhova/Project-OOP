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

    assert product_in_category.category_count == 1
    assert product_in_category.product_count == 0
