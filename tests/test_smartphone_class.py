def test_smartphone_init(smartphone_product1):
    assert smartphone_product1.name == "Samsung"
    assert smartphone_product1.model == "S10"
    assert smartphone_product1.memory == 256
    assert smartphone_product1.color == "Зеленый"
    assert smartphone_product1.efficiency == 6
    assert smartphone_product1.description == "Сматрфон"
    assert smartphone_product1.price == 60000.0
    assert smartphone_product1.quantity == 5


def test_smartphone_add(smartphone_product1, smartphone_product2):
    assert smartphone_product1 + smartphone_product2 == 650000.0


def test_smartphone_error(smartphone_product1, smartphone_product2):
    assert smartphone_product1 + 1
