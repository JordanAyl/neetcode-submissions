# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        newl = []
        curr = dummy
        for i in range(len(lists)):
            while lists[i]:
                newl.append(lists[i].val)
                lists[i] = lists[i].next
        newl.sort()

        for node in newl:
            curr.next = ListNode(node)
            curr = curr.next

        return dummy.next