import merge_two_sorted_lists
from singly_linked_list import LinkedList
from singly_linked_list import Node

def print_list(list: Node):
    current = list
    print("[", end = " ")
    while(current):
        print(str(current.data), end = " ")
        current = current.next
        if(current):
            print(", ", end = " ")
    print("]", end = " ")

def test(list1: Node, list2: Node, output: Node):
    print("Input: list1 = ", end = " ")
    print_list(list1)
    print(", list2 = ", end = " ")
    print_list(list2)
    
    print("\nOutput: ", end = " ")
    print_list(output)
    print("\n")

    result = merge_two_sorted_lists.merge_two_sorted_lists(list1, list2)

    while result and output:
        assert result.data == output.data
        result = result.next
        output = output.next

def main():
    list1 = LinkedList()
    list1.push(4)
    list1.push(2)
    list1.push(1)
    list2 = LinkedList()
    list2.push(4)
    list2.push(3)
    list2.push(1)
    output = LinkedList()
    output.push(4)
    output.push(4)
    output.push(3)
    output.push(2)
    output.push(1)
    output.push(1)
    test(list1.head, list2.head, output.head)

    list1 = LinkedList()
    list2 = LinkedList()
    output = LinkedList()
    test(list1.head, list2.head, output.head)

    list1 = LinkedList()
    list2 = LinkedList()
    list1.push(0)
    output = LinkedList()
    output.push(0)
    test(list1.head, list2.head, output.head)


if __name__ == "__main__":
    main()