class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word)) + "@" + word
        
        return ans

    def decode(self, s: str) -> List[str]:
        ptr = 0
        curr_len = ""
        ans = ""
        ret = []
        while ptr < len(s):
            # get the number of char in a word
            while s[ptr] != "@":
                curr_len += s[ptr]
                ptr += 1
            curr_len = int(curr_len)
            ptr += 1

            # loop through the word
            for _ in range(curr_len):
                ans += s[ptr]
                ptr += 1
            ret.append(ans)
            ans = ""

            # reset to count the next word
            curr_len = ""

        return ret