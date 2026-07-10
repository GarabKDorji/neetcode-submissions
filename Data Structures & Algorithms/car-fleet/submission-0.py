class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            Input - two arrays of same length position(miles) and speed(miles per hou)
                - target is destination 
            
            Ouput - 
            Return the number of separate car fleets that reach the target.

            A fleet can contain:
                One car traveling by itself.
                Multiple cars that catch each other before or exactly at the target.

            The fleets do not need to arrive at the target at the same time as other fleets. Each separate group counts as one fleet.
            
            Constraint - 
                n == position.length == speed.length.
                1 <= n <= 1000
                0 < target <= 1000
                0 < speed[i] <= 100
                0 <= position[i] < target
            Plan
                initilizee stack 
                sort in descending order based on the position
                
                now we iterate throught the  sorted list 
                we calcuateh time to reach 
                we append that to the stack 
                and now if stack has at least len >2 then stack[-2] >= stack[-1]  pop from the stack 
                if not we iterate throught list 

                return length of the stakc 
        '''
        stack = [] 
        pair= [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse = True)

        for p,s in pair:
            stack.append((target-p)/s)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                    stack.pop()
        
        return len(stack)



