class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        su=0
        for i in range(len(s)-1,0,-1):
            if(dic.get(s[i])>dic.get(s[i-1])):
                su=su - (2*dic.get(s[i-1]))
            su=su+dic.get(s[i])
        return(su+dic.get(s[0]))
