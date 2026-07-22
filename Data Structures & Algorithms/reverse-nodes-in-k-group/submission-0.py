# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None 
            j = 0
            while node and j < k:
                new = node.next 
                node.next = prev 
                prev = node 
                node = new 
                j += 1
            return prev,node

        if not head or k <= 1:
            return head
                
        
        
        n = 0   
        curr = head 
        while curr:
            n += 1 
            curr = curr.next 
        
        if n// k == 0:
            return head 

        dummy = ListNode(0, head)
        group_prev = dummy


        for _ in range(n // k):
            group_start = group_prev.next

            new_head, next_group = reverse(group_start)

            # Connect the previous part to the new group head
            group_prev.next = new_head

            # The old group head is now the group tail
            group_start.next = next_group

            # Move to the node before the next group
            group_prev = group_start

        return dummy.next
            


