# We have an array which is already sorted in non-decreasing order. 
# Return the indices of the two numbers when added together equals to the target.

class Solution:
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1

        while i < j:
            # if the sum is greater than the target, move the right pointer
            if numbers[i] + numbers[j] > target:
                j = j - 1
            # if the sum is less than the taget, move the left pointer
            elif numbers[i] + numbers[j] < target:
                i = i + 1
            else:
                # The indicies in the problem on leetcode is 1 based so we add 1 to it.
                return [i + 1, j + 1]
        return []


sol = Solution()

test_cases = [
    ([2, 7, 11, 15],    9,  [1, 2]),
    ([3, 5, 8, 11, 14], 8,  [1, 2]),
    ([1, 4, 6, 9, 12],  13, [1, 5]),
    ([1, 2, 3, 4, 5],   10, []),
    ([0, 1, 2, 3, 4],   0,  []),
    ([3, 3, 5, 7, 7],   10, [1, 5])
]

for numbers, target, expected_output in test_cases:
    result = sol.twoSum(numbers, target)
    if result == expected_output:
        print(f"Test Passed: {numbers}, Target: {target}, Result: {result}")
    else:
        print(f"Test Failed: {numbers}, Target: {target}, Expected: {expected_output}, Result: {result}")
