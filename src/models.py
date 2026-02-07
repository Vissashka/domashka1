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
        self.__name = name  # Приватный атрибут названия
        self.__description = description  # Приватный атрибут описания
        self.__price = price  # Приватный атрибут цены
        self.__quantity = quantity  # Приватный атрибут количества

    # Свойства для приватных атрибутов (геттеры и сеттеры)

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Ошибка: цена не должна быть нулевой или отрицательной!")
        else:
            self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Количество товара не может быть отрицательным!")
        else:
            self.__quantity = value

    @staticmethod
    def validate_price(price):
        try:
            price_value = float(price)
            if price_value <= 0:
                raise ValueError("Цена должна быть положительной")
            return True
        except (ValueError, TypeError):
            return False

    @classmethod
    def new_product(cls, data, existing_products=None):
        """
        Класс-метод создает новый продукт или увеличивает количество у существующего товара.

        :param data: словарь с параметрами товара
        :param existing_products: список существующих объектов Product
        :return: объект типа Product
        """
        name = data['name']
        description = data['description']
        price = float(data['price'])
        quantity = int(data['quantity'])

        if existing_products is not None:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity  # Увеличение количества через сеттер
                    if product.price < price:
                        product.price = price  # Выбираем наибольшую цену
                    return product

        return cls(name, description, price, quantity)

    def __repr__(self):
        return f'Product({self.name}, {self.price}, {self.quantity})'



class Category:
    """Класс представляет собой категорию товаров."""

    def __init__(self):
        """
        Инициализирует категорию с пустым приватным списком товаров.
        """
        self.__products = []  # Приватный атрибут-список товаров

    def add_product(self, product):
        """
        Добавляет продукт в категорию.

        :param product: объект класса Product
        """
        self.__products.append(product)

    @property
    def products(self):
        """
        Возвращает представление списка товаров категории в удобной форме строки.
        """
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price:.2f} руб., остаток: {product.quantity}\n'
        return result[:-1]

    def __repr__(self):
        return f'Category(\n{self.products})\n'





