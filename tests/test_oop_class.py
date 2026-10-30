import pytest

from src.lawngrass_class import LawnGrass
from src.oop_class import Product, Category
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


def test_add_product_successfully_adds_product():
    """Проверяем, что продукт корректно добавляется в категорию."""
    category = Category(name="Фрукты", description="Сочные фрукты")
    product = Product("Банан", "Фрукт", 50.0, 10)

    initial_len = len(category._Category__products)
    initial_count = Category.product_count

    category.add_product(product)

    assert len(category._Category__products) == initial_len + 1
    assert category._Category__products[-1] is product
    assert Category.product_count == initial_count + 1


def test_add_product_raises_type_error_for_non_product():
    """Проверяем, что при передаче не-Product выбрасывается TypeError."""
    category = Category(name="Овощи", description="Зелёные овощи")
    invalid_item = "Не продукт"  # строка вместо объекта Product

    with pytest.raises(TypeError) as exc_info:
        category.add_product(invalid_item)

    assert "В категорию можно добавить только объект Product" in str(exc_info.value)


def test_add_product_multiple_products():
    """Проверяем добавление нескольких продуктов подряд."""
    category = Category(name="Напитки", description="Всё для бодрости")
    p1 = Product("Чай", "Напиток", 100.0, 5)
    p2 = Product("Кофе", "Напиток", 200.0, 3)

    category.add_product(p1)
    category.add_product(p2)

    products = category._Category__products
    assert len(products) == 2
    assert products[0] is p1
    assert products[1] is p2

    assert Category.product_count >= 2


def test_products_property_returns_empty_string_when_no_products():
    """Если в категории нет товаров — возвращается пустая строка."""
    category = Category(name="Пустая категория", description="Пока ничего нет")

    assert category.products == ""


def test_products_property_formats_single_product_correctly():
    """Проверка формата для одного продукта."""
    p = Product("Банан", "Фрукт", 50.0, 10)
    category = Category(name="Фрукты", description="Сочные фрукты")
    category.add_product(p)

    expected = "Банан, 50.0 руб. Остаток: 10 шт."
    assert category.products == expected


def test_products_property_formats_multiple_products_with_newlines():
    """Для нескольких продуктов строки должны быть разделены переносом."""
    p1 = Product("Огурец", "Овощ", 100.0, 5)
    p2 = Product("Помидор", "Овощ", 80.0, 3)

    category = Category(name="Овощи", description="Свежие овощи")
    category.add_product(p1)
    category.add_product(p2)

    expected = (
        "Огурец, 100.0 руб. Остаток: 5 шт.\n"
        "Помидор, 80.0 руб. Остаток: 3 шт."
    )

    assert category.products == expected


def test_products_property_order_matches_addition_order():
    """Порядок товаров в строке должен соответствовать порядку добавления."""
    p1 = Product("А", "Тест", 10.0, 1)
    p2 = Product("Б", "Тест", 20.0, 2)
    p3 = Product("В", "Тест", 30.0, 3)

    category = Category(name="Алфавит", description="По порядку")
    category.add_product(p1)
    category.add_product(p3)
    category.add_product(p2)

    lines = category.products.split("\n")
    assert lines[0] == "А, 10.0 руб. Остаток: 1 шт."
    assert lines[1] == "В, 30.0 руб. Остаток: 3 шт."
    assert lines[2] == "Б, 20.0 руб. Остаток: 2 шт."


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


def test_middle_price_returns_correct_average():
    p1 = Product("Огурец", "Овощ", 100.0, 5)
    p2 = Product("Банан", "Фрукт", 50.0, 10)
    p3 = Product("Помидор", "Овощ", 80.0, 3)

    category = Category(name="Овощи и фрукты", description="Свежие продукты")

    category.add_product(p1)
    category.add_product(p2)
    category.add_product(p3)

    result = category.middle_price()
    expected = (100.0 + 50.0 + 80.0) / 3
    assert result == expected


def test_middle_price_returns_zero_when_no_products():
    category = Category(name="Пустая категория", description="Пока ничего нет")
    assert category.middle_price() == 0


def test_middle_price_handles_single_product():
    p = Product("Авокадо", "Фрукт", 200.0, 2)
    category = Category(name="Экзотика", description="Редкие фрукты")
    category.add_product(p)

    assert category.middle_price() == 200.0


def test_middle_price_with_float_precision():
    p1 = Product("Чай", "Напиток", 99.99, 1)
    p2 = Product("Кофе", "Напиток", 100.01, 1)
    category = Category(name="Напитки", description="Горячие и холодные")
    category.add_product(p1)
    category.add_product(p2)

    result = category.middle_price()
    expected = (99.99 + 100.01) / 2
    assert abs(result - expected) < 1e-9


