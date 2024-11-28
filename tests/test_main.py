import pytest
from main_14 import Category, Product, Mixin, Smartphone, LawnGrass

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
    assert product.price == 200000.0  # Price should not change


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

    assert "Ожидается объект типа Product, а получен str" in str(excinfo.value)
    assert len(category.products) == 2
    assert Category.product_count == initial_product_count


def test_add_inherited_product_to_category(category):
    class TestProduct(Product, Mixin):  # Inheriting from Mixin to show the creation print
        pass

    inherited_product = TestProduct("Новый продукт", "Тестовое описание", 50000.0, 10)
    initial_product_count = Category.product_count

    category.add_product(inherited_product)

    assert len(category.products) == 3
    assert Category.product_count == initial_product_count + 1
    assert f"{inherited_product.name}, {inherited_product.price} руб. Остаток: {inherited_product.quantity} шт." in category.products


def test_product_init_and_str():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_category_init_and_str():
    category = Category("Test Category", "Test Description", [])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == []
    assert str(category) == "Test Category, количество продуктов: 0 шт."


def test_middle_price(category):
    middle_price = category.middle_price()
    assert middle_price == 195000.0


def test_smartphone_init():
    smartphone = Smartphone("Test Smartphone", "Test Description", 100.0, 10, "High", "Model X", "128GB", "Black")
    assert smartphone.name == "Test Smartphone"
    assert smartphone.description == "Test Description"
    assert smartphone.price == 100.0
    assert smartphone.quantity == 10
    assert smartphone.efficiency == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == "128GB"
    assert smartphone.color == "Black"


def test_smartphone_repr():
    smartphone = Smartphone("Test Smartphone", "Test Description", 100.0, 10, "High", "Model X", "128GB", "Black")
    assert repr(smartphone) == "Smartphone(name='Test Smartphone', description='Test Description', " \
                               "price=100.0, quantity=10, efficiency='High', model='Model X', memory='128GB', color='Black')"


def test_smartphone_add():
    smartphone1 = Smartphone("Test Smartphone 1", "Test Description 1", 100.0, 5, "High", "Model X", "128GB", "Black")
    smartphone2 = Smartphone("Test Smartphone 2", "Test Description 2", 200.0, 3, "Medium", "Model Y", "256GB", "White")
    total_cost = smartphone1 + smartphone2
    assert total_cost == 1100.0


def test_smartphone_add_invalid():
    smartphone = Smartphone("Test Smartphone", "Test Description", 100.0, 10, "High", "Model X", "128GB", "Black")
    product = Product("Test Product", "Test Description", 50.0, 5)

    with pytest.raises(TypeError) as excinfo:
        _ = smartphone + product

    assert "Нельзя сложить продукты разных типов: Smartphone и Product" in str(excinfo.value)


def test_lawngrass_init():
    lawngrass = LawnGrass("Test LawnGrass", "Test Description", 50.0, 20, "USA", "7-10 days", "Green")
    assert lawngrass.name == "Test LawnGrass"
    assert lawngrass.description == "Test Description"
    assert lawngrass.price == 50.0
    assert lawngrass.quantity == 20
    assert lawngrass.country == "USA"
    assert lawngrass.germination_period == "7-10 days"
    assert lawngrass.color == "Green"


def test_lawngrass_str():
    lawngrass = LawnGrass("Test LawnGrass", "Test Description", 50.0, 20, "USA", "7-10 days", "Green")
    assert str(lawngrass) == "Test LawnGrass, 50.0 руб. Остаток: 20 шт."


def test_lawngrass_add():
    lawngrass1 = LawnGrass("Test LawnGrass 1", "Test Description 1", 50.0, 10, "USA", "7-10 days", "Green")
    lawngrass2 = LawnGrass("Test LawnGrass 2", "Test Description 2", 60.0, 5, "Canada", "5-7 days", "Dark Green")
    total_cost = lawngrass1 + lawngrass2
    assert total_cost == 800.0


def test_lawngrass_add_invalid():
    lawngrass = LawnGrass("Test LawnGrass", "Test Description", 50.0, 10, "USA", "7-10 days", "Green")
    product = Product("Test Product", "Test Description", 30.0, 5)

    with pytest.raises(TypeError) as excinfo:
        _ = lawngrass + product

    assert "Нельзя сложить продукты разных типов: LawnGrass и Product" in str(excinfo.value)