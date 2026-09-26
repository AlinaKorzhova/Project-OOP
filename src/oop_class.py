class Product:
    """"""
    name: str
    description: str
    price: float
    quantity :str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    total_categories = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1


if __name__ == "__main__":
    product1 = Product("Огурец", "Овощ", 100.0, 5)
    product2 = Product("Банан", "Фрукт", 50.0, 10)

    category = Category("Фрукты", "Разные фрукты")
    category.products.append(product1)
    category.products.append(product2)

    # Теперь ты можешь проверить список продуктов в категории
    for product in category.products:
        print(
            f"Название продукта: {product.name}, Описание: {product.description}, Цена: {product.price}, Количество: {product.quantity}")
