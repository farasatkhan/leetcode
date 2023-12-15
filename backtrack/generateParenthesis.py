from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] 
        res = []

        def backtrack(openCount, closeCount):
            # Base case: If the count of open and close parenthesis reaches 'n',
            # a valid combination is formed, so add it to the result
            if openCount == closeCount == n:
                res.append("".join(stack))
                return res

            # If the count of open parenthesis is less than 'n', add an open parenthesis '('
            # and recursively call backtrack to explore further combinations
            if openCount < n:
                stack.append('(')
                backtrack(openCount + 1, closeCount)
                stack.pop()

            # If the count of close parenthesis is less than the count of open parenthesis,
            # add a close parenthesis ')' and recursively call backtrack to explore further combinations
            if closeCount < openCount:
                stack.append(')')
                backtrack(openCount, closeCount + 1)
                stack.pop()

        # Start the backtracking with counts of open and close parenthesis at 0
        backtrack(0, 0)

        return res
