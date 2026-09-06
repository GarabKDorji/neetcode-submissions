# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head 
        fast = head 

        while fast.next and fast.next.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        curr = slow.next 
        slow.next = None 

        prev = None 
        while curr: 
            new = curr.next 
            curr.next = prev 
            prev = curr 
            curr = new 
        
        curr = head 
        curr2 = prev 

        while curr and curr2: 
            new1 = curr.next 
            new2 = curr2.next 
            
            curr.next = curr2 
            curr2.next = new1 

            curr = new1 
            curr2 = new2 
    



