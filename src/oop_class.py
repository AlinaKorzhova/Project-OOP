class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_dict: dict, list_product: list) -> "Product":
        name = product_dict["name"]
        price = float(product_dict["price"])
        quantity = int(product_dict["quantity"])

        for product in list_product:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                return product

        new_product = cls(
            name=name,
            description=product_dict.get("description", ""),
            price=price,
            quantity=quantity
        )
        list_product.append(new_product)
        return new_product

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def total_cost(self) -> float:
        return self.price * self.quantity

    def __add__(self, other: "Product") -> float | TypeError:
        try:
            if isinstance(other, Product):
                return self.total_cost() + other.total_cost()
        except TypeError:
            print("Можно складывать только объекты Product")


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @classmethod
    def total_products(cls) -> int:
        return cls.product_count

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("В категорию можно добавить только объект Product")

    @property
    def products(self) -> str:
        if not self.__products:
            return ""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    def __str__(self) -> str:
        count_products = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {count_products} шт."


if __name__ == "__main__":
    product1 = Product("Огурец", "Овощ", 100.0, 5)
    product2 = Product("Банан", "Фрукт", 50.0, 10)
    product3 = Product("Хлеб", "Хлебобулочные изделия", 60.0, 8)
    product4 = Product("Колбаса", "Мясное изделие", 500.0, 12)

    category = Category("Фрукты", "Разные фрукты", [product1, product2])
    category.add_product(product3)
    category.add_product(product4)

    print(Category.total_products())
    print("\nСписок товаров в категории:\n", category.products)
    print("\nСтроковое представление категории:", str(category))
