class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s = set(nums)
        pairs = 0
        for i in s:
            n = nums.count(i)
            pairs += (
                n*(n-1) //2
            )
        return pairs