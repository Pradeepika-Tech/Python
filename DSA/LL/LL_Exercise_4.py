class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, value):
        if not self.head:
            return None
        a_list, b_list = Node(0), Node(0)
        prev_1, prev_2 = a_list, b_list
        temp = self.head
        while temp:
            if temp.value < value:
                prev_1.next = temp
                prev_1 = temp
            else:
                prev_2.next = temp
                prev_2 = temp
            temp = temp.next
        prev_1.next = None
        prev_2.next = None
        prev_1.next = b_list.next
        self.head = a_list.next


ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list()  # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list()  # Output: 3 2 1 5 8 10

