class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i%2==0:res.insert(0, 0)
            else:res.insert(len(res), 1)
        return res