class Solution:
    def maxProfit(self, pr: List[int]) -> int:
        max_prof = 0
        mn = pr[0]
        for i in pr:
            if i-mn>max_prof:max_prof = i-mn
            if i < mn:mn = i
        return max_prof


        ## APP 2 - dict
# class Solution:
#     def maxProfit(self, pr: List[int]) -> int:
#         seen = {}
#         mn = pr[0]
#         max_prof = 0

#         for i, price in enumerate(pr):
#             seen[i] = price
#             max_prof = max(max_prof, price - mn)
#             mn = min(mn, price)

#         return max_prof