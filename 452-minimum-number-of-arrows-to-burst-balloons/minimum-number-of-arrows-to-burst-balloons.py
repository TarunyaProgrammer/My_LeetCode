class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        currEnding = -float('inf')
        points.sort()
        arrow = 0
        for start, end in points:
            if start <= currEnding:
                currEnding = min(end, currEnding)
            else:
                arrow += 1
                currEnding = end
        return arrow