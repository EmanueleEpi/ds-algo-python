class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def append(self, val):
        if self._size == self._capacity:
            self._resize()
        self._data[self._size] = val
        self._size += 1

    def _resize(self):
        self._capacity *= 2
        new_data = [None] * self._capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def __getitem__(self, index):
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError("Index out of bounds")

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"DynamicArray({[self._data[i] for i in range(self._size)]})"
