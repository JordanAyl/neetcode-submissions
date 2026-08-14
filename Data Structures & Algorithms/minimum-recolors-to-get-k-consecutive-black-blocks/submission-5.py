class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        mp = {}
        l = 0
        lowf = float("inf")
        for r in range(len(blocks)):
            mp[blocks[r]] = mp.get(blocks[r], 0) + 1

            if r - l + 1 > k:
                mp[blocks[l]] -= 1
                l += 1
            if r - l + 1 == k:
                if 'W' in mp:
                    lowf = min(lowf, mp['W'])
                else:
                    lowf = 0
        return lowf
