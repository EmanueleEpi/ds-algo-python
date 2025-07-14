from week_00_bootup.singly_linked_list import SinglyLinkedList


def test_linked_list():
    ll = SinglyLinkedList()
    assert repr(ll) == "Empty"
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert repr(ll) == "1 -> 2 -> 3"
    ll.prepend(0)
    assert repr(ll) == "0 -> 1 -> 2 -> 3"
    ll.delete(2)
    assert repr(ll) == "0 -> 1 -> 3"
    ll.reverse()
    assert repr(ll) == "3 -> 1 -> 0"
