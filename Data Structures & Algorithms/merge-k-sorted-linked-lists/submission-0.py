# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = []

        for head in lists:
            while head:
                res.append(head.val)
                head = head.next

        res.sort()

        dummy = ListNode(0)
        tail = dummy

        for value in res:
            tail.next = ListNode(value)
            tail = tail.next

        return dummy.next

        