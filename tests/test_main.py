import pytest

from main_14 import Category, Product  # Замените 'main' на фактическое имя вашего файла


# Фикстура для создания продукта
@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


# Фикстура для создания категории
@pytest.fixture
def category(product):
    # Используем фикстуру product для создания объекта Category
    products = [product, Product("Iphone 15", "512GB, Gray space",
                                 210000.0, 8)]
    return Category("Смартфоны", "Описание категории", products)


def test_product_initialization(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(category):
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 2

    # Убедитесь, что статические счетчики правильно обновляются
    assert Category.category_count == 1
    assert Category.product_count == 2

    # Сброс счетчиков для качественного выполнения последующих тестов
    Category.category_count = 0
    Category.product_count = 0
