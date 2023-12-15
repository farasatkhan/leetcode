class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checks = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # Loop through each character in the input string 's'
        for char in s:
            if char in checks:
                if stack and stack[-1] == checks[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        # If the stack is empty, return True (indicating all brackets are properly matched)
        # Otherwise, return False (indicating there are unmatched brackets left)
        return True if not stack else False
    


valid_input="({[]})"
invalid_input="({[})"

s = Solution()
result = s.isValid(valid_input)
print(result)