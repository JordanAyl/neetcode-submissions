class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        l = 0
        r = len(needle)
        length = len(haystack)
        
        while r <= length:
            if haystack[l:r] == needle:
                return l
            l += 1
            r += 1

        return -1