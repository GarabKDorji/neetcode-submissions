class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        arr = [] 

        for i, v in freq.items():
            arr.append((v,i))
        

        arr.sort(key = lambda x:-x[0])

        res = [] 
        for i in arr:
            res.append(i[1])
            if len(res) >= k:
                break 
        
        return res

        
