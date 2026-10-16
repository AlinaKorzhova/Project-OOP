
def test_lawnglass_init(lawnglass_product1):
    assert lawnglass_product1.name == "Овес"
    assert lawnglass_product1.description == "Зерновая культура"
    assert lawnglass_product1.price == 10
    assert lawnglass_product1.quantity == 10000
    assert lawnglass_product1.country == "Россия"
    assert lawnglass_product1.germination_period == "30 дней"
    assert lawnglass_product1.color == "Золотой"

def test_lawnglass_add(lawnglass_product1, lawnglass_product2):
    assert lawnglass_product1 + lawnglass_product2 == 155000

def test_lawnglass_error(lawnglass_product1, lawnglass_product2):
    assert lawnglass_product1 + 1