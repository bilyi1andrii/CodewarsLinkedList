class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

def reverse(head, index = 0, values = None):
    if head is None:
        return None

    def recursive_call(head, values):
        if values is None:
            values = []

        values.append(head.data)
        if head.next is None:
            return values[::-1]

        return recursive_call(head.next, values)


    if values is None:
        values = recursive_call(head, values) + [None]

    current_elm = values[index]

    if current_elm is None:
        return None

    return Node(data=current_elm, next=reverse(head, index + 1, values))
