from src.oop_class import Product


class Smartphone(Product):
    def __init__(self, name, model, memory, color, efficiency, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.memory = memory
        self.color = color
        self.efficiency = efficiency

    def __add__(self, other: Product) -> float | type[TypeError]:
        if type(other) is Smartphone:
            return self.total_cost() + other.total_cost()
        return TypeError


if __name__ == "__main__":
    smartphone_product1 = Smartphone("Samsung", "S10", 256, "Зеленый", 6, "Сматрфон", 60000.0, 5)
    smartphone_product2 = Smartphone("Samsung", "S20", 256, "Зеленый", 6, "Сматрфон", 70000.0, 5)
    print(smartphone_product1.name)
    print(smartphone_product1.model)
    print(smartphone_product1.memory)
    print(smartphone_product1.color)
    print(smartphone_product1.efficiency)
    print(smartphone_product1.description)
    print(smartphone_product1.price)
    print(smartphone_product1.quantity)

    print(smartphone_product1 + smartphone_product2)
