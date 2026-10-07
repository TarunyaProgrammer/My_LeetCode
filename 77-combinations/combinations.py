class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start: int, path: list[int]):
            # Base case: valid combination found
            if len(path) == k:
                res.append(path.copy())
                return
            
            # Explore choices
            # Pruning optimization: only loop while enough remaining numbers exist to reach length k
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # Backtrack
                
        backtrack(1, [])
        return res