class Solution:

  def numDecodings(self, s: str) -> int:

    # ##### APP 1
    # n = len(s)
    # # w1 represents ways to decode s[i+1], w2 represents ways to decode s[i+2]
    # w1, w2 = 1, 0

    # for i in range(n - 1, -1, -1):
    #   current = 0
    #   if s[i] != '0':
    #     current += w1
    #     # Check if two-digit combination (s[i:i+2]) is valid ("10" to "26")
    #     if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
    #       current += w2

    #   w2, w1 = w1, current

    # return w1

    ##### APP 2
    n = len(s)
    memo = {}
    def f(idx):
        if idx==n:
            return 1
        if s[idx] == 0: return 0

        if idx in memo:
            return memo[idx]

        ways = 0

        if '1' <= s[idx] <= '9':
            ways += f(idx+1)

        if idx + 1 < n:
            two_digit = int(s[idx : idx + 2])
            if 10 <= two_digit <= 26:
                ways += f(idx + 2)

        memo[idx] = ways
        return ways
        
    return f(0)