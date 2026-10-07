class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        s = set(friends)
        for i in order:
            if i in s:res.append(i)
        return res