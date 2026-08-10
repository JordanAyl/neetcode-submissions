class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        count = Counter(arr)
        lists = deque()

        for i in arr:
            if count[i] == 1:
                lists.append(i)

        if len(lists) >= k:
            return lists[k-1]

        return ""