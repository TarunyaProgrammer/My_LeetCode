class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        high, low = n-1, 0
        while high>=low:
            mid = (high+low)//2
            if nums[mid]==target:return mid # prob solved here!
            if nums[mid]<=nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
        return -1