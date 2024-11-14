class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        PREP
        parameters:
        int nums list
        return:
        int number, majority element in the array 
        example:
        [3,2,3] -> 3, because 3 appears more than half ot the time
        pseudocode:
        1. count variable = 0
        2. Start wiht the current majority which is the first numbewr
        3. increment the count if the majority is found again, otherwise, decrement count
        4. if count <=0, majority is the current number
        5. return majority
        '''
        count = 0
        majority = nums[0]

        for num in nums:
            if num != majority:
                count -= 1
                if count <= 0:
                    majority = num
                    count +=1
            else:
                count += 1
        return majority
        # [1,3,1,1,4,1,1,5,1,1,6,2,2]
        #                          n 
        #   count = 1
        #   majority = 1