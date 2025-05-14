from typing import List


class Stack():
    def __init__(self, size):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self) -> int:
        return self.stack.pop()
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack(len(tokens))
        for i in tokens:
            if i in "+-/*":
                r = stack.pop()
                l = stack.pop()
                if i == "+":
                    res = l+r
                elif i == "-":
                    res = l-r
                elif i == "*":
                    res = l*r
                elif i == "/":
                    res = int(l/r)
                
                stack.push(res)
            else:
                stack.push(int(i))
        return stack.pop()