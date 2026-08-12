class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count = {}
        l = 0
        largest = 0
        for r in range(len(s)):
            
            if s[r] in count:
                l = max(l, count[s[r]] + 1)

            count[s[r]] = r

            largest = max(largest, r -l + 1)


        return largest


