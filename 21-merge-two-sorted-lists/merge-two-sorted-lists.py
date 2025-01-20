# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # PREP
        # 1. make a dummy node to hold the updated list 
        # 2. if the list1.next value > list2.next value, then list2.value goes next in the dummy node
        #     otherwise, list1.next value goes next
        #     do current.next for either  list one or list2 depending on which one is put as the next node in the dummy node
        # 3. updated the dummy node so it's current node is the next one. 

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next 
        
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
            

        
















        # # create a dummy listnode to hold the new linked list
        # dummy = ListNode()
        # # move through linkedlist by setting another variable to be equal to the dummy, it will be the tail
        # tail = dummy

        # # when there are equal number of nodes in both list1 and list2
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next
        #     else:
        #         tail.next = list2
        #         list2 = list2.next
        #     tail = tail.next 

        # if list1:
        #     tail.next = list1
        # if list2:
        #     tail.next = list2

        # return dummy.next
        