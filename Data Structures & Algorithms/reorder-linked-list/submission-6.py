# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return None 
        
        slow = head 
        fast = head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        curr = slow.next   
        slow.next = prev = None

        while curr:
            new = curr.next 
            curr.next = prev
            prev = curr 
            curr = new 
        
        new_head = prev 
        l1 = head
        l2 = new_head 
        while l1 and l2: 
            new1 = l1.next 
            new2 = l2.next 

            l1.next = l2 
            l2.next = new1 

            l1 = new1 
            l2 = new2 
        

        

        

