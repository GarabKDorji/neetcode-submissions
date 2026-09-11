class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        curr = dummy 
        prev_group = curr

        while True: 
            i = 0 

            # Find kth node
            while curr and k > i: 
                curr = curr.next 
                i += 1 
            
            if not curr:
                break 

            kth = curr 
            new_group = kth.next

            # Reverse group
            prev = new_group
            curr = prev_group.next

            while curr != new_group:
                new = curr.next 
                curr.next = prev 
                prev = curr 
                curr = new

            # Connect reversed group
            old_head = prev_group.next
            prev_group.next = prev      # FIX 1
            prev_group = old_head

            curr = prev_group           # FIX 2
        
        return dummy.next