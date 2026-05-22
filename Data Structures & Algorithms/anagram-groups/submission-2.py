from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for word in strs:
            freq = tuple(sorted(Counter(word).items()))
            if freq in hashmap.keys():
                hashmap[freq].append(word)
            else:
                hashmap[freq] = [word]

        ans = []
        for words in hashmap.values():
            ans.append(words)
        
        return ans