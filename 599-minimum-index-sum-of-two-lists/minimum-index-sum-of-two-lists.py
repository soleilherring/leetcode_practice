class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        set1 = set(list1)
        set2 = set(list2)

        # # make a dictionary to hold set 1 name and index
        #     for name in set2 if it's in set 1, update the dictionary index
        #     shogun 0
        #     tapioca 1
        #     burger 2
        #     kfc 3
        #     if name in set1, 
        #         dict[shogun] +=1 
        #         dic

        # check if there is an intersection of 1, if so just return
        intersection = (set1 & set2)
        if len(intersection) ==1:
            return list(intersection)
        
        str_index = {}
        for index, word in enumerate(list1):
            if word in intersection:
                str_index[word] = index
        # print(str_index)
            
        for index, word in enumerate(list2):
            if word in str_index:
                str_index[word] += index
        
       
        result = [] 
        min_index = float('inf')
        for word, val in str_index.items():
            if val < min_index:
                min_index = val
                result = [word]
            elif val == min_index:
                result.append(word)
        return result



            
        
        
        
        
        
        
        
        
        
        # set1 = set(list1)
        # set2 = set(list2)

        # intersection =  (set1 & set2) 
        # if len(intersection) == 1:
        #     return list(intersection)

        # index_dict = {}

        # # filter by intersection words
        # for index, word in enumerate(list1):
        #     if word in intersection:
        #         index_dict[word] = index
        # # only add index to words that are in the index dict (which we know are intersecting because we filtered for that)
        # for index, word in enumerate(list2):
        #     if word in index_dict:
        #         index_dict[word] += index

        # min_index = float('inf')
        # result = []

        # for word, index_sum in index_dict.items():
        #     if index_sum < min_index:
        #         min_index = min(index_sum, min_index)
        #         result = [word]
        #     elif min_index == index_sum:
        #         result.append(word)
        # return result