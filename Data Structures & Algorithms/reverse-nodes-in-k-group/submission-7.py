# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy 
        curr = dummy
        while True: 
            i = 0
            while curr and i < k : 
                curr = curr.next 
                i += 1 
            
            if not curr:
                break 
            
            kth = curr 
            new_group = kth.next 
            prev = kth.next
            curr = prev_group.next 

            while curr != new_group: 
                new = curr.next 
                curr.next = prev 
                prev = curr 
                curr = new 
            
            old_head = prev_group.next
            prev_group.next= prev 

            prev_group = old_head 
            curr = prev_group 
        
        return dummy.next


