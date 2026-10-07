class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = sum(nums)
        if x < k: return sum(nums)
        elif x // k == 0: return 0
        return x % k
        