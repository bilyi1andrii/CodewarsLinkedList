class InvalidArgumentException(Exception):
    pass

def get_nth(node, index, current_index = 0):
    if index < 0 or node is None:
        raise InvalidArgumentException


    if current_index == index:
        return node
    return get_nth(node.next, index, current_index + 1)