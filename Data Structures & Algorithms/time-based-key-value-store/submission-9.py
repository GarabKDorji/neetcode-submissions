class TimeMap:

    def __init__(self): 
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore: 
            self.keyStore[key] = []
        self.keyStore[key].append((value,timestamp))        

    def get(self, key: str, timestamp: int) -> str:

        v = self.keyStore.get(key,[])
        l = 0 
        r = len(v) - 1 
        res = ""
        while l <= r: 
            mid = (l + r)//2 
            if v[mid][1] <= timestamp: 
                res = v[mid][0]
                l = mid + 1 
            else:
                r = mid - 1
        
        return res
