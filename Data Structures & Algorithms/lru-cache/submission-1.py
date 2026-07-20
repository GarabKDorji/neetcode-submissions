class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.store = {}
    def get(self, key: int) -> int:
        if key not in self.store:
            return - 1 
        
        value = self.store[key] 
        self.store.pop(key)
        self.store[key]  = value 
        return value

        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)

        self.store[key] = value

        if len(self.store) > self.cap:
            old_key = next(iter(self.store))
            self.store.pop(old_key)