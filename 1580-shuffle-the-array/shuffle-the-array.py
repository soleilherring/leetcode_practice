class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        '''
        PREP
        parameters = int list and n (*2, is the length of the list)
        return: updated list 
        example: [2,5,1,3,4,7] ->[2,3,5,4,1,7]; [1] -> [1], 
        pseudocode:
        1. result array
        3. for i in range(n)
            a. first append the first 0th postion
            b. append starting from n
        return the result array
        '''
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])
        return result