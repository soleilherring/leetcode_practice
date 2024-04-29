class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointer method
        # get left and right pointer
        l = 0
        r = len(s) - 1

        # make a while loop to move through the array
        # while the left pointer is less than the right

        while l < r:
            # if the letter in the array is alphanumeric, then check when  it is lowercase. 
            # it the lowercase arent the same  then, return false. Otherwise, keep moving
            if s[l].isalnum() and s[r].isalnum():
                # check if when lowercase if they aren't the same, return false and leave loop
                if s[l].lower() != s[r].lower():
                    return False
                # otherwise, we want to keep moving through the array 
                l += 1
                r -= 1
            # else, if the left letter isn't alphanumeric, we want to move left over
            elif not s[l].isalnum():
                l += 1 
            # else, if the right letter isn't alphanmeric, we want to mover right over 
            else:
                r -= 1
        # if we have moved through the entire array and now the left and right are at same spot, 
        # we can return True because that means we have exited the loop
        return True 
