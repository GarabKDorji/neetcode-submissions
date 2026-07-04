class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_string = [] 
        for char in s:
            if  char.isalpha() or char.isnumeric():
                c = char.lower()
                new_string.append(c)
        


        l = 0 
        r = len(new_string)-1
        while l < r:
            if new_string[l] != new_string[r]:
                return False 
            l += 1 
            r -= 1 
        return True
            

            


        

                

        