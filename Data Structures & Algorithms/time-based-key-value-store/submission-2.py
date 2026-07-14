class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.store :
            self.store[timestamp] = {} 
            self.store[timestamp][key] = []

        self.store[timestamp][key].append(value)

            

    def get(self, key: str, timestamp: int) -> str:
        if not self.store:
            return ""

        # Only include timestamps that contain the requested key
        res = [
                time for time in self.store
                if key in self.store[time]
            ]

        if not res:
            return ""

        l = 0
        r = len(res) - 1

        while l <= r:
            mid = (l + r) // 2

            if res[mid] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1

        # No timestamp is less than or equal to the target
        if r < 0:
            return ""

        chosen_timestamp = res[r]
        return self.store[chosen_timestamp][key][-1]