class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.store = {}   # key → value
        self.order = []   # least recent → most recent
    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        self.order.remove(key)
        self.order.append(key)

        return self.store[key]

        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)
            self.order.remove(key)

        self.store[key] = value
        self.order.append(key)
        if len(self.order) > self.cap:
            value = self.order.pop(0)
            self.store.pop(value)
        

