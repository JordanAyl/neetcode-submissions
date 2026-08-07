class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        length = len(temperatures)
        if sum(temperatures) / len(temperatures)  == temperatures[0]:
            return [0] * len(temperatures)

        for l in range(length - 1):
            r = l + 1

            while r < length:
                if temperatures[l] < temperatures[r]:
                    res.append(r  - l)
                    break
                if r == len(temperatures) - 1 and not temperatures[l] < temperatures[r]:
                    res.append(0)

                r += 1
        res.append(0)

        return res
