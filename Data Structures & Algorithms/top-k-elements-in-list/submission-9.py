class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for i, v in freq.items():
            bucket[v].append(i)
        
        res = [] 
        for i in range(len(bucket)-1,0, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res
        return []