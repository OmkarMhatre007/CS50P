class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Jar capacity cannot be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot put negative cookies")
        if self.size + n > self.capacity:
            raise ValueError("More than capacity")
        self.size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot get negative cookies")
        if self.size < n:
            raise ValueError("Contain less cookies than you want")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity is wrong")
        if capacity < self.size:
            raise ValueError("Capacity can't be reduce")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Jar Overflowed")
        if size < 0:
            raise ValueError("Cookies cannot be negative")
        self._size = size
