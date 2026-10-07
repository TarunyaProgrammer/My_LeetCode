class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i1 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        for i2 in range(n2):
            while i1 < n2 and nums1[i1] < nums2[i2]:i1 += 1
            if i1 == n1:break
            if nums1[i1] == nums2[i2]:return nums1[i1]
        return -1