class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class EmptyListError(Exception):
    pass

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise EmptyListError

    head = source.data
    new_source = source.next
    new_dest = Node(head)
    new_dest.next = dest

    return Context(new_source, new_dest)