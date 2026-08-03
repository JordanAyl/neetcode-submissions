class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs)):
            string += f"{len(strs[i])}" + "#" + strs[i]
        return string
        
    def decode(self, s: str) -> List[str]:
        strnglst = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i +length
            strnglst.append(s[i:j])
            i = j
        
        return strnglst

