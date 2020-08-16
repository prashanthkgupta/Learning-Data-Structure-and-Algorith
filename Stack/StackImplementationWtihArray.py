class Stack:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.top = -1
        self.arr = [None] * capacity

    def is_full(self):
        return self.capacity == self.top + 1

    def is_empty(self):
        return self.top == -1

    def peek(self):
        if not self.is_empty():
            return self.arr[self.top]
        else:
            raise Exception('Underflow')

    def increase_size(self, size_multi=2):
        self.capacity *= size_multi
        temp = self.capacity * [None]
        if not temp:
            raise Exception('Use Bigger Machine')
        for i in range(self.top + 1):
            temp[i] = self.arr[i]
        self.arr = temp

    def decrease_size(self, size_dev=2):
        self.capacity //= size_dev
        temp = self.capacity * [None]
        for i in range(self.top + 1):
            temp[i] = self.arr[i]
        self.arr = temp

    def push(self, data):
        if self.is_full():
            self.increase_size()
        self.top += 1
        self.arr[self.top] = data

    def pop(self):
        if self.is_empty():
            raise Exception('Underflow')
        data = self.arr[self.top]
        self.top -= 1
        if self.top < self.capacity / 2:
            self.decrease_size()


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.is_empty())
    print(stack.is_full())
    print(stack.capacity)
    print(stack.peek())
