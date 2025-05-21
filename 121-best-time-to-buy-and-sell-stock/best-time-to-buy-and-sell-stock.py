class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find min and max, max - min max is winner
        '''
        PREP
        parameters:
        int prices list
        return:
        int maximum profit
        if no profit, return 0 
        example:
        [7,1,5,3,6,4] -> 5 
        [7,4,2,1] -> 0 
        pseuodocode:
        1. 
        make a minimum price variable:
            minimum_price = prices[0]
        2. 
        make a maximum price so far variable:
            maximum_price = 0 

        3. two pointers
        left and right
        - left will be minmum and 
        - right for loop
            -calculate right - minimum 
            - compare the max to the current calcuation, if it is larger, that becomes t
            the new max
            - minimum, compare the current minimum with the current element, if it is smaller, that is
            the new minimum
            return the max
        '''

        min_price = prices[0]
        max_profit = 0

        for r in range(1,len(prices)):
            current_profit = prices[r] - min_price
            if current_profit > max_profit:
                max_profit = current_profit
            if prices[r] < min_price:
                min_price = prices[r]
        return max_profit