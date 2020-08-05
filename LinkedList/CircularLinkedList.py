class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def print(self):
        print('data = %d and next = %s' % (self.data, self.next))


class CirculerLinkedList:
    def __init__(self, node=None):
        self.head = node
        if node is not None:
            self.head.next = self.head

    def length(self):
        if self.head is None:
            return 0
        count = 1
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
            count += 1
        return count

    def list(self):
        if self.head is not None:
            cur = self.head
            while cur.next is not self.head:
                print(cur.data)
                cur = cur.next
            print(cur.data)

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            new_node.next = self.head
            cur.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            new_node.next = self.head
            cur.next = new_node
            self.head = new_node

    def delete_first(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                cur = self.head
                while cur.next is not self.head:
                    cur = cur.next
                cur.next = cur.next.next
                self.head = self.head.next

    def delete_last(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            elif self.head.next.next == self.head:
                self.head.next = self.head
            else:
                cur = self.head
                while cur.next.next is not self.head:
                    cur = cur.next
                cur.next = cur.next.next

    def clear(self):
        self.head = None


if __name__ == '__main__':
    cir_ll = CirculerLinkedList(Node(5))

    cir_ll.insert_at_last(1)
    cir_ll.insert_at_last(12)
    cir_ll.insert_at_last(13)
    cir_ll.insert_at_last(14)

    cir_ll.delete_last()
    cir_ll.delete_last()
    cir_ll.delete_last()
    cir_ll.delete_last()
    cir_ll.delete_last()

    cir_ll.list()
