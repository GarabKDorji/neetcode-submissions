# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy 
        base = 0 
        extra = 0 
        while l1 or l2 or extra > 0 :  
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + extra 
            base = total % 10  
            extra = total // 10 
            node = ListNode(base)
            curr.next = node 
            curr = curr.next 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
            
