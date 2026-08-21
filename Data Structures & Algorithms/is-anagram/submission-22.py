class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = {}
        mp2 = {}
        for i, n in enumerate(s):
            mp[n] = mp.get(n, 0) + 1
            mp2[t[i]] = mp2.get(t[i], 0) + 1

        return mp == mp2