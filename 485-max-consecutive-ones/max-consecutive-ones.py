class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        count=0
        for i in nums:
            if i!=1:
                maxi=max(maxi,count)
                count=0
            else:
                count+=1
        return max(maxi,count)