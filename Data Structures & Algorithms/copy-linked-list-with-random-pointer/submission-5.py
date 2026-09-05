"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        store = {None:None} 
        dummy = Node(0)
        curr = dummy 
        head1 = head
        while head1: 
            node = Node(head1.val)
            store[head1] = node 
            curr.next = node 
            curr = curr.next 
            head1 = head1.next 
        
        curr = dummy.next

        while head: 
            curr.random = store[head.random]
            head = head.next 
            curr = curr.next
        
        return dummy.next
            
        

        
