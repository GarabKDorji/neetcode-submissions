class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers:
            return [] 

        numbers.sort()

        j = 0
        for i in range(len(numbers)):
            for j in range(i,len(numbers)):
                if numbers[i] == numbers[j]:
                    continue 
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        return []
        
