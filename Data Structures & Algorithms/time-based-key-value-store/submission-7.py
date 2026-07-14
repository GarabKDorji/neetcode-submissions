class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store :
            self.store[key] = []

        self.store[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        if not self.store:
            return ""

        # Only include timestamps that contain the requested key
        res = self.store.get(key,[])


        l = 0
        r = len(res) - 1

        while l <= r:
            mid = (l + r) // 2

            if res[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1

        # No timestamp is less than or equal to the target

        if r < 0:
            return ""

        return res[r][1]