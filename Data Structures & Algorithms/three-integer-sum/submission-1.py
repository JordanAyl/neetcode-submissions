class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """Two Pointer"""
        """Needs Sorting"""
        """moving left and intial to the right will increase the total"""
        """move right to the left to decrease total"""
        sumsList = []

        nums.sort()
        for i in range(len(nums)):


            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[right] + nums[left] + nums[i]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    sumsList.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return sumsList

