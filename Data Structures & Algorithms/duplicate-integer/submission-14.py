class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mp = {}

        for i, n in enumerate(nums):
            mp[n] = mp.get(n, 0) + 1

            if mp[n] > 1:
                return True

        return False