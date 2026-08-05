class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for i in range(len(strs)):
            ana["".join(sorted(strs[i]))].append(strs[i])

        new = list(ana.values())
        res = []
        for i in range(len(new)):
            tmp = new.pop(0)
            res.append(tmp)
        
        return res
