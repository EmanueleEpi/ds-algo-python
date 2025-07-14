class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Node | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None

    def append(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def delete(self, val: int) -> bool:
        if not self.head:
            return False
        if self.head.val == val:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next and curr.next.val != val:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
            return True
        return False

    def reverse(self) -> None:
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def __repr__(self) -> str:
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " -> ".join(nodes) if nodes else "Empty"
