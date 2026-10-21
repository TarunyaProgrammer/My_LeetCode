class Solution:

  def numDecodings(self, s: str) -> int:
    n = len(s)
    # w1 represents ways to decode s[i+1], w2 represents ways to decode s[i+2]
    w1, w2 = 1, 0

    for i in range(n - 1, -1, -1):
      current = 0
      if s[i] != '0':
        current += w1
        # Check if two-digit combination (s[i:i+2]) is valid ("10" to "26")
        if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
          current += w2

      w2, w1 = w1, current

    return w1