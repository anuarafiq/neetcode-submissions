from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str):
        k = len(s1)
        n = len(s2)
        s1_permute = Counter(s1)

        for i in range(k, n+1):
            if Counter(s2[i-k:i]) == s1_permute: return True

        return False