class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sList = sorted(list(s))
        tList = sorted(list(t))

        for i in range(len(sList)):
            if sList[i] != tList[i]:
                return False
        return True
            


        