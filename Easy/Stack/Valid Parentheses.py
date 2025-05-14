class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size

    # push
    def push(self, item):
        if self.isFull():
            print("Stack Is Full")
        else:
            self.stack.append(item)
    # pop
    def pop(self):
        if self.isEmpty():
            print("Nothing To Pop")
            return None
        else:
            return self.stack.pop(-1)
    # isEmpty
    def isEmpty(self):
        return len(self.stack) == 0
    # isFull
    def isFull(self):
        return len(self.stack) == self.size
    # Peek
    def peek(self):
        if self.isEmpty():
            return "Stack Is Empty"
        else:
            return self.stack[-1]
class Solution:
    def isValid(self, s: str) -> bool:
        str = s
        stack = Stack(len(str))
        match = {"}": "{", "]": "[", ")": "("}
        for i in str:
            if i in "{([":
                stack.push(i)
            elif i in "}])":
                top = stack.pop()
                if top != match[i]:
                    return False
        return stack.isEmpty()

