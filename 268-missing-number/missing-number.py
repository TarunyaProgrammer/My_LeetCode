class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sm = sum(nums)
        l = len(nums)
        return (
            (l * (l+1))//2 - sm
        )