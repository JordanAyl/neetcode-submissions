class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = sorted(t)
        "".join(t)

        s = sorted(s)
        "".join(s)

        return s == t




            


        