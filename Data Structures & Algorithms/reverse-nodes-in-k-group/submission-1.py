# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        dummy = ListNode(0, head)
        group_prev = dummy
        while True: 
            kth = None 
            curr = group_prev 
            j = 0
            while curr and j < k: 
                j += 1 
                curr = curr.next 
            kth = curr
            if not kth:
                break
            groupNext = kth.next

            prev , curr = kth.next, group_prev.next 
            while curr != groupNext:
                new = curr.next 
                curr.next = prev
                prev = curr 
                curr= new 

            group_start = group_prev.next
            group_prev.next = kth
            group_prev = group_start
        
        return  dummy.next 


            


