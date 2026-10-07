class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l1 = len(nums)
        filtered_list = [i for i in nums if i != 0]
        l2 = len(filtered_list)
        nums[:] = filtered_list + [0]*(l1-l2)