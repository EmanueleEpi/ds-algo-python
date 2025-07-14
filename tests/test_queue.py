from week_00_bootup.queue import Queue


def test_queue():
    q = Queue()
    assert q.is_empty()
    q.enqueue(10)
    q.enqueue(20)
    assert q.peek() == 10
    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert q.dequeue() is None
