class Solution:
    def isValid(self, s: str) -> bool:
        dic = {']':'[', '}':'{', ')':'('}
        holder = []

        for value in s:
            if value in dic:
                if holder and holder[-1] == dic[value]:
                    holder.pop()
                else:
                    return False
            else:
                holder.append(value)

        return not holder







