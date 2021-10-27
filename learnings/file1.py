class Product:
    class_variable = 12

    def __init__(self, price):
        # self.set_price(price)
        self.price = price

    @classmethod
    def class_method(cls):
        cls.class_variable = 110

    def __hide_method(self):
        print("Hiding this method")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value

    # price = property(get_price, set_price)


# product = Product(-10)
product = Product(10)
print(product)
print(product.price)
# print(product.__price)
# product.__price = 10
print(product.class_variable)
print(product.class_method())
print(product.class_variable)
print(Product.class_variable)

# print(product.get_price())
# product.set_price()
# print(product.get_price())

product1 = Product(-10)
print(product1.price)
# product1.__price = -12
