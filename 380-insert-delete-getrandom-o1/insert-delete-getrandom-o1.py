class RandomizedSet:

    def __init__(self):
        # first initialize a list
        self.lst = []
        # initiazlize a dict   
        self.dct = {}

    def insert(self, val: int) -> bool:
        # use the dictionary to check if the value is in the dictionary, if it is return false (because we are using this like its a set)
        # if the value isn't in the dictionary, append it to the list and update the dictioanry so that the index  is len of the array
        if val in self.dct:
            return False 
        
        # add it to the array and update the dictionary
        self.lst.append(val)
        self.dct[val] = len(self.lst)-1
        # print(self.dct)
        return True 

    def remove(self, val: int) -> bool:
        # if we want to remove we want to find the item in the dictionary and get it's index
        # when we get its index we want to find where it is in the array and swap its position with the last item in the array
        # update the dictionary so that the swapped value now holds the index of the toberemoved item and pop the last item aka toberemoved from the array

        # [1, 2]
        #  0. 1
        # inde_val = 0
        # swap 2 and 1
        # [2,1]
        # update 2 so the index is the index_val
        # pop the 1 (last position) off the list
        # [2]
        # update the dictionary so it doesnt have the removed key/value pair
        # del 1:0 from dictionary
        # {2:0, 1:0}
        # {1:0, 2:1}

    # val is the value to be removed
        if val not in self.dct:
            return False
        
        remove_index = self.dct[val]
            # in the array use the index to find the value to be removed
        # self.lst[index], self.lst[-1] = self.lst[-1], self.lst[index]
        last = self.lst[-1]

        self.lst[remove_index] =  last
        # Swap the value-to-remove with the last value
        self.dct[last] = remove_index

        # delete the removed value from list because we swapped it (only if using in place swapping) otherwise we just have a duplicate of last because we made the postiion were the removed value to now equal last too

        self.lst.pop()
        # remove from the dictionary 
        del self.dct[val]

        return True

    def getRandom(self) -> int:
        index =  random.randint(0, len(self.lst)-1)
        return self.lst[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()