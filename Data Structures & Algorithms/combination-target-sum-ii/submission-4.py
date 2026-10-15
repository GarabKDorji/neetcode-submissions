class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(currSum, index):
            if currSum == target:
                res.append(path[:])
                return

            if currSum > target or index >= len(candidates):
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                dfs(candidates[i] + currSum, i + 1)
                path.pop()

        dfs(0, 0)
        return res
                