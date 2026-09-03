class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store: 
            self.store[key] = [] 
        
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value = self.store.get(key, [])
        if not value: 
            return ""
        
        l = 0 
        r = len(value) - 1 
        while l <=r : 
            mid = (l + r)//2 
            if value[mid][1] > timestamp: 
                r = mid - 1 
            else:
                l = mid + 1 
        if l > 0:
            return value[l-1][0]
        return ""
