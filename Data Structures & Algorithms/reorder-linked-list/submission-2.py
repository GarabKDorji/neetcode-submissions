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
        
        head2 = slow.next 
        slow.next = None 
    
        prev = None 
        while head2: 
            new = head2.next 
            head2.next = prev 
            prev = head2
            head2 = new 
        
        curr1 = head 
        curr2 = prev 

        while curr1 and curr2: 
            new1 = curr1.next
            new2 = curr2.next 

            curr1.next = curr2 
            curr2.next = new1 

            curr1 = new1 
            curr2 = new2 
        



