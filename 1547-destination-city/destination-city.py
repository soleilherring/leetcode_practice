class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        nested list with list of strings of destinations 
        return the destination city
        example [["a", "b"], ["c","d"], ["b", "c"]] -> d
        pseudo:
            1. make into dictionary
            2. if the the destination doesnt appear as both a key and value, than it is the destination 
            loop over
            if the destination is not a key at some point it is the destination city
        """
        destinations = {}
        
        def build_dict(route, hash_map):
            for i in range(1, len(route)):
                destinations[path[i-1]] = path[i]
            return destinations
        
        for path in paths:
            all_routes = build_dict(path, destinations)
        
        for path in all_routes.values():
            if path not in all_routes.keys():
                return path