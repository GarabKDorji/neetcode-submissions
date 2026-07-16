# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
  
        slow = head 
        fast = head     

        while fast and fast.next:
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
        
        curr1 = head 
        curr2 = prev 

        while curr1 and curr2: 
            new1 = curr1.next
            new2 = curr2.next 

            curr1.next = curr2
            curr2.next = new1 

            curr1 = new1
            curr2 = new2





