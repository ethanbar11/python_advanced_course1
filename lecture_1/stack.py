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

    def __add__(self, other):
        new_stack = Stack()
        new_stack.lst += self.lst + other.lst

    def __eq__(self, other):
        if len(self.lst) != len(other.lst):
            return False

        for i, item in enumerate(self.lst):
            if item != other.lst[i]:
                return False
        return True

    def __len__(self):
        return len(self.lst)


def validate_sentence(sentence):
    stack = Stack()
    bracelets = {'{': '}', '(': ')', '[': ']'}
    for s in sentence:
        if s in bracelets.values() or s in bracelets.keys():
            # If i'm here- it means that s is a bracelet.
            if s in bracelets.keys():
                # If I'm here it means that it opens
                stack.push(s)
            if s in bracelets.values():
                # If I'm here it means that it closes
                if len(stack) == 0:
                    return False
                opening_bracelet = stack.pop()
                if bracelets[opening_bracelet] != s:
                    return False
    # There are still more opening bracelets but no closings.
    if len(stack) > 0:
        return False
    return True


stack = Stack()
stack.push('a')
stack.push('b')
print(stack.pop())

# print(validate_sentence('[([)]]'))
