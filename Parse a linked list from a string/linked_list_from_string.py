class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s, index = 0):
    values = s.split(' -> ')
    new_values = [int(elm) if elm != 'None' else None for elm in values]
    current_elm = new_values[index]

    if current_elm is None:
        return None

    return Node(data=current_elm, next=linked_list_from_string(s, index + 1))
