from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        s1_permute = Counter(s1)
        s2_permute = Counter(s2[:k])

        for i in range(k, n):
            if s2_permute == s1_permute: return True
            else:
                s2_permute[s2[i-k]] -= 1
                s2_permute[s2[i]] += 1

        if Counter(s2[n-k:n]) == s1_permute: return True

        return False