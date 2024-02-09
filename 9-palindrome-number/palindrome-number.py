class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
           return False

        num = 0
        copy_x = x
        while copy_x > 0:
            remainder = copy_x %10 
            num = num * 10 + remainder
            copy_x //=10
        return x == num









        # input = x
        # new_num = 0
        # while x > 0: #121, 12,1, 
        #     new_num = new_num *10 + x %10  
        #     # 0 * 10 + 121 % 10 -> 0 + 1 = 1 
        #     # 1 *10 + 12%10-> 10+2= 12
        #     # 12 *10 + 1 %10 -> 120 +1 = 121
        #     x = x//10 
        #     #12
        #     #1
        #     # 0
        # return new_num == input