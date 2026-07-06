class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        
        
        for i in strs:
            ltr = [0] * 26
            for j in i:
                ltr[ord(j) - ord('a')] += 1

            ana[tuple(ltr)].append(i)

        return list(ana.values())
            

        






            
            
            


        