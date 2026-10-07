class Solution:
   def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        curr = []
        n = len(s)
        def f(i):
            if i == n:
                ans.append(" ".join(curr[::]))
            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    curr.append(s[i:j+1])
                    f(j+1)
                    curr.pop()
        f(0)
        return ans