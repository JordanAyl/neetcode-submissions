class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        abovek = []

        for key, val in freq.items():
            abovek.append([val, key])

        res = []
        abovek.sort()
        while len(res) < k:
            res.append(abovek.pop()[1])

        return res



