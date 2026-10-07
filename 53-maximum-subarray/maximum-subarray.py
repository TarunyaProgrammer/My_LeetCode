class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        total = 0
        for i in nums:
            total+=i
            if total> maxi:maxi = total
            if total<0:total = 0
        return maxi
