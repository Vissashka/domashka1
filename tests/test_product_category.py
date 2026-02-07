import pytest
from src.models import Product, Category

@pytest.fixture
def sample_products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]

def test_product_attributes(sample_products):
    product = sample_products[0]
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_category_attributes(sample_products):
    category = Category("Смартфоны", "Модели современных устройств", sample_products[:2])
    assert hasattr(category, 'name'), "Объект Category не имеет атрибута 'name'"
    assert hasattr(category, 'description'), "Объект Category не имеет атрибута 'description'"
    assert hasattr(category, 'products'), "Объект Category не имеет атрибута 'products'"
    assert category.name == "Смартфоны"
    assert category.description == "Модели современных устройств"
    assert len(category.products) == 2  # Теперь должно быть ровно 2 элемента

def test_additional_category_and_product(sample_products):
    new_product = Product("55\" QLED 4K TV", "Фоновая подсветка, высокое разрешение", 123000.0, 7)
    second_category = Category("Телевизоры", "Современное телевидение", [new_product])
    assert second_category.name == "Телевизоры"
    assert len(second_category.products) == 1  # Должен быть ровно 1 элемент

def test_add_product_to_category(sample_products):
    category = Category("Электроника", "Различные устройства")
    first_product = sample_products[0]
    category.add_product(first_product)
    assert len(category.products) == 1  # Должен быть ровно 1 элемент


