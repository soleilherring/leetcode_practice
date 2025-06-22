class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        """
        parameters:
        list of lists, 
        restaurant[i] = [id, rating, veganFriendly, price, distance]
            filter first by veganFriendly
        filter by veganFriendly, price, distance

        return:
        list of restaurants sorted by rating from highest to lowest
        if restaurant is the same, by id highest to lowest
        """
        
        # for restaurant in restaurants:
            # lambda function
            # if veganFriendly = 1, filter out restaurants that are vegan friendly
        if veganFriendly == 1:
            restaurants = list(filter(lambda restaurant: restaurant[2] == 1, restaurants))
            # otherwise filter based on maxPrice, maxDistance
            # filter to check that the maxPrice for each restaurant is lower than the maxPrice variable
        restaurants = list(filter(lambda restaurant: restaurant[3]<= maxPrice and restaurant[4] <=maxDistance, restaurants))
        # sorty by rating (descending)
        sorted_restaurants = sorted(restaurants, key = lambda r:(-r[1], -r[0]))
       
        return [r[0] for r in sorted_restaurants]
        