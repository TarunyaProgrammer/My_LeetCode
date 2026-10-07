class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(start, remain, path):
            if remain == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain: # will never be possible
                    break

                path.append(candidates[i])
                backtrack(i, remain - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res