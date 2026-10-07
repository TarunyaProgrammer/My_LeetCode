class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        posI,negI = 0,1
        for i in nums:
            if i>=0:
                res[posI] = i
                posI+=2
            else:
                res[negI] = i
                negI+=2
        return res