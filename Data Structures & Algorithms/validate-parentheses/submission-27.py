class Solution:
    def isValid(self, s: str) -> bool:
        validate = {']':'[', '}':'{', ')':'(' }
        res = []

        for i in s:
            if i in validate:
                if res and res[-1] == validate[i]:
                    res.pop()
                else:
                    return False
            else:
                res.append(i)

        return not res










