from typing import List
from abc import ABC, abstractmethod

class Mixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # вызываем __init__ родительского класса
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        for key, value in self.__dict__.items():
            print(f"{key}: {repr(value)}")


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct, Mixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        else   :
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
        if not isinstance(product, Product):
            raise TypeError(f"Ожидается объект типа Product, а получен {type(product).__name__}")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[str]:
        return [f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт." for i in self.__products]

    @property
    def description(self) -> str:
        """Геттер для __description."""
        return self.__description

    def middle_price(self) -> float:

        try:
            total_pr = sum(product.price for product in self.__products)
            result = total_pr / len(self.__products)
            return (result)
        except ZeroDivisionError:
            print("Ошибка: деление на ноль!")
            return 0.0

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: str,
                 model: str, memory: str, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return f"{self.__class__.__name__}(name={repr(self.name)}, description={repr(self.description)}, " \
               f"price={self.price}, quantity={self.quantity}, efficiency={repr(self.efficiency)}, " \
               f"model={repr(self.model)}, memory={repr(self.memory)}, color={repr(self.color)})"
#isinstance(other, Smartphone)
    def __add__(self, other):
        if not (type(self).__name__ == type(other).__name__):
            raise TypeError(f"Нельзя сложить продукты разных типов: {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
#isinstance(other, LawnGrass)
    def __add__(self, other):
        if not (type(self).__name__ == type(other).__name__):
            raise TypeError(f"Нельзя сложить продукты разных типов: {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())