from singly_linked_list import Node

def merge_two_sorted_lists(list1: Node, list2: Node)->Node:
    dummy = Node()
    current = dummy

    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next
    