class Node:
    def __init__(self, nexto = None):
        self.next = nexto


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    prev = None
    current = head

    while current and current.next:
        next_pair_start = current.next.next
        next_pair_end = current.next

        current.next.next = current
        current.next = next_pair_start

        if prev:
            prev.next = next_pair_end
        else:
            head = next_pair_end

        prev = current
        current = next_pair_start

    return head
