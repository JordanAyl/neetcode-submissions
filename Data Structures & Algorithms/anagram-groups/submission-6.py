class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            lst = [0] * 26

            for s in word:
                lst[ord('a') - ord(s)] += 1

            mp[tuple(lst)].append(word)

        return list(mp.values())