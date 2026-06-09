class Solution:
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        l, r = 0, 0
        max_len = 0
        substring = set()

        for i in range(n):
            if not substring: 
                substring.add(s[i])
                continue

            while s[i] in substring: 
                substring.remove(s[l])
                l += 1

            else:
                substring.add(s[i])
            r += 1
            max_len = max(max_len, r-l + 1)

        return max_len