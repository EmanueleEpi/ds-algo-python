class HashMap:
    def __init__(self, size=10):
        self._buckets = [[] for _ in range(size)]
        self._size = size

    def _hash(self, key):
        return hash(key) % self._size

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, _) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx][i] = (key, value)
                return
        self._buckets[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return None

    def remove(self, key):
        idx = self._hash(key)
        self._buckets[idx] = [(k, v) for (k, v) in self._buckets[idx] if k != key]

    def __repr__(self):
        return str(self._buckets)
