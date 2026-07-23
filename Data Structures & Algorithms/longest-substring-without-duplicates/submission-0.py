class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = deque()
        length = 0
        
        for c in s:
            while c in sub:
                sub.popleft()
            sub.append(c)
            length = max(length, len(sub))

        return length