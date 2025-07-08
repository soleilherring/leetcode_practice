class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = set(list1)
        set2 = set(list2)

        intersection =  (set1 & set2) 
        if len(intersection) == 1:
            return list(intersection)

        index_dict = {}

        # filter by intersection words
        for index, word in enumerate(list1):
            if word in intersection:
                index_dict[word] = index
        # only add index to words that are in the index dict (which we know are intersecting because we filtered for that)
        for index, word in enumerate(list2):
            if word in index_dict:
                index_dict[word] += index

        min_index = float('inf')
        result = []

        for word, index_sum in index_dict.items():
            if index_sum < min_index:
                min_index = min(index_sum, min_index)
                result = [word]
            elif min_index == index_sum:
                result.append(word)
        return result