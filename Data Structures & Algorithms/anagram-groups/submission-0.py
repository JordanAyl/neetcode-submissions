class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashstr = {}
        gramList = []

        for strg in strs:
            key = tuple(sorted(strg))

            if key in hashstr:
                hashstr[key].append(strg)
            else:
                hashstr[key] = [strg]

        return list(hashstr.values())

                
        






            
            
            


        