class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = list(s)
        word2 = list(t)
        
        return sorted(word1)==sorted(word2)