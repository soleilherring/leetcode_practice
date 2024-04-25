class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers approach
        # make pointers
        left = 0
        right = len(numbers) -1
        current_sum = 0

        while left < right:
            # check if target is less than current sum
            current_sum = numbers[left] + numbers[right]

            # check if current_sum == target:
            if current_sum == target:
                return [left + 1, right +1 ]
            # if current sum is less than the target, we need to make left a bigger number
            if current_sum < target:
                left +=1
            else:
                # else, if current sum is greater than the target, we need to make the right a smaller number
                right -=1
        