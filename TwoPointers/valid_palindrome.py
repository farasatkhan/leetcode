class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l points to the start of the string and r points to the end of the string
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while l < r and not self.isAlphaNumeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            # increment l by 1 and decrement r by 1
            l, r = l + 1, r - 1
            
        return True
    
    # Checking whether the character is alphanumeric
    def isAlphaNumeric(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))


# Create an object of the Solution class
sol = Solution()

# Define the test cases
test_cases = [
    ("A man, a plan, a canal, Panama", True),
    ("racecar", True),
    ("12321", True),
    ("hello world", False),
    ("", True),
    ("a", True),
    ("!@#$%^", True),
    ("Was it a car or a cat I saw?", True),
    ("Able was I ere I saw Elba", True),
    ("!!!", True)
]

# Run the test cases and print the results
for input_str, expected_output in test_cases:
    result = sol.isPalindrome(input_str)
    if result == expected_output:
        print(f"Test Passed: '{input_str}' is a palindrome: {result}")
    else:
        print(f"Test Failed: '{input_str}' is not a palindrome: {result}")