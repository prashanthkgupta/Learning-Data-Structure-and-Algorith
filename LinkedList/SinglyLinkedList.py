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


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.length = 0 if node is None else 1

    def list(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # def length(self):
    #     count = 0
    #     cur = self.head
    #     while cur is not None:
    #         count += 1
    #         cur = cur.next
    #     return count

    def insert_at_the_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_the_end(self, data):
        self.length += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def insert_at_the_middle(self, position, data):
        if position > self.length + 1 or position < 0:
            raise Exception('Invalid Position Parameter')  # test
        else:
            if position == 1:
                self.insert_at_the_beginning(data)
            elif position == self.length + 1:
                self.insert_at_the_end(data)
            else:
                position -= 2
                cur = self.head
                new_node = Node(data)
                while position != 0:
                    cur = cur.next
                    position -= 1
                new_node.next = cur.next
                cur.next = new_node
                self.length += 1

    def delete_at_the_beginning(self):
        if self.length == 0:
            raise Exception('No Elements in the List')
        else:
            self.length -= 1
            self.head = self.head.next

    def delete_at_the_end(self):
        if self.length == 0:
            raise Exception('No Elements in the List')
        else:
            cur = self.head
            if self.length == 1:
                self.head = None
            else:
                prev = cur
                cur = cur.next
                while cur.next is not None:
                    prev = cur
                    cur = cur.next
                prev.next = None
            self.length -= 1

    def del_at_the_middle(self, position):
        if self.length == 0:
            raise Exception('No Elements in the List')
        elif position > self.length:
            raise Exception('Invalid position for the list')
        else:
            if position == 1:
                self.delete_at_the_beginning()
            elif position == self.length:
                self.delete_at_the_end()
            else:
                cur = self.head
                counter = 2
                while counter < position:
                    counter += 1
                    cur = cur.next
                cur.next = cur.next.next
                self.length -= 1

    def clear(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_the_end(5)
    linked_list.insert_at_the_beginning(4)
    linked_list.insert_at_the_end(6)

    linked_list.insert_at_the_middle(1, 3)
    linked_list.insert_at_the_middle(5, 7)
    linked_list.insert_at_the_middle(2, 77)

    linked_list.delete_at_the_beginning()
    linked_list.delete_at_the_end()
    linked_list.del_at_the_middle(4)

    linked_list.list()
