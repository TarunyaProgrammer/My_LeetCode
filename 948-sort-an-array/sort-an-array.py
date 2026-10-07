class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # l = len(nums)
        # is_swap = False
        # for i in range(l-2, -1, -1):
        #     for j in range(i+1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        #             is_swap = True
        #     if not is_swap:break
        # return nums


        # l = len(nums)
        # for i in range(1, l):
        #     key = nums[i]
        #     j = i-1
        #     while j>=0 and nums[j]>key:
        #         nums[j+1] = nums[j]
        #         j-=1
        #     nums[j+1] = key
        # return nums


        def mArray(l,r):
            res = []
            i = j = 0
            n,m = len(l),len(r)
            while i<n and j<m:
                if l[i] <= r[j]:
                    res.append(l[i])
                    i+=1
                else:
                    res.append(r[j])
                    j+=1
            if i<n:res.extend(l[i:])
            if j<m:res.extend(r[j:])
            return res
        
        def merge_sort(arr):
            if len(arr)<=1:return arr
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return mArray(left, right)
        return (merge_sort(nums))