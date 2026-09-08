# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        group_prev = dummy 

        while True: 
            curr = group_prev
            i = 0
            while curr and i < k:
                curr = curr.next 
                i += 1 

            if not curr: 
                break 
            
            kth = curr 
            curr = group_prev.next
            old_head = curr
            group_next = kth.next 
            prev = group_next

            while curr != group_next: 
                new = curr.next 
                curr.next = prev 
                prev = curr 
                curr = new 
            
            group_prev.next = kth
            group_prev = old_head
        
        return dummy.next
            




        