class Solution:
    def mostWordsFound(self, sent: List[str]) -> int:
        mx = 0
        for i in sent:
            curr = i.count(" ") +1
            if mx<curr:mx = curr
        return mx