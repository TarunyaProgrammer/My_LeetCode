class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def backtrack(start: int, path: list[int]):
            ans.append(list(path))
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # backtrack
                
        backtrack(0, [])
        return ans