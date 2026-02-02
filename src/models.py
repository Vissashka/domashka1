class Product:
    """Класс описывает товар."""

    def __init__(self, name, description, price, quantity):
        """
        Инициализация объекта товара.

        :param name: наименование товара
        :param description: описание товара
        :param price: цена товара
        :param quantity: количество товара
        """
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

        # Назначаем атрибуты экземпляра
        self.name = name
        self.description = description
        self.products = products

        # Изменяем счётчики класса
        Category.category_count += 1
        Category.product_count += sum(p.quantity for p in products)


