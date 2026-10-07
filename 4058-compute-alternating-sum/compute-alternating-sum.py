from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sums = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                sums += num
            else:
                sums -= num
        return sums