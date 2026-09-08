# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        curr = dummy
        prev_group = curr
        while True: 
            i = 0 
            while curr and i < k: 
                curr = curr.next 
                i += 1 
            
            if not curr:
                break 
            
            kth = curr 
            prev = curr.next 
            curr = prev_group.next
            next_group = kth.next
            old_head = curr 
            while curr != next_group: 
                new = curr.next 
                curr.next = prev 
                prev = curr 
                curr = new 
            
            prev_group.next = prev 
            prev_group = old_head 
            curr= prev_group


        return dummy.next

