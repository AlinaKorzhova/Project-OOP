from src.oop_class import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Product) -> float | type[TypeError]:
        if type(other) is LawnGrass:
            return self.total_cost() + other.total_cost()
        return TypeError


if __name__ == "__main__":
    lawnglass_product1 = LawnGrass("Овес", "Зерновая культура", 10, 10000, "Россия", "30 дней", "Золотой")
    print(lawnglass_product1.name)
    print(lawnglass_product1.description)
    print(lawnglass_product1.price)
    print(lawnglass_product1.quantity)
    print(lawnglass_product1.country)
    print(lawnglass_product1.germination_period)
    print(lawnglass_product1.color)

    lawnglass_product2 = LawnGrass("Пшеница", "Зерновая культура", 11, 5000, "Россия", "30 дней", "Золотой")
    print(lawnglass_product1 + lawnglass_product2)