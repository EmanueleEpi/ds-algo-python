class Stack:
    def __init__(self):
        self._data: list[int] = []

    def push(self, val: int) -> None:
        self._data.append(val)

    def pop(self) -> int | None:
        if self._data:
            return self._data.pop()
        return None

    def peek(self) -> int | None:
        if self._data:
            return self._data[-1]
        return None

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"
