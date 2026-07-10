class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()
                d = i - prev_index
                res[prev_index] = d 
            
            stack.append(i)
        
        return res
            
