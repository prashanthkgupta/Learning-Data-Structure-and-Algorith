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

    def insert_at_the_end(self, data):
        new_node = Node(data)
        if self.length != 0:
            new_node.prev = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def insert_at_the_middle(self, position, data):
        if position < 1 or position > self.length + 1:
            raise Exception('invalid position for the list')
        elif position == 1:
            self.insert_at_the_beginning(data)
        elif position == self.length + 1:
            self.insert_at_the_end(data)
        else:
            new_node = Node(data)
            cur = self.head
            cur_count = 2
            while position > cur_count:
                cur = cur.next
                cur_count += 1
            cur.next.prev = new_node
            new_node.next = cur.next
            cur.next = new_node
            new_node.prev = cur
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

    def delete_first(self):
        if self.length == 0:
            raise Exception('No nodes to get deleted')
        else:
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
            self.length -= 1

    def delete_last(self):
        if self.length == 0:
            raise Exception('No nodes to get deleted')
        else:
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            self.length -= 1

    def delete_at_middle(self, position):
        if position < 1 or position > self.length:
            raise Exception('There is not any node in the specified position')
        else:
            if position == 1:
                self.delete_first()
            elif position == self.length:
                self.delete_last()
            else:
                cur = self.head.next
                cur_count = 2
                while position > cur_count:
                    cur = cur.next
                    cur_count += 1
                cur.next.prev = cur.prev
                cur.prev.next = cur.next
                self.length -= 1


if __name__ == '__main__':
    d_list = DoublyLinkedList(Node(1))
    d_list.insert_at_the_beginning(2)
    d_list.insert_at_the_beginning(3)
    d_list.insert_at_the_beginning(4)
    d_list.insert_at_the_beginning(5)

    d_list.insert_at_the_end(13)
    d_list.insert_at_the_end(131)

    d_list.delete_last()
    d_list.delete_last()
    d_list.delete_last()

    d_list.delete_at_middle(2)
    d_list.delete_at_middle(2)
    # print(d_list.length)
    d_list.delete_at_middle(2)
    d_list.delete_at_middle(1)
    d_list.delete_at_middle(1)

    d_list.print_list()
