class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        curr = 0
        l = 0
        count = 0
        for r in range(len(arr)):
            curr += arr[r]

            if r - l + 1 > k:
                curr -= arr[l]
                l += 1
            
            if r - l + 1 == k and curr >= target:
                count += 1

        return count


            