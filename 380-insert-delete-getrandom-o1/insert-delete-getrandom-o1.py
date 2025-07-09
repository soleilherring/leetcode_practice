import random
class RandomizedSet:

    def __init__(self):
        self.new_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.new_set:
            self.new_set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.new_set:
            self.new_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        self.new_list = list(self.new_set)
        random_item = random.choice(self.new_list)
        return random_item
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()