# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """While loop curr """

        if not list1 and list2:
            return list1 or list2

        dummy = node = ListNode()
        
        #If one of the list arent null continue
        while list1 and list2:
            #if one val is great than the other make it part of new list and move that list fwrd
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next
            #update node list to newest value
            node = node.next

        #finalize last number
        node.next = list1 or list2

        #return the head of the list that was held in dummy
        return dummy.next