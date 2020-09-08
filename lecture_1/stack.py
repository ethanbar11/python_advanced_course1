def func(a):
    print(a)


class StackIterator:
    def __init__(self, stack):
        self.stack = stack
        self.i = 0

    def __next__(self):
        if len(self.stack.lst) > self.i:
            self.i += 1
            return self.stack.lst[self.i - 1]
        else:
            raise StopIteration()


class Stack:
    def __init__(self):
        self.lst = []

    def __iter__(self):
        return StackIterator(self)

    def push(self, x):
        self.lst.append(x)

    # This function returns none if stack is empty.
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            return None
            # return "Stack is empty!"

    def top(self):
        if not self.is_empty():
            return self.lst[-1]

    def is_empty(self):
        return len(self.lst) == 0


stack = Stack()
stack.push('a')
stack.push('b')
print(stack.pop())
