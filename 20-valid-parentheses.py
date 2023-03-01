# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        brackets ={
            '[':']',
            '{':'}',
            '(':')'
        }

    # example: 
        if len(s) %2:
            return False
        # "()[]{}"
        stack = []
        for bracket in s:
            #  check if that bracket is in brackets
            if bracket in brackets:
                stack.append(bracket) #[ '(']
            elif not stack and brackets[stack.pop()] != bracket:
                # [] and brackets['('] != 
                return False
        return not stack 