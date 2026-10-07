import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxHeap = []

        def dist(x,y):
            return - ( x**2 + y**2 )**(0.5) ## negate for max heap
        for x,y in points:
            heappush(maxHeap, ( dist(x,y), [x,y] ))
            
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [point for dist, point in maxHeap]