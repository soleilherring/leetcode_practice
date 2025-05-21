class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary that counts the elements in the array
        # array that holds the index = number count, and the number placed there is the number with that count
        # go through the array backwards and get that number from the array up until it hits the kth number 


        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1 

        freq = [[] for num in range(len(nums)+1)]

        # add the number into the array in the correct position where the number is in the index(count) spot
        for num, frequency in num_count.items():
            freq[frequency].append(num)

        # iterate through the array backwards
        # start stop step
        # result array

        result = []
        for i in range(len(freq) -1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                        return result

