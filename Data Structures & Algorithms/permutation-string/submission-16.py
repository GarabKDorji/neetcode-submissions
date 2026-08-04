class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0 
        freq_s1 = Counter(s1)
        count = defaultdict(int)
        for r in range(len(s2)):
            count[s2[r]] +=1 

            if r - l + 1 > len(s1):
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    count.pop(s2[l])
                l +=1 
            print(count)
            if freq_s1 == count:
                return True 

        return False                