class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def quickSelect(l,r):
            if l >= r: 
                return
            pivotDistance = points[r][0] **2 + points[r][1] **2 
            p = l 

            for i in range(l,r):
                dist = points[i][0] **2 + points[i][1] **2 
                if dist <= pivotDistance: 
                    points[p],points[i] = points[i], points[p]
                    p += 1 
            points[r],points[p] = points[p], points[r]

            if p < k: 
                return quickSelect(p+1, r)
            elif p > k: 
                return quickSelect(l, p-1)

        index = quickSelect(0,len(points)-1)
        return points[:k]