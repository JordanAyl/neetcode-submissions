class Solution:
    """def twoSum(self, nums, target):
        indices = [];
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    indices.append(i);
                    indices.append(j);
                    return indices;
"""

    """ Hashmap/Dictionary version coded myself"""

    def twoSum(self, nums, target):
        dic = {};
        for i, n in enumerate(nums):
            dic[n] = i;

        for i, n in enumerate(nums):
            diff = target - n;
            if diff in dic and i != dic[diff]:
                return [i, dic[diff]]
        return []



        