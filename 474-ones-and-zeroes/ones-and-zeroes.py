class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        

        # dp = [ [0]*(n+1) for _ in range(m+1) ]
        # for s in strs:
        #     zeros = s.count('0')
        #     ones = s.count('1')

        #     for i in range(m, zeros - 1, -1):
        #         for j in range(n, ones - 1, -1):
        #             dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                    
        # return dp[m][n]

        ## APP 2

        memo = {}
        def f(idx, zeros, ones):
            if zeros > m or ones > n:
                return -float('inf')
            
            # since 0 count and 1 count sahi hai but arrau khatam
            if idx == len(strs):
                return 0

            state = (idx, zeros, ones)
            if state in memo:
                return memo[state]

            
            z = strs[idx].count('0')
            o = strs[idx].count('1')
        
            pick = 1 + f(idx+1, zeros + z, ones + o)
            skip = f(idx+1, zeros, ones)
            memo[state] = max(pick, skip)
            return max(pick, skip)
        return f(0,0,0)