def test_product(product1):
    assert product1.name == "Огурец"
    assert product1.description == "Овощ"
    assert product1.price == 100.00
    assert product1.quantity == 5


def test_category(product_in_category):
    assert product_in_category.name == "Фрукты"
    assert product_in_category.description == "Разные фрукты"

    assert len(product_in_category.products) == 2
    assert product_in_category.products[0].name == "Огурец"
    assert product_in_category.products[0].description == "Овощ"
    assert product_in_category.products[0].price == 100.0
    assert product_in_category.products[0].quantity == 5

    assert product_in_category.products[1].name == "Банан"
    assert product_in_category.products[1].description == "Фрукт"
    assert product_in_category.products[1].price == 50.0
    assert product_in_category.products[1].quantity == 10

    assert product_in_category.category_count == 1
    assert product_in_category.product_count == 0
