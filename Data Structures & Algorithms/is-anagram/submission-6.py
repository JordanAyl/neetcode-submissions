class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sChar = sorted(s)
        tChar = sorted(t)

        for x in range(len(sChar)):
            if sChar[x] != tChar[x]:
                return False
                
        return True


        