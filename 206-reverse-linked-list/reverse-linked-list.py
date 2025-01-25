# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prep
        # 1. linked list of ints
        # 2. reversed ll
        # 3. 1-> 2 ; 2 ->1 
        # 4. create variables 
        # prev = None
        # temp = None
        # current 

        # while loop :
        #     while current:
        #         - have temp variable hold what is next to current
        #         - set current.next to prev
        #         - prev into current
        #         - curent into current.next
        #  return prev

        prev = None
        temp = None
        current = head 

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev