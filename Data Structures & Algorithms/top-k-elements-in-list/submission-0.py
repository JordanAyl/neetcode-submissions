class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashnums = {}
        numsList = []

        for num in nums:
            hashnums[num] = 1 + hashnums.get(num, 0)

        for num,cnt in hashnums.items():
            numsList.append([cnt,num])

        numsList.sort()
        res = []
        while k > len(res):
            res.append(numsList.pop()[1])

        
        return res

        

        
        