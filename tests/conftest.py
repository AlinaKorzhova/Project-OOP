import pytest
from src.oop_class import Product, Category
from src.Smartphone_class import Smartphone
from src.LawnGrass_class import LawnGrass

@pytest.fixture
def product1():
    return Product(
        name="Огурец",
        description="Овощ",
        price=100.0,
        quantity=5,
    )


@pytest.fixture
def product2():
    return Product(
        name="Банан",
        description="Фрукт",
        price=50.0,
        quantity=10,
    )


@pytest.fixture
def product_in_category(product1, product2):
    category = Category(
        name="Фрукты",
        description="Разные фрукты"
    )
    category.add_product(product1)  # можно и в «Фрукты», логика не строгая, главное — в категорию
    category.add_product(product2)
    return category


@pytest.fixture
def smartphone_product1():
    return Smartphone("Samsung", "S10", 256, "Зеленый", 6, "Сматрфон", 60000.0, 5)


@pytest.fixture
def smartphone_product2():
    return Smartphone("Samsung", "S20", 256, "Зеленый", 6, "Сматрфон", 70000.0, 5)


@pytest.fixture
def lawnglass_product1():
    return LawnGrass("Овес", "Зерновая культура", 10, 10000, "Россия", "30 дней", "Золотой")


@pytest.fixture
def lawnglass_product2():
    return LawnGrass("Пшеница", "Зерновая культура", 11, 5000, "Россия", "30 дней", "Золотой")
