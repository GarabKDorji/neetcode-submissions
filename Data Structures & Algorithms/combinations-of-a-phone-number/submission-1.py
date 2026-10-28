class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letter = {"2":"abc",
               "3":"def",
               "4":"ghi",
               "5":"jkl",
               "6":"mno",
               "7":"pqrs",
               "8":'tuv',
               "9":"wxyz"}
        res = []
        part = []

        def dfs(index): 
            if index == len(digits):
                res.append("".join(part[:]))
                return 

            for i in letter[digits[index]]:
                part.append(i)
                dfs(index+1)
                part.pop()
        dfs(0)
        return res
        


