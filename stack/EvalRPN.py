from typing import List

class Solution:
    def evalRPN(self, tokens: List[int]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b * a))
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        
        return stack[-1] if stack else -1