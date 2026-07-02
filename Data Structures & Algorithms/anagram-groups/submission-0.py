class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            if not str return [] 
            freq map 
            loop throught the list 
                sort the word 
                and then chck if it in the map 
                if not we create the word as the key and we append 
                and in the list we append it the value 
                freq {act: [act,cat,], opst: [pots,tops,stop],aht:[hat]} 
        '''

        if not strs:
            return [] 

        freq = {}

        for s in strs:
            v = "".join(sorted(s))
            if v not in freq:
                freq[v] = []
            freq[v].append(s)
        
        return list(freq.values())