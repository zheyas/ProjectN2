from typing import List

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, prod):
        name = prod["name"]
        description = prod["description"]
        price = prod["price"]
        quantity = prod["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price > 0:
            self.__price = price
        else:
            print('Цена должна быть больше нуля')


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.__description = description
        self.__products = products

        # Update static counters
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        # Подсчет общего количества товаров в категории
        total_quantity = sum(product.quantity for product in self.__products)
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[str]:
        return [f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт." for i in self.__products]


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))  # Покажет общее количество продуктов

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
