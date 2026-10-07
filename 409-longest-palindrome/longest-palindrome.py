# class Solution:
#     from collections import defaultdict
#     def longestPalindrome(self, s: str) -> int:
#         freq = defaultdict(int)
#         for char in s:
#             freq[char] += 1  # Count frequencies
        
#         total = 0
#         has_odd = False
#         for count in freq.values():
#             total += count // 2 * 2  # Add even pairs
#             if count % 2 == 1:  # Track if any odd count exists
#                 has_odd = True
        
#         return total + 1 if has_odd else total



# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         c = Counter(s)

#         one = True
#         count = 0
#         for k,v in c.items():
#             count += (v // 2) * 2

#             if one and v & 1 == 1:
#                 count += 1
#                 one = False
#         return count




class Solution:
    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0

        # Loop over characters in the string
        for c in s:
            # If set contains the character, match found
            if c in character_set:
                character_set.remove(c)
                
                res += 2
            else:
               
                character_set.add(c)
        if character_set:
            res += 1

        return res