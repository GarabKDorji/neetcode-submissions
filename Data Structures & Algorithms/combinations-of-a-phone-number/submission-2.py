class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        store = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        path = [] 
        res = []
        def dfs(index):
            if index == len(digits): 
                res.append("".join(path[:]))
                return 
            for i in store[digits[index]]:
                path.append(i)
                dfs(index+1)
                path.pop()
        
        dfs(0)
        return res
            
