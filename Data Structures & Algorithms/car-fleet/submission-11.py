class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
                
        l = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in l:
            t = (target - p) / s

            stack.append(t)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)