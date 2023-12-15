class Solution:
    def __init__(self):
        # Initialize two stacks: one for values and one for tracking minimums
        self.stack = [] 
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Update the minimum value stack
        # If minStack is empty, set the current value as the minimum
        # Otherwise, update it with the minimum between the current value and the previous minimum
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def getTop(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]