from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.__opened = False

    def open(self):
        if self.__opened:
            raise InvalidOperationError('Stream is already opened')
        self.__opened = True

    def close(self):
        if not self.__opened:
            raise InvalidOperationError('Stream is already closed')
        self.__opened = False

    @abstractmethod
    def read(self):  # no implementation
        pass


class FileStream(Stream):
    def read(self):
        print('Reading stream using file')


class NetworkStream(Stream):
    def read(self):
        print('Reading stream using network')


# polymorphism
def poly_test(streams):
    for stream in streams:
        stream.open()
        stream.read()
        stream.close()


# possible to call stream directly if it is not abstract base class
# stream = Stream()
# stream.open()

file_stream = FileStream()
file_stream.open()
file_stream.read()
file_stream.close()

network_stream = NetworkStream()
network_stream.open()
network_stream.read()
network_stream.close()
poly_test([FileStream(), NetworkStream()])

from collections import namedtuple

# namedtupels are immutable , can't change member variable values
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=2, y=2)
print(p1.x)
print(p1 == p2)
print(p1 != p2)
print(p1 > p2)
print(p1 < p2)
print(id(p1))
print(id(p2))
# p1.x = 34  # AttributeError: can't set attribute
# update via
p1 = Point(x=34, y=67)
print(p1.x)
