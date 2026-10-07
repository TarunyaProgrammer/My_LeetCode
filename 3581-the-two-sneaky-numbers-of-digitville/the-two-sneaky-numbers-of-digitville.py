class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = [0]*len(nums)
        chor = []
        for i in nums:
            if freq[i]<1:
                freq[i]=1
            else:
                chor.append(i)

        return chor