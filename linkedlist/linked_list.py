"""Implements a basic LinkedList to create a LinkedList from a list of integers"""

class Node:
    def __init__(self, value):
        self.value = value  # required to create instance
        self.next = None    # initial value

def create_linked_list(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)  # set in first loop
            print("First node as head with tail pointing to i: ")
            print(head.value)       # head.next not set yet
            tail = head             # when there is 1 node the tail points to the head node
            print(tail.value)
        else:
            # initial head.next assigned from reference to it via tail.next
            print("Start else loop: ")
            tail.next = Node(value)     # starts being set on second loop and also assigned to head: they point to the same memory address
            print("Previous tail value: ", tail.value)
            print("Previous tail next: ", tail.next.value)
            tail = tail.next            # new tail created from previous tail.next
            print("New tail.value from previous tail.next: ", tail.value)

    return head


# Testing ...
input_list = [1, 2, 3, 4, 5, 6, 7]

# Testing
head = create_linked_list(input_list)
print("Head value: ", head.value, "Head.next.value: ", head.next.value)
