import numpy as np

array = np.array([2, 6, 0])
print(array)
print(array.shape)
print(type(array))

array_2d = np.array([[1, 2], [3, 4]])
print(array_2d)
print(array_2d.shape)
print(type(array_2d))

array = np.zeros((3, 4))
print('Zero array default is float\n', array)

array = np.zeros((3, 4), dtype=int)
print('Zero array with type int\n', array)

array = np.ones((3, 4), dtype=int)
print('One\'s array with type int\n', array)

array = np.full((3, 4), 5, dtype=int)
print('Numpy array with full as 5 type int \n', array)

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)  # all arithmetic operations are supported

# cert_wn1vc326


map = {}

map.keys()

list_cr = ['as', 'as3']

print(all(list_cr))
