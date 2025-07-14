from week_00_bootup.stack import Stack


def test_stack():
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() is None
