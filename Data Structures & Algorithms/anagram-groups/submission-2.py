class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list) 

        for s in strs: 
            count = [0] * 26 
            for char in s:
                count[ord(char) - ord("a")] += 1 
            freq[tuple(count)].append(s)

        return list(freq.values())