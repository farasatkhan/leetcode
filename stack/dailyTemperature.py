from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            # Iterate through the temperatures list along with their indices
            while stack and temperature > stack[-1][1]:
                # While the stack is not empty and the current temperature is greater
                # than the temperature at the top of the stack, update the result
                stackI, stackT = stack.pop()  # Get the index and temperature from the stack
                res[stackI] = index - stackI  # Update the result at the index with days to warmer temperature

            # Push the current temperature and its index onto the stack
            stack.append([index, temperature])

        return res
