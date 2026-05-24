class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        s = s.replace(" ", "").lower()
        s = "".join([c for c in s if c.isalnum()])
        l, r = 0, len(s)-1

        while l <= r:
            while not s[l].isalnum(): l += 1
            while not s[r].isalnum(): r -= 1

            if s[l] != s[r]: return False
            l += 1
            r -= 1

        return True