class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
    #   parameters: list of lists
    # return: the destination 
    # example: [['london','milan'], ['milan', 'vienna'], ['vienna','hamburg']]
    # return hamburg
    # pseudo:
    # 1. make into a dictinoary
    #2. check that each has a key with a value, if not value, return that node
    # 3. for each key in dictionary 
    #       check if it has a value. if not, return key 

        dest_dict = {}
        for path in paths:
            dest_dict[path[0]] = path[1]

        for path in dest_dict:
            while path in dest_dict:
                path = dest_dict[path]
        return path
        
