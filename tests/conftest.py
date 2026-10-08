import pytest
from src.oop_class import Product, Category

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

