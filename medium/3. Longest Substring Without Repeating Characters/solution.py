class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i0, res = 0, 0
        for i, c in enumerate(s):
            if c in d:
                i0 = max(i0, d[c] + 1)
            res = max(res, i-i0+1)
            d[c] = i
        return res