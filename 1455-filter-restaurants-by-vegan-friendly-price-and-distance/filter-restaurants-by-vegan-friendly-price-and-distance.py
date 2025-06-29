class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    # #   parameters:
    # list of lists
    # integers
    # - veganFriendly,
    # -maxPrice
    # -maxDistance
    # return
    # list of integers(id, ordered by the rating)
    # example [1,4,1,40,10], [4,10,0,10,3], [3,8,1,30,4]-> [3,1]
    # pseudocode:
    # 1. filter by three categories:
    #     a. veganfriendly (if true)
    #     b. maxPrice (less than or equal to)
    #     c. maxDistance( less than or equal to)
    # 2. return an array of ids, sorted by rating

    # CONTANTS = id, rating, veganFriendly price, distance and their indexes
    # A. for loop 
    #     a. check if the maxPrice/maxDistance is less than or equal to input
    #         check if the veganFriendly is 0, if it isnt that means its true so filter by that
    # B. after getting filtered list, sort by rating
    # c. return id for the sorted by rating list
        ID, RATING, VEGAN, PRICE, DIST = 0, 1, 2, 3, 4
        filtered = []
        for rest in restaurants:
            if rest[PRICE] <= maxPrice and rest[DIST] <= maxDistance and (veganFriendly == 0 or rest[VEGAN]):
                filtered.append(rest)

        # sort, usually ascending, need to make descending 
        sorted_rest = sorted(filtered, key= lambda rest : (rest[RATING], rest[ID]), reverse =True)
        
        # return result array based on id of sorted rating list
        result = []
        for rest in sorted_rest:
            result.append(rest[ID])
        
        return result