import pytest
from src.oop_class import Product, Category, BaseProduct


def test_cannot_instantiate_base_product():
    """Абстрактный класс нельзя создать напрямую."""
    with pytest.raises(TypeError) as exc_info:
        BaseProduct("Огурец", "Овощ", 100.0, 5)
    # В сообщении будет что-то вроде "Can't instantiate abstract class..."
    assert "abstract" in str(exc_info.value).lower()


def test_product_rejects_zero_quantity_on_init():
    """quantity == 0 должен вызывать ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Product("Огурец", "Овощ", 100.0, 0)
    assert "Товар с нулевым количеством" in str(exc_info.value)


def test_price_setter_rejects_negative():
    p = Product("Огурец", "Овощ", 100.0, 5)
    old_price = p.price
    p.price = -10.0
    assert p.price == old_price  # цена не изменилась


def test_category_product_count_no_double_counting():
    """
    Важно: product_count не должен учитывать товары дважды:
    - при создании Category с products
    - и потом при add_product.
    """
    p1 = Product("Огурец", "Овощ", 100.0, 5)
    p2 = Product("Банан", "Фрукт", 50.0, 10)

    initial_count = Category.product_count

    category = Category(name="Фрукты", description="Разные", products=[p1, p2])
    # Внутри __init__ уже добавили 2 к счётчику
    assert Category.product_count == initial_count + 2

    category.add_product(p1)  # добавляем ещё один (тот же самый объект)
    assert Category.product_count == initial_count + 3

    # Если бы было двойное суммирование в add_product, было бы +4, но у нас логика верная.


def test_new_product_updates_price_only_if_higher():
    """new_product обновляет цену только если новая цена больше текущей."""
    p = Product("Огурец", "Овощ", 100.0, 5)
    products_list = [p]

    # Новая цена меньше — не должна обновиться
    result = Product.new_product({"name": "Огурец", "price": 80.0, "quantity": 3}, products_list)
    assert result is p
    assert p.price == 100.0  # цена осталась прежней
    assert p.quantity == 8  # количество всё равно суммируется

    # Новая цена больше — должна обновиться
    result2 = Product.new_product({"name": "Огурец", "price": 120.0, "quantity": 2}, products_list)
    assert result2 is p
    assert p.price == 120.0
    assert p.quantity == 10


def test_new_product_handles_string_numbers():
    """new_product должен корректно обрабатывать строки в price/quantity."""
    products_list = []
    data = {"name": "Помидор", "price": "80.5", "quantity": "3"}
    result = Product.new_product(data, products_list)

    assert len(products_list) == 1
    assert result.price == 80.5
    assert result.quantity == 3


def test_new_product_missing_description_uses_empty():
    products_list = []
    data = {"name": "Яблоко", "price": 50.0, "quantity": 4}  # нет description
    result = Product.new_product(data, products_list)

    assert result.description == ""


def test_middle_price_with_large_numbers_no_overflow():
    """middle_price должен работать и с большими числами (float справляется)."""
    huge_price = 1e12
    p1 = Product("Супер-товар", "Редкий", huge_price, 1)
    p2 = Product("Ещё дороже", "Очень редкий", huge_price * 2, 1)

    category = Category("Дорогие товары", "Очень дорогие")
    category.add_product(p1)
    category.add_product(p2)

    avg = category.middle_price()
    expected = (huge_price + huge_price * 2) / 2
    assert abs(avg - expected) < 1e-9


def test_add_with_non_product_returns_type_error_or_none():
    """Проверяем поведение __add__ с неподходящим типом.

    У тебя сейчас:
      - если isinstance(other, Product) -> сумма
      - иначе -> ничего не возвращает (None), но есть try/except, который печатает.
    """
    p = Product("Огурец", "Овощ", 100.0, 5)
    result = p + "не продукт"
    assert result is None  # либо проверяй, что TypeError не выброшен, а возвращён None


def test_str_representation_of_product():
    p = Product("Огурец", "Овощ", 100.0, 5)
    expected = "Огурец, 100.0 руб. Остаток: 5 шт."
    assert str(p) == expected


def test_str_representation_of_category_with_products():
    p1 = Product("Огурец", "Овощ", 100.0, 5)
    p2 = Product("Банан", "Фрукт", 50.0, 10)
    category = Category("Фрукты", "Разные", [p1, p2])

    total_qty = p1.quantity + p2.quantity
    expected = f"Фрукты, количество продуктов: {total_qty} шт."
    assert str(category) == expected


def test_str_representation_of_empty_category():
    category = Category("Пустая", "Ничего нет")
    expected = "Пустая, количество продуктов: 0 шт."
    assert str(category) == expected
