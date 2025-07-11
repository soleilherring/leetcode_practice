class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # parameters:
        # nums int list
        # k (window size)
        # return array of k most frequent int
        # 1. make a bucket array with sub arrays holding the places for length nums + 1 (becaue 0 will have no elements)
        # 2. make a dictionary that can hold the element and it's count as the value
        # 3. loop through the bucket and the index of the bucket will be the count for the num and the value will be an array at that spot
        # 4. iterate backwords and if there is a number get that and append to result array until the arry is of k size

        # make bucket array
        freq = [[] for _ in range(len(nums) + 1)]

        # make dictionary where key = nums, val = count of the num
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 0
            num_count[num] += 1

        # update the freq array
        # the index = count
        # the [num,] will be appended to the array
        for key, val in num_count.items():
            freq[val].append(key)
        print(freq)

        # iterate backwards and add to a result array the k most frequent elements  
        result = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                for num in freq[i]:
                    result.append(num)
                    if len(result) == k:
                        return result