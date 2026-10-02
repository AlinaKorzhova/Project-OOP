class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None) -> None:
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)

    @classmethod
    def total_products(cls) -> int:
        return cls.product_count


if __name__ == "__main__":
    product1 = Product("Огурец", "Овощ", 100.0, 5)
    product2 = Product("Банан", "Фрукт", 50.0, 10)

    category = Category("Фрукты", "Разные фрукты", [product1, product2])

    print(Category.total_products())

    for product in category.products:
        print(
            f"Название продукта: {product.name}, Описание: {product.description}, "
            f"Цена: {product.price}, Количество: {product.quantity}"
        )
