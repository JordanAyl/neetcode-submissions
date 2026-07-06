class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ana = {}
        ana2 = {}
        for i in range(len(s)):
            ana[s[i]] = 1 + ana.get(s[i], 0)
            ana2[t[i]] = 1 + ana2.get(t[i], 0)

        return ana == ana2        
        





            


        