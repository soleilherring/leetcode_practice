# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        PREP
        parameters = head of a linked list
        return = true or false, true if there is a cycle 
        *** if there is a revisting of a previous node***
        returns false
        example: [1,2,3,4] 1->2->3 ->4 
                              ^______|

        pseudocode:
        1. unique = set()
        if not head:
            return False
            
        curr = head
        while curr:
            if curr not in unique:
                unique.add(curr)
            else:
                return  True
            curr = curr.next
        return False
        '''

        unique = set()
         
        if not head: 
            return False
        
        curr = head # 1
        while curr: #curr 2
            if curr not in unique:
                unique.add(curr) #{1, 2}
            else:
                return True
            curr = curr.next #2, None
        return False
        