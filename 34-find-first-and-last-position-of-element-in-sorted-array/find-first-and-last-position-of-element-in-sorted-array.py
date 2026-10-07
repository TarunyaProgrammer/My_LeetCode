class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(nums, target, findLeft):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if findLeft:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return bound
        
        leftBound = findBound(nums, target, True)
        if leftBound == -1:
            return [-1, -1]
        
        rightBound = findBound(nums, target, False)
        return [leftBound, rightBound]