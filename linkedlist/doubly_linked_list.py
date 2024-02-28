class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head == None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next


"""Testing"""
# Create empty doubly linked list
linked_list = DoublyLinkedList()
# first element is head
linked_list.append(1)
# sets head.next via tail.next, set previous to head and set new tail as previous tail.next
linked_list.append(-2) 
# sets 2nd tail.next to 3rd value, sets previous to current tail, set current tail as tail.next 
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous
