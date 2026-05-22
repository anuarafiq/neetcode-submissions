class Solution:

    key = 2
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            for c in word:
                c = chr(ord(c) + self.key)
                ans += c
            if strs.index(word) != len(strs) - 1:
                ans += " "
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = ""
        ret = []
        for c in s:
            if c == " ": 
                ret.append(ans)
                ans = ""
                continue
            c = chr(ord(c) - self.key)
            ans += c
        ret.append(ans)

        return ret