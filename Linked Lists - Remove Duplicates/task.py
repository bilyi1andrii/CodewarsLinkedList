class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def remove_duplicates(head):
    if head is None:
        return None

    seen = {}
    current = head
    prev = None

    while current is not None:
        if current.data in seen:
            prev.next = current.next
        else:
            seen[current.data] = True
            prev = current
        current = current.next

    return head

