# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """change the pointer of the current node to the next after"""

        prev = None
        curr = head
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp

        return prev
            
