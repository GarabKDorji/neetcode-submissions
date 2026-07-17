class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        
        arr = [(v,i) for i,v in freq.items()]

        arr.sort(reverse = True)

        res = [] 
        for i in arr:
            res.append(i[1])
            if len(res) == k:
                return res

            