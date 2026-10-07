class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def bt(start, path):
            res.append(path[:]) # copying current subset
            for idx in range(start, len(nums)):

                #pruning
                if idx > start and nums[idx] == nums[idx-1]:
                    continue
                
                path.append(nums[idx])
                bt(idx+1, path)
                path.pop()
        bt(0, [])
        return res