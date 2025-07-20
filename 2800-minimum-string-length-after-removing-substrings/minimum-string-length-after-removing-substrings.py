class Solution:
    def minLength(self, s: str) -> int:
        # parameters:
        # string of uppercase characters
        # we can remove 'AB' or 'CD' in one operation
        # return 
        # minimum possible length of the resulting string
        # example:
        # 'AEFGBCDS'
        # 'AEFGBS'
        #use a stack to add the characters
        # if there is nothing in the stack add first character
        #  if the current character and the previous character in the stack are AB pop the last character from stack
        #  if current charaacter and previous characte in stack are CD pop the last character from stack
        #  otherwise, add to stack
        # return len of stack

        stack = []
        for chr in s:

            if not stack:
                stack.append(chr)
                continue

            if  stack[-1] == 'A' and chr == 'B':
                stack.pop()
            elif stack[-1] == 'C' and chr == 'D':
                stack.pop()
            else:
                stack.append(chr)

        return len(stack)
        
