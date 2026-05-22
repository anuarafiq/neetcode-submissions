from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]

        group = []
        groups = []
        seen = set()
        for i in range(len(strs)):
            if i not in seen:
                curr = Counter(strs[i])
                group.append(strs[i])
            for j in range(i+1, len(strs)):
                if Counter(strs[j]) == curr and j not in seen:
                    group.append(strs[j])
                    seen.add(j)
            if group:
                groups.append(group)
            group = []
        
        return groups