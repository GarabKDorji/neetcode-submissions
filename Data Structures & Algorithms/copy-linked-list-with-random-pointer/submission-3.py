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
        curr = head
        dummy = Node(0)
        curr = head 
        tail = dummy 
        while curr: 
            tail.next = Node(curr.val)
            curr = curr.next 
            tail = tail.next        
        
        freq = {} 
        curr2 = dummy.next 
        curr1 = head
        while curr1: 
            freq[curr1] = curr2
            curr1 = curr1.next 
            curr2 = curr2.next

        curr = head 
        curr2 = dummy.next 
        while curr:
            value = curr.random
            if value:
                node = freq[value]
            else:
                node = None
            curr2.random = node 
            curr = curr.next 
            curr2 = curr2.next 
        
        return dummy.next

            



        
        
        