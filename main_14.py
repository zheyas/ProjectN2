from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        # Update static counters
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.products.append(product)
        Category.product_count += 1


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации,"
                         " но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром,"
                         " станет вашим другом и помощником",
                         [product4])

    # Outputs
    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(Category.category_count)
    print(Category.product_count)

    # Adding a new product to category2
    product5 = Product("Sony Bravia 55\"", "Высокое разрешение, 4K", 100000.0, 3)
    category2.add_product(product5)

    print(len(category2.products))
    print(Category.category_count)
    print(Category.product_count)
