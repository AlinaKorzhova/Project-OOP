class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_dict: dict, list_product: list):
        name = product_dict["name"],
        price = float(product_dict["price"],)
        quantity = int(product_dict["quantity"])

        for product in list_product:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                return product

        # если товар не найден создается новый объект
        new_product = cls(name=name, description=product_dict.get("description", ""), price=price, quantity=quantity)
        list_product.append(new_product)
        return new_product


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

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.total_product += 1

    @property  # геттер
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str


if __name__ == "__main__":
    product1 = Product("Огурец", "Овощ", 100.0, 5)
    product2 = Product("Банан", "Фрукт", 50.0, 10)
    product3 = Product("Хлеб", "Хлебобулочные изделия", 60.0, 8)
    product4 = Product("Колбаса", "Мясное  зделие", 500.0, 12)

    category = Category("Фрукты", "Разные фрукты", [product1, product2])

    print(Category.total_products())

    for product in category.products:
        print(
            f"Название продукта: {product.name}, Описание: {product.description}, "
            f"Цена: {product.price}, Количество: {product.quantity}"
        )
