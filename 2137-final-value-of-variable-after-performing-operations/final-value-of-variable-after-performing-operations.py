class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        plus = op.count("++X") + op.count("X++")
        minus = op.count("--X") + op.count("X--")
        return plus-minus