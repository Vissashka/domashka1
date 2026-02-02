class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += sum(p.quantity for p in products)

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")  # Должно вывести True
    print(category1.description)
    print(len(category1.products))  # Проверка длины списка товаров
    print(category1.category_count)  # Категория первая создана
    print(category1.product_count)  # Сумма количеств товаров в первой категории

    product4 = Product("55\ QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))  # Товаров всего один
    print(category2.products)  # Прямо выводим сам продукт
    print(Category.category_count)  # Уже создано две категории
    print(Category.product_count)  # Теперь ещё семь единиц товара добавилось

from src.models import Product, Category
from utils import load_data_from_json  # Импортируем нашу функцию

# Имя файла с данными
filename = 'data.json'

# Загружаем данные из JSON-файла
categories = load_data_from_json(filename)

# Выводим данные на экран
for category in categories:
    print(f"КАТЕГОРИЯ: {category.name}")
    print(f"ОПИСАНИЕ: {category.description}\n")
    for product in category.products:
        print(f"\tНазвание: {product.name}")
        print(f"\tОписание: {product.description}")
        print(f"\tЦена: {product.price}")
        print(f"\tКоличество: {product.quantity}\n")


