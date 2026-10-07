class Solution:
    def canPlaceFlowers(self, bed: List[int], n: int) -> bool:
        m = 0
        if len(bed) == 1:
            return n == 0 or bed[0] == 0
        if bed[0] == 0 and bed[1] == 0:
            m += 1
            bed[0]=1
        if bed[-1] == 0 and bed[-2] == 0:
            m += 1
            bed[-1]=1
        for i in range(1, len(bed)-1):
            if bed[i-1] == 0 and bed[i] == 0 and bed[i+1] == 0:
                bed[i]=1
                m += 1
                print(i)
        if m>=n:return True
        return False