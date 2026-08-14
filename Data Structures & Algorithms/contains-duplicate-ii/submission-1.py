class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        l = 0
        for r in range(len(nums)):
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            if r - l + 1 > k + 1:
                mp[nums[l]] -= 1
                l += 1
            if mp[nums[r]] > 1:
                return True
        
        return False
                

        

            
