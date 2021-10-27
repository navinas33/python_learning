print('Hello Navin..')
a = 1
b = 56
navin = {1: 67}
text = 'Apple'
print(text[1:-2])
print(text[-2])
formatted_text = f'This is {text}'
print(formatted_text)
formatted = 'This is {} and {}'.format(text, text)
print(formatted)
print('--------------------------------------')

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print('Even numbers count', count)


def greet():
    print('Welcome')


greet()


def fizz_buzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return 'FizzBuzz'
    if value % 3 == 0:
        return 'Fizz'
    if value % 5 == 0:
        return 'Buzz'
    return value


print(fizz_buzz(value=15))


def swap(x, y):
    return y, x


x = 10
y = 11
print(f'Before Swap Value : {x} and {y}')
x, y = swap(x, y)  # or simple x. y = y, x  ( does the same )
print(f'After Swap Value : {x} and {y}')

# frequency of char in string
value = 'NaviNii'

characters_dict = dict()

for char in value:
    if char in characters_dict:
        characters_dict[char] = characters_dict[char] + 1
    else:
        characters_dict[char] = 1

final_char = ''
previous_value = 0

for key, dict_value in characters_dict.items():
    if dict_value > previous_value:
        final_char = key
    previous_value = dict_value

print(characters_dict)
print(final_char)

# get frequency of char in string

value = 'NaviNii'

characters_dict = dict()

for char in value:
    if char in characters_dict:
        characters_dict[char] = characters_dict[char] + 1
    else:
        characters_dict[char] = 1

sorted_array = sorted(characters_dict.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_array)
print(sorted_array[0])
print(*sorted_array[0])


class Product:
    class_variable = 12

    def __init__(self, price):
        self.price = price

    @classmethod
    def class_method(cls):
        cls.class_variable = 110

    def __hide_method(self):
        print("Hiding this method")

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


product = Product(10)
print(product)
print(product.price)
print(product.class_variable)
print(product.class_method())
print(product.class_variable)
print(Product.class_variable)

print(product.get_price())
product.set_price(-12)
print(product.get_price())


# print(product.__hide_method())


class NavDict:
    def __init__(self):
        self.values = {}

    def add(self, key, value):
        self.values[key] = value

    def get(self, key):
        return self.values.get(key)

    def update(self, key, value):
        self.values[key] = value

    def remove(self, key):
        del self.values[key]

    def __str__(self):
        return f'{self.values}'


nav_dict = NavDict()
print(nav_dict)
nav_dict.add('firstName', 'Navin')
print(nav_dict)
nav_dict.add('secondName', 'kumar')
print(nav_dict)
nav_dict.add('age', 25)
print(nav_dict)
nav_dict.add('dummy', 25)
print(nav_dict)
nav_dict.update('dummy', 45)
print(nav_dict)
print(nav_dict.get('firstName'))
print(nav_dict.get('FirstName'))
nav_dict.remove('dummy')
print(nav_dict)


class New_Dict:
    def __init__(self):
        self.__tags = {}

    def add(self, key, value):
        self.__tags[key] = value

    def __getitem__(self, item):
        return self.__tags.get(item)

    def __setitem__(self, key, value):
        self.__tags[key] = value

    def __delitem__(self, key):
        del self.__tags[key]

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        iter(self.__tags)

    def __str__(self):
        return f'{self.__tags}'


new_dict = New_Dict()
print(new_dict)
new_dict['name'] = 'Navin'
print(new_dict)
print(new_dict['name'])
print(new_dict['navin'])
new_dict['dummy'] = 123
print(new_dict)
del new_dict['dummy']
print(new_dict)

# print(new_dict.__tags['test'])

print(new_dict.__dict__)  # get all fileds in class
print(new_dict._New_Dict__tags)  # access private fields
