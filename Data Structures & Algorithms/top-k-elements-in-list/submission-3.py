class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for i, n in enumerate(nums):
            mp[n] = mp.get(n, 0) + 1

        order = []
        for num, cnt in mp.items():
            order.append([cnt, num])
        
        order.sort()
        res = []
        for i in range(k):
            res.append(order.pop()[1])

        return res

