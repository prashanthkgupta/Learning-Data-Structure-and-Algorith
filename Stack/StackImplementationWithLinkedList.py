class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            raise Exception('Underflow')
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.is_empty():
            raise Exception('Underflow')
        return self.head.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())