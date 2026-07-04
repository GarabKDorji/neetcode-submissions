class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = []

        for c in s:
            if c.isalnum():
                newStr.append(c.lower())

        newStr = ''.join(newStr)

        return newStr == newStr[::-1]
            


        

                

        