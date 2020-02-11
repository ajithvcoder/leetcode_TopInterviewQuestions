class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        if a==-b:
            return 0
        if (abs(a)>abs(b)):
            a,b=b,a
        if a<0:
            return -self.getSum(-a,-b)
        # if b==0:
        #     return a
        while b:
            c=a&b
            a=a^b
            b=c<<1
        return a
        