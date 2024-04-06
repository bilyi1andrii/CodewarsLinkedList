class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data, copy_node = None):
    if head is None:
        return Node(data)

    if head.data > data:
        new_node = Node(data)
        new_node.next = head
        return new_node

    if copy_node is None:
        copy_node = Node(head.data)
    else:
        new_copy_node = Node(head.data)
        new_copy_node.next = copy_node
        copy_node = new_copy_node

    second_half = sorted_insert(head.next, data, copy_node)

    if copy_node is None:
        return second_half
    copy_node.next = second_half
    return copy_node
