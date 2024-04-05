def stringify(node):
    if node is None:
        return 'None'

    if node.next is None:
        return f'{node.data} -> None'

    return f"{node.data} -> " + stringify(node.next)