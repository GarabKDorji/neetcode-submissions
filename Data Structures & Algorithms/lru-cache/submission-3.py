class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        
        previous = self.right.prev 
        previous.next = node 
        node.next = self.right 
        node.prev = previous 
        self.right.prev = node

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # Remove node from current position
            node.prev.next = node.next
            node.next.prev = node.prev

        else:
            node = Node(key, value)
            self.cache[key] = node

        # Insert node on the right
        previous = self.right.prev
        previous.next = node
        node.prev = previous
        node.next = self.right
        self.right.prev = node

        if len(self.cache) > self.cap:
            remove = self.left.next

            self.left.next = remove.next
            remove.next.prev = self.left

            self.cache.pop(remove.key)

            



        

