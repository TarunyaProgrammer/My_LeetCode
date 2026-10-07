class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        nums[:] = nums[:len(nums)-k][::-1] + nums[len(nums)-k:][::-1]
        nums.reverse()