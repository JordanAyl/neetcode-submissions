class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hasht = Counter(magazine)

        for i in ransomNote:
            
            if i not in hasht:
                return False
            hasht[i] -= 1
            if hasht[i] < 0:
                return False

        return True
