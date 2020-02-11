class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNum = str(x)
        
        strNum = list(strNum)
        
        return (strNum == strNum[::-1])