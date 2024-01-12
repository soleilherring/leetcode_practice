
# DESCRIPTION:
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(lst):
    # PREP
    # P : list of numbers
    # R : list of numbers (inverse of first list)
    # E : [1,2,3,4,5] --> [-1,-2,-3,-4,-5]
    # P :
    # 1. for loop for ever number in the list
    # 2. multiply number by negative sign
    # 3 return the list with the updated numbers 
    
    
    inverted_list = [-item for item in lst]
    return inverted_list