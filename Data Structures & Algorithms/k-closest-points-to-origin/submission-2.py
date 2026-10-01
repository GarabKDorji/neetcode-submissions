class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []
        for xi,yi in points: 
            heapq.heappush(max_heap,[-(xi**2 + yi**2),xi,yi])
            if len(max_heap) > k :
                heapq.heappop(max_heap)

        res = []
        while k > 0: 
            val, x, y = heapq.heappop(max_heap)
            res.append([x,y])
            k -= 1 
        return res

