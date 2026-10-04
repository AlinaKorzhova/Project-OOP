class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
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
    name: str
    description: str
    products: list
    total_categories = 0  # счетчик категорий
    total_product = 0  # счетчик товаров

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

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

    # Создаём категорию и добавляем товары в неё
    category = Category("Фрукты", "Разные фрукты")
    category.add_product(product1)  # можно и в «Фрукты», логика не строгая, главное — в категорию
    category.add_product(product2)
    category.add_product(product3)
    category.add_product(product4)

    print(category.name)
    print(category.description)
    print("Всего категорий:", Category.total_categories)
    print("Всего товаров:", Category.total_product)
    print("\nТовары в категории:\n", category.products)
