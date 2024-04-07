class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

class EmptyNodeError(Exception):
    pass

def alternating_split(head):
    if head is None or head.next is None:
        raise EmptyNodeError

    odd_node = odd_head = Node()
    even_node = even_head = Node()

    current_head = head
    index = 1

    while current_head is not None:
        if index % 2:
            odd_node.next = Node(current_head.data)
            odd_node = odd_node.next
        else:
            even_node.next = Node(current_head.data)
            even_node = even_node.next

        current_head = current_head.next
        index += 1

    return Context(odd_head.next, even_head.next)
