from week_00_bootup.min_heap import MinHeap


def test_min_heap():
    h = MinHeap()
    h.push(3)
    h.push(1)
    h.push(2)
    assert repr(h) == "MinHeap([1, 3, 2])" or repr(h) == "MinHeap([1, 2, 3])"
    assert h.pop() == 1
    assert h.peek() == 2
    assert len(h) == 2
