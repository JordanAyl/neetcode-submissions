class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        length = max(len(nums1), len(nums2))
        n1 = set(nums1)
        n2 = set(nums2)
        
        nset1 = set()
        nset2 = set()
        for i in range(length):
            if i < len(nums1) and nums1[i] not in n2:
                nset1.add(nums1[i])

            if i < len(nums2) and nums2[i] not in n1:
                nset2.add(nums2[i])

        return [list(nset1), list(nset2)]
            