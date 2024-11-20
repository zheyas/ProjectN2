import pytest
from main_14 import Category, Product  # Замените 'main_14' на фактическое имя вашего файла


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category(product):
    products = [
        product,
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    ]
    return Category("Смартфоны", "Описание категории", products)


def test_new_product_creation():
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }
    new_product = Product.new_product(product_data)
    assert new_product.name == "Xiaomi Redmi Note 11"
    assert new_product.description == "1024GB, Синий"
    assert new_product.price == 31000.0
    assert new_product.quantity == 14


def test_set_and_get_price(product):
    product.price = 200000.0
    assert product.price == 200000.0

    product.price = -50000.0
    assert product.price == 200000.0  # Цена не изменилась


def test_add_product_to_category(category):
    initial_product_count = Category.product_count
    new_product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category.add_product(new_product)

    assert len(category.products) == 3
    assert Category.product_count == initial_product_count + 1


def test_get_products_format(category):
    product_list = category.products
    assert len(product_list) == 2
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in product_list
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in product_list


def test_category_total_quantity(category):
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_add_invalid_product_to_category(category):
    initial_product_count = Category.product_count

    with pytest.raises(TypeError) as excinfo:
        category.add_product("Not a product")

    assert "Так делать нельзя" in str(excinfo.value)
    assert len(category.products) == 2
    assert Category.product_count == initial_product_count


def test_add_inherited_product_to_category(category):
    class TestProduct(Product):
        pass

    inherited_product = TestProduct("Новый продукт", "Тестовое описание", 50000.0, 10)
    initial_product_count = Category.product_count

    category.add_product(inherited_product)

    assert len(category.products) == 3
    assert Category.product_count == initial_product_count + 1
    assert "Новый продукт, 50000.0 руб. Остаток: 10 шт." in category.products
