class Queue:
    def __init__(self):
        self._data: list[int] = []

    def enqueue(self, val: int) -> None:
        self._data.append(val)

    def dequeue(self) -> int | None:
        if self._data:
            return self._data.pop(0)
        return None

    def peek(self) -> int | None:
        if self._data:
            return self._data[0]
        return None

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({self._data})"
