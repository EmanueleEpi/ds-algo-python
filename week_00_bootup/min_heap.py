import heapq


class MinHeap:
    def __init__(self):
        self._data: list[int] = []

    def push(self, val: int) -> None:
        heapq.heappush(self._data, val)

    def pop(self) -> int | None:
        if self._data:
            return heapq.heappop(self._data)
        return None

    def peek(self) -> int | None:
        return self._data[0] if self._data else None

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"MinHeap({self._data})"
