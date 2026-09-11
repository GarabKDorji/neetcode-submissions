class Node: 

    def __init__(self,key,value): 
        self.key = key 
        self.value = value
        self.prev = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.store = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev 
    
    def insert(self, node):
        nxt, prev = self.right, self.right.prev 
        prev.next, nxt.prev = node , node 
        node.prev , node.next = prev , nxt

    def get(self, key: int) -> int:
        if key not in self.store: 
            return -1 
        
        node = self.store[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.store: 
            self.remove(self.store[key])
        self.store[key] = Node(key, value)
        self.insert(self.store[key])

        if len(self.store) > self.cap: 
            lru = self.left.next 
            self.remove(self.store[lru.key]) 
            del self.store[lru.key]   
        
