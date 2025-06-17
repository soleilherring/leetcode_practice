class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        parameters: 
        list of string - list 1
        list of string - list 2
        return:
        the common strings with the lowest index sum
        example ['cat','dog','bird'], 
                ['dog','lizard', 'cat']
                1 + 0 => 1, 
                ['dog']
        use set to find common words
        index_sum dict, to hold the word and the sum of index as value
        two for loops
            for loop for list 1 
                check that this is a common word in the common_str set if so...
                    add word to dict with value as its current index
            for loop for list 2
                check that this is a common word in the common_str set if so... 
                    add word to dict with value+= index (because this will be already added to index_sum dict, we are just adding the 
                    new index to it so we can get the sum of index)
            make a new list
            result list
            minimum value = min(index_sum.val)
            for loop
                from word in the common strs..
                    check if the index_sum[word] value == min val, if so add it to result list
            return result list
                


        
        """
        common_str = set(list1) & set(list2)
        index_sum = {}
        for index, word in enumerate(list1):
            if word in common_str:
                index_sum[word] = index
        for index, word in enumerate(list2):
            if word in common_str:
                index_sum[word] += index

        result = []
        min_sum = min(index_sum.values())
        for word in common_str:
            if index_sum[word] == min_sum:
                result.append(word)
        return result 