class Node: 
    
    def __init__(self, key, value): 
        self.key = key 
        self.val = value 
        self.next = None 
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.cap = capacity 
        
        self.left, self.right = Node(0,0) , Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node): 
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev


    def insert(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.next , nxt.prev = node, node
        node.prev , node.next = prev,nxt

    def get(self, key: int) -> int:
        if key not in self.store: 
            return -1 
        
        node = self.store[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.store: 
            self.remove(self.store[key])
        self.store[key] = Node(key, value)
        self.insert(self.store[key])

        if len(self.store) > self.cap: 
            lru = self.left.next 
            self.remove(lru)
            del self.store[lru.key]

         
