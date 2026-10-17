def test_product(product1):
    assert product1.name == "Огурец"
    assert product1.description == "Овощ"
    assert product1.price == 100.00
    assert product1.quantity == 5


def test_price_ignored():
    p = Product("Яблоко", "Фрукт", 30.0, 2)
    old_price = p.price
    p.price = -5.0
    assert p.price == old_price


def test_new_product_updates_quantity_and_price():
    products_list = [Product("Ананас", "Троп. фрукт", 200.0, 3)]
    product_dict = {"name": "Ананас", "price": 250.0, "quantity": 5}
    updated = Product.new_product(product_dict, products_list)
    assert updated.quantity == 5
    assert updated.price == 250.0

    assert product_in_category.category_count == 1
    assert product_in_category.product_count == 0
