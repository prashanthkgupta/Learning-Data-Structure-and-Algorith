class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def has_prev(self):
        return self.prev is not None

    def print(self):
        print('Node [data = %s ]' % self.data)


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0 if node is None else 1

    def insert_at_the_beginning(self, data):
        new_node = Node(data)
        if self.length != 0:
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def print_list(self, asc_order=True):
        if asc_order:
            cur = self.head
            while cur is not None:
                print(cur.data)
                cur = cur.next
        else:
            cur = self.tail
            while cur is not None:
                print(cur.data)
                cur = cur.prev


if __name__ == '__main__':
    d_list = DoublyLinkedList(Node(1))
    d_list.insert_at_the_beginning(2)
    d_list.insert_at_the_beginning(3)
    d_list.insert_at_the_beginning(4)
    d_list.insert_at_the_beginning(5)
    d_list.print_list(False)

