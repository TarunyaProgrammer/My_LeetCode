from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        count = Counter(nums)

        minHeap = []
        for num, freq in count.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [num for freq, num in minHeap]