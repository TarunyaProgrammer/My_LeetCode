class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        #all eaten by m2
        ans = sum(reward2)
        arr = []

        for i in range(len(reward1)):
            arr.append(reward1[i]-reward2[i])

        arr.sort(reverse = True)
        ans += sum(arr[:k])
        return ans