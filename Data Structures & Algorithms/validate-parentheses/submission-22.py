class Solution:
    def isValid(self, s: str) -> bool:
        bracketHash = {'}' : '{',']' : '[',')' : '('}
        result = []
        for c in s:
            if c in bracketHash:
                if result and result[-1] == bracketHash[c]:
                    result.pop()
                else:
                    return False
            else:
                result.append(c)

        return not result










