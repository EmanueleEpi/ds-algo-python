class DynamicArray:
    """Minimal wrapper around Python list so we can practice custom methods."""

    def __init__(self):
        self._data: list[int] = []

    def append(self, val: int) -> None:
        self._data.append(val)

    def __len__(self) -> int:  # lets us call len(obj)
        return len(self._data)

    def __repr__(self) -> str:
        return f"DynamicArray({self._data})"
