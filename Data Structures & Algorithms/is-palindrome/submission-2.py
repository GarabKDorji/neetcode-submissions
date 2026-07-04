class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_string = [] 
        for char in s:
            if  char.isalpha() or char.isnumeric():
                c = char.lower()
                new_string.append(c)

        string = "".join(new_string)

        return string == string[::-1]            

            


        

                

        