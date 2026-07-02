class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        res = list(freq.keys())
        res.sort(key= lambda k: -freq[k])

        return res[:k]