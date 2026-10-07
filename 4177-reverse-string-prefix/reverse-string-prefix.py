class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        rs = s[:k]
        final = rs[::-1]
        return final+s[k:]