class Solution:
    def decodeString(self, s: str) -> str:
        # add the item to the stack
        # [3]
        # if it's a [ then add it to the stack
        # add a to the stack
        # if its a ] then weve reached the end of the stack
        # [  ']' 'a' '[' '3' ] -> [ '3', '[', 'a', ']']
        #     start popping out. ]
        #     a
        #     [
        #     3
        #     if it's a letter, append it to an array  and have the most recently popped go to the front
        #     'a'
        #     if number, multiply that letter or string by 'a'
        #     aaa
        #     add that back to the stack 
        #     [aaa] join the stack

        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                segment= ''
                while stack[-1] != '[':
                    removed = stack.pop()
                    segment = removed + segment 
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    new_num = stack.pop()
                    num = new_num + num 

                chunk = int(num) * segment
                stack.append(chunk)
                
        return ''.join(stack)
