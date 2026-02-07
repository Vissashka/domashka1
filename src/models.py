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
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data):
        """Создает новый продукт на основе словаря."""
        name = data.get('name')
        description = data.get('description')
        price = float(data.get('price'))  # Конвертируем в число
        quantity = int(data.get('quantity'))  # Конвертируем в целое число
        return cls(name, description, price, quantity)

    @classmethod
    def new_product(cls, data, existing_products=None):
        """Создает новый продукт либо объединяет с существующими товарами."""
        if existing_products is not None:
            similar_product = next(
                (p for p in existing_products if p.name == data.get('name')), None
            )
            if similar_product:
                similar_product.quantity += int(data.get('quantity'))
                similar_product.price = max(similar_product.price, float(data.get('price')))
                return similar_product
        return cls.new_product(data)



    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой на допустимое значение."""
        if value <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной!")
        self._price = value

    @price.setter
    def price(self, value):
        """Сеттер для цены с дополнительной защитой при попытке снижения стоимости."""
        if value <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной!")
        elif value < self._price:
            answer = input(f'Вы пытаетесь снизить цену на "{self.name}". Продолжить? (y/n)')
            if answer.strip().lower() != 'y':
                print("Изменение цены отменено.")
                return
        self._price = value



class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self._products = products
        Category.category_count += 1
        # При создании категории суммируем начальное количество продуктов
        Category.product_count += sum(p.quantity for p in products)

    def add_product(self, product):
        """Добавляет продукт в категорию."""
        self._products.append(product)
        # Количество продуктов увеличивается только при добавлении
        Category.product_count += product.quantity

    @property
    def products(self):
        """Возвращает список продуктов."""
        return self._products